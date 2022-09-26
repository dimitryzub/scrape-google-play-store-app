import time, json, re
from parsel import Selector
from playwright.sync_api import sync_playwright


def run(playwright):
    page = playwright.chromium.launch(headless=True).new_page()
    page.goto("https://play.google.com/store/apps/details?id=com.collectorz.javamobile.android.books&hl=en_GB&gl=US")

    user_comments = []

    # if "See all reviews" button present
    if page.query_selector('.Jwxk6d .u4ICaf button'):
        print("the button is present.")

        print("clicking on the button.")
        page.query_selector('.Jwxk6d .u4ICaf button').click(force=True)

        print("waiting a few sec to load comments.")
        time.sleep(4)
        
        last_height = page.evaluate('() => document.querySelector(".fysCi").scrollTop')  # 2200

        while True:
            print("scrolling..")
            page.query_selector('.h3YV2d').click(force=True)
            page.keyboard.press("End")
            time.sleep(3)

            new_height = page.evaluate('() => document.querySelector(".fysCi").scrollTop')

            if new_height == last_height:
                break
            else:
                last_height = new_height

    selector = Selector(text=page.content())
    page.close()

    print("done scrolling. Exctracting comments...")
    for index, comment in enumerate(selector.css(".RHo1pe"), start=1):

        comment_likes = comment.css(".AJTPZc::text").get()   

        user_comments.append({
            "position": index,
            "user_name": comment.css(".X5PpBb::text").get(),
            "user_avatar": comment.css(".gSGphe img::attr(srcset)").get().replace(" 2x", ""),
            "user_comment": comment.css(".h3YV2d::text").get(),
            "comment_likes": comment_likes.split("people")[0].strip() if comment_likes else None,
            "app_rating": re.search(r"\d+", comment.css(".iXRFPc::attr(aria-label)").get()).group(),
            "comment_date": comment.css(".bp9Aid::text").get(),
            "developer_comment": {
                "dev_title": comment.css(".I6j64d::text").get(),
                "dev_comment": comment.css(".ras4vb div::text").get(),
                "dev_comment_date": comment.css(".I9Jtec::text").get()
            }
        })

    print(json.dumps(user_comments, indent=2, ensure_ascii=False))


with sync_playwright() as playwright:
    run(playwright)
