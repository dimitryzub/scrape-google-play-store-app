from bs4 import BeautifulSoup
import requests, lxml, re, json

# https://requests.readthedocs.io/en/latest/user/quickstart/#custom-headers
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

# https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
params = {
    "id": "com.nintendo.zara",     # app name
    "gl": "US",                    # country of the search
    "hl": "en_GB"                  # language of the search
}


def google_store_app_data():
    html = requests.get("https://play.google.com/store/apps/details", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, "lxml")

    # where all app data will be stored
    app_data = {
        "basic_info":{
            "developer":{},
            "downloads_info": {}
        },
        "user_comments": []
    }
    
    # [11] index is a basic app information
    # https://regex101.com/r/zOMOfo/1
    basic_app_info = json.loads(re.findall(r"<script nonce=\"\w+\" type=\"application/ld\+json\">({.*?)</script>", 
                                           str(soup.select("script")[11]), re.DOTALL)[0])
     
    # https://regex101.com/r/6Reb0M/1
    additional_basic_info =  re.search(fr"<script nonce=\"\w+\">AF_initDataCallback\(.*?(\"{basic_app_info.get('name')}\".*?)\);<\/script>", 
            str(soup.select("script")), re.M|re.DOTALL).group(1)
    
    app_data["basic_info"]["name"] = basic_app_info.get("name")
    app_data["basic_info"]["type"] = basic_app_info.get("@type")
    app_data["basic_info"]["url"] = basic_app_info.get("url")
    app_data["basic_info"]["description"] = basic_app_info.get("description").replace("\n", "")  # replace new line character to nothing
    app_data["basic_info"]["application_category"] = basic_app_info.get("applicationCategory")
    app_data["basic_info"]["operating_system"] = basic_app_info.get("operatingSystem")
    app_data["basic_info"]["thumbnail"] = basic_app_info.get("image")
    app_data["basic_info"]["content_rating"] = basic_app_info.get("contentRating")
    app_data["basic_info"]["rating"] = round(float(basic_app_info.get("aggregateRating").get("ratingValue")), 1)  # 4.287856 -> 4.3
    app_data["basic_info"]["reviews"] = basic_app_info.get("aggregateRating").get("ratingCount")
    app_data["basic_info"]["reviews"] = basic_app_info.get("aggregateRating").get("ratingCount")
    app_data["basic_info"]["price"] = basic_app_info["offers"][0]["price"]
    
    app_data["basic_info"]["developer"]["name"] = basic_app_info.get("author").get("name")
    app_data["basic_info"]["developer"]["url"] = basic_app_info.get("author").get("url")
    
    # https://regex101.com/r/C1WnuO/1
    app_data["basic_info"]["developer"]["email"] = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", additional_basic_info).group(0)
    
    # https://regex101.com/r/Y2mWEX/1 (a few matches but re.search always matches the first occurence)
    app_data["basic_info"]["release_date"] = re.search(r"\d{1,2}\s[A-Z-a-z]{3}\s\d{4}", additional_basic_info).group(0)
    
    # https://regex101.com/r/7yxDJM/1
    app_data["basic_info"]["downloads_info"]["long_form_not_formatted"] = re.search(r"\"(\d+,?\d+,?\d+\+)\"\,(\d+),(\d+),\"(\d+M\+)\"", additional_basic_info).group(1)
    app_data["basic_info"]["downloads_info"]["long_form_formatted"] = re.search(r"\"(\d+,?\d+,?\d+\+)\"\,(\d+),(\d+),\"(\d+M\+)\"", additional_basic_info).group(2)
    app_data["basic_info"]["downloads_info"]["as_displayed_short_form"] = re.search(r"\"(\d+,?\d+,?\d+\+)\"\,(\d+),(\d+),\"(\d+M\+)\"", additional_basic_info).group(4)
    app_data["basic_info"]["downloads_info"]["actual_downloads"] = re.search(r"\"(\d+,?\d+,?\d+\+)\"\,(\d+),(\d+),\"(\d+M\+)\"", additional_basic_info).group(3)
    
    # https://regex101.com/r/jjsdUP/1
    # [2:] skips 2 PEGI logo thumbnails and extracts only app images 
    app_data["basic_info"]["images"] = re.findall(r",\[\d{3,4},\d{3,4}\],.*?(https.*?)\"", additional_basic_info)[2:]
    
    try:
        # https://regex101.com/r/C1WnuO/1
        app_data["basic_info"]["video_trailer"] = "".join(re.findall(r"\"(https:\/\/play-games\.\w+\.com\/vp\/mp4\/\d+x\d+\/\S+\.mp4)\"", additional_basic_info)[0])
    except:
        app_data["basic_info"]["video_trailer"] = None
    
    
    # User reviews
    # https://regex101.com/r/xDVZq7/1
    user_reviews = re.findall(r'Write a short review.*?<script nonce="\w+">AF_initDataCallback\({key:.*data:\[\[\[\"\w.*?\",(.*?)sideChannel: {}}\);<\/script>',
                                       str(soup.select("script")), re.DOTALL)
    
    # https://regex101.com/r/D6BIBP/1
    # [::3] to grab every 2nd (second) picture to avoid duplicates
    avatars = re.findall(r",\"(https:.*?)\"\].*?\d{1}", str(user_reviews))[::3]
    
    # https://regex101.com/r/18EziQ/1
    ratings = re.findall(r"https:.*?\],(\d{1})", str(user_reviews))
    
    # https://regex101.com/r/mSku7n/1
    comments = re.findall(r"https:.*?\],\d{1}.*?\"(.*?)\",\[\d+,\d+\]", str(user_reviews))
    
    for comment, rating, avatar in zip(comments, ratings, avatars):
        app_data["user_comments"].append({
            "user_avatar": avatar,
            "user_rating": rating,
            "user_comment": comment
        })


    print(json.dumps(app_data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    # https://stackoverflow.com/a/17533149/15164646
    # reruns script if `basic_app_info` or `additional_basic_info` throws an exception due to <script> position change
    while True: 
        try:
            google_store_app_data()
        except:
            pass
        else:
            break
