![image](https://user-images.githubusercontent.com/78694043/150782168-b55eda6e-a31d-4796-9137-9a3af5d56807.png)


# Scrape Google Play Store App 

This repository is for [Scrape Google Play Store App results in Python](https://serpapi.com/blog/scrape-google-play-store-app-in-python/) blog post at SerpApi with step-by-step explanation scraping process.

This is not a complete solution, although could be. There's exists a complete third-party solutions like [Python `google-play-scraper`](https://github.com/JoMingyu/google-play-scraper) without any external dependencies, and [JavaScript `google-play-scraper`](https://github.com/facundoolano/google-play-scraper). which you might like better. 

This repo and blog post is for someone who's looking to learn and/or build something on their own by adding thing on top of it since it's easier than addining things to the package.

#### Example output

```json
{
  "basic_info": {
    "developer": {
      "name": "Nintendo Co., Ltd.",
      "url": "https://supermariorun.com/",
      "email": "supermariorun-support@nintendo.co.jp"
    },
    "downloads_info": {
      "long_form_not_formatted": "100,000,000+",
      "long_form_formatted": "100000000",
      "as_displayed_short_form": "100M+",
      "actual_downloads": "211560819"
    },
    "name": "Super Mario Run",
    "type": "SoftwareApplication",
    "url": "https://play.google.com/store/apps/details/Super_Mario_Run?id=com.nintendo.zara&hl=en_GB&gl=US",
    "description": "Control Mario with just a tap!",
    "application_category": "GAME_ACTION",
    "operating_system": "ANDROID",
    "thumbnail": "https://play-lh.googleusercontent.com/3ZKfMRp_QrdN-LzsZTbXdXBH-LS1iykSg9ikNq_8T2ppc92ltNbFxS-tORxw2-6kGA",
    "content_rating": "Everyone",
    "rating": 4.0,
    "reviews": "1643139",
    "price": "0",
    "release_date": "22 Mar 2017",
    "images": [
      "https://play-lh.googleusercontent.com/yT8ZCQHNB_MGT9Oc6mC5_mQS5vZ-5A4fvKQHHOl9NBy8yWGbM5-EFG_uISOXmypBYQ6G",
      "https://play-lh.googleusercontent.com/AvRrlEpV8TCryInAnA__FcXqDu5d3i-XrUp8acW2LNmzkU-rFXkAKgmJPA_4AHbNjyY",
      "https://play-lh.googleusercontent.com/AESbAa4QFa9-lVJY0vmAWyq2GXysv5VYtpPuDizOQn40jS9Z_ji8HXHA5hnOIzaf_w",
      "https://play-lh.googleusercontent.com/KOCWy63UI2p7Fc65_X5gnIHsErEt7gpuKoD-KcvpGfRSHp-4k8YBGyPPopnrNQpdiQ",
      "https://play-lh.googleusercontent.com/iDJagD2rKMJ92hNUi5WS2S_mQ6IrKkz6-G8c_zHNU9Ck8XMrZZP-1S_KkDsA6KDJ9No",
      "https://play-lh.googleusercontent.com/QsdO8Pn6qxvfAi4es7uicI-xB21dPN3s8SBfmnuXPjFftdXCuugxis7CDJbAkQ_pzA",
      "https://play-lh.googleusercontent.com/oEIUG3KTnijbe5TH3HO3NMAF5Ai8LkIAtKOO__TduDq4wOzGQA2PzZlBJg2C4mURDR8",
      "https://play-lh.googleusercontent.com/BErkwcIVa4ldoVL56EvGWTQJ2nPu-Y6EFeAS4dfK7l0CufebWdrRC9CduHqNwysPYf8",
      "https://play-lh.googleusercontent.com/cw86ny78mbNHVRDLlhw1fxVbZxiYFC7yYDRY3Nt2dnRGihRhxo1eOy4IjrSVVzKW9Is",
      "https://play-lh.googleusercontent.com/Kx0gmRSH582Te-BeTo-C87f3hl-2sf7DRaWso3qZ46p9PZ97socE6FuK09vzebVF8AA",
      "https://play-lh.googleusercontent.com/OJhOUUZjTUw4e3EEbPlZnuKdmUIGdLSSwUgb5ygPfiO0h1SeHIl3s_L7R8xBDLVnjPU",
      "https://play-lh.googleusercontent.com/Z0Ggjrocxk7SRTAhFCL6ZEc04eCAdI09Xf08Th7dfn_ViIBrK7E8Bd1p3Lfi-pjiLLWz",
      "https://play-lh.googleusercontent.com/pn58u5DpcUNOgE4NOQc4jFJaFyR3EaiO0YWlekYdQmBV3Q6jrF_ioX78gbtH2eZTTA",
      "https://play-lh.googleusercontent.com/EItdRRArK4yI7LPArgKOhwTrcALMSFS41F49dOuX6c8a7XPw20WNfSiDrE7ZnIbTRME",
      "https://play-lh.googleusercontent.com/xDFJgEfAPeGcfk72Nfe9jE-7oDyMDYtucW4W0mYh3vV8YgMb2T91BQ1do1r_8fU-Sw",
      "https://play-lh.googleusercontent.com/Bn6SFuIjgL8CLHTB6C7t_Dv7MCGwAxh8OIV7z-gKhNpJtxss2Vqwl_50HdHFUyoet7s",
      "https://play-lh.googleusercontent.com/eEKSdZPf7yo-WWcb9tGLQ-O17XVbd02rGREHwWC79JDOgVZFTaWmi0s1vg2H4Mn51hI",
      "https://play-lh.googleusercontent.com/vlOYHPoi3AwQuAEAuWi1pu37cnxObDelQ5xQQP3ojAmptiJbBereG8Ugvlp_vihDS9c",
      "https://play-lh.googleusercontent.com/2PuQ1L2sE0opnEG9AywzAzNBIV0sZo1y1ftrJ518oPwgjtUJ6iUrKskgn8DWRClFQnM",
      "https://play-lh.googleusercontent.com/TvcAspZw7Tc1CQV3DJrzPL_I4sACQhvNhDqB90r9yiYfAnPOUk8gi1fFcT1NdAsKG_l-",
      "https://play-lh.googleusercontent.com/vpt0r-PxWy2ea8xvuPSg0cn3iNXrS1v6pCFzWSPOane0lkDcfIGoSTvhiFz_en4CePI",
      "https://play-lh.googleusercontent.com/3ZKfMRp_QrdN-LzsZTbXdXBH-LS1iykSg9ikNq_8T2ppc92ltNbFxS-tORxw2-6kGA",
      "https://play-lh.googleusercontent.com/iTZtyWYr4T-slu1nifgRqEhtMLmxcNagc2rDAyiWntDQWCVLlGR7rDvx0uK6z-zLujwv",
      "https://play-lh.googleusercontent.com/iTZtyWYr4T-slu1nifgRqEhtMLmxcNagc2rDAyiWntDQWCVLlGR7rDvx0uK6z-zLujwv"
    ],
    "video_trailer": "https://play-games.googleusercontent.com/vp/mp4/1280x720/qjHSn4GwQWY.mp4"
  },
  "user_comments": [
    {
      "user_avatar": "https://play-lh.googleusercontent.com/EGemoI2NTXmTsBVtJqk8jxF9rh8ApRWfsIMQSt2uE4OcpQqbFu7f7NbTK05lx80nuSijCz7sc3a277R67g",
      "user_rating": "3",
      "user_comment": "Now, while I love the Mario Series, I will say that I am not the biggest fan of this game. When playing Remix 10, I found that the screen lagged for seemingly no reason, which threw me off plenty of times. The level design also seems pretty bland and just the same old settings you see over and over again. Overall I feel like this was just another cash grab from Nintendo, not to mention you actually need to PAY to unlock the rest of the game. But other than that, it looks decent graphic-wise."
    }, ... other comments
    {
      "user_avatar": "https://play-lh.googleusercontent.com/EGemoI2NTXmTsBVtJqk8jxF9rh8ApRWfsIMQSt2uE4OcpQqbFu7f7NbTK05lx80nuSijCz7sc3a277R67g",
      "user_rating": "2",
      "user_comment": "Too many tutorials that dont even let you play until 5 minutes of tapping the screen. Then after only a few levels you have to pay for the rest of them. Nintendo makes so much money you\\'d think they could make a game that allowed you to pay to remove ads, not pay to play the game you installed in the first place. But when you aren\\'t being forcefed tutorials for a game you won\\'t play that long anyway, the gameplay is actually pretty fun and challenging. Those are the only pros."
    }
  ]
}
```
