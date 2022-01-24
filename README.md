![image](https://user-images.githubusercontent.com/78694043/150782168-b55eda6e-a31d-4796-9137-9a3af5d56807.png)


# Google Play Store App Example Scraper


This repository is for [Scrape Google Play Store App results in Python]() in SerpApi blog post with step-by-step explanation scraping process. _Link will be active soon_.

This is not a complete solution, although could be. There's exists a third-party solutions: [Python google-play-scraper](https://github.com/JoMingyu/google-play-scraper) 
without any external dependencies, and [JavaScript google-play-scraper](https://github.com/facundoolano/google-play-scraper).

**Example output** from current repository scraper (_3 out of 40 comments are show_):

```json
{
  "app_data": [
    {
      "app_name": "Super Mario Run",
      "app_type": "SoftwareApplication",
      "app_url": "https://play.google.com/store/apps/details/Super_Mario_Run?id=com.nintendo.zara&hl=en_US&gl=RU",
      "app_main_thumbnail": "https://play-lh.googleusercontent.com/5LIMaa7WTNy34bzdFhBETa2MRj7mFJZWb8gCn_uyxQkUvFx_uOFCeQjcK16c6WpBA3E",
      "app_description": "A new kind of Mario game that you can play with one hand.You control Mario by tapping as he constantly runs forward. You time your taps to pull off stylish jumps, midair spins, and wall jumps to gather coins and reach the goal!Super Mario Run can be downloaded for free and after you purchase the game, you will be able to play all the modes with no additional payment required. You can try out all four modes before purchase: World Tour, Toad Rally, Remix 10, and Kingdom Builder.\u25a0World TourRun and jump with style to rescue Princess Peach from Bowser\u2019s clutches! Travel through plains, caverns, ghost houses, airships, castles, and more.Clear the 24 exciting courses to rescue Princess Peach from Bowser, waiting in his castle at the end. There are many ways to enjoy the courses, such as collecting the 3 different types of colored coins or by competing for the highest score against your friends. You can try courses 1-1 to 1-4 for free.After rescuing Princess Peach, a nine-course special world, World Star, will appear.\u25a0Remix 10Some of the shortest Super Mario Run courses you'll ever play!This mode is Super Mario Run in bite-sized bursts! You'll play through 10 short courses one after the other, with the courses changing each time you play. Daisy is lost somewhere in Remix 10, so try to clear as many courses as you can to find her!\u25a0Toad RallyShow off Mario\u2019s stylish moves, compete against your friends, and challenge people from all over the world.In this challenge mode, the competition differs each time you play.Compete against the stylish moves of other players for the highest score as you gather coins and get cheered on by a crowd of Toads. Fill the gauge with stylish moves to enter Coin Rush Mode to get more coins. If you win the rally, the cheering Toads will come live in your kingdom, and your kingdom will grow. \u25a0Kingdom BuilderGather coins and Toads to build your very own kingdom.Combine different buildings and decorations to create your own unique kingdom. There are over 100 kinds of items in Kingdom Builder mode. If you get more Toads in Toad Rally, the number of buildings and decorations available will increase. With the help of the friendly Toads you can gradually build up your kingdom.\u25a0What You Can Do After Purchasing All Worlds\u30fb All courses in World Tour are playableWhy not try out the bigger challenges and thrills available in all courses?\u30fb Easier to get Rally TicketsIt's easier to get Rally Tickets that are needed to play Remix 10 and Toad Rally. You can collect them in Kingdom Builder through Bonus Game Houses and ? Blocks, by collecting colored coins in World Tour, and more.\u30fb More playable charactersIf you rescue Princess Peach by completing course 6-4 and build homes for Luigi, Yoshi, and Toadette in Kingdom Builder mode, you can get them to join your adventures as playable characters. They play differently than Mario, so why not put their special characteristics to good use in World Tour and Toad Rally?\u30fb More courses in Toad RallyThe types of courses available in Toad Rally will increase to seven different types of courses, expanding the fun! Along with the new additions, Purple and Yellow Toads may also come to cheer for you.\u30fb More buildings and decorations in Kingdom BuilderThe types of buildings available will increase, so you'll be able to make your kingdom even more lively. You can also place Rainbow Bridges to expand your kingdom.\u30fb Play Remix 10 without having to waitYou can play Remix 10 continuously, without having to wait between each game.*Internet connectivity required to play. Data charges may apply. May contain advertisements.",
      "app_content_rating": "Rated for 3+",
      "app_category": "GAME_ACTION",
      "app_operating_system": "ANDROID",
      "app_rating": 3.5,
      "app_reviews": "1616124",
      "app_author": "Nintendo Co., Ltd.",
      "app_author_url": "https://supermariorun.com/",
      "app_screenshots": [
        "https://play-lh.googleusercontent.com/dcv6Z-pr3MsSvxYh_UiwvJem8fktDUsvvkPREnPaHYienbhT31bZ2nUqHqGpM1jdal8",
        "https://play-lh.googleusercontent.com/SVYZCU-xg-nvaBeJ-rz6rHSSDp20AK-5AQPfYwI38nV8hPzFHEqIgFpc3LET-Dmu-Q",
        "https://play-lh.googleusercontent.com/Nne-dalTl8DJ9iius5oOLmFe-4DnvZocgf92l8LTV0ldr9JVQ2BgeW_Bbjb5nkVngrQ",
        "https://play-lh.googleusercontent.com/yIqljB_Jph_T_ITmVFTpmDV0LKXVHWmsyLOVyEuSjL2794nAhTBaoeZDpTZZLahyRsE",
        "https://play-lh.googleusercontent.com/5HdGRlNsBvHTNLo-vIsmRLR8Tr9degRfFtungX59APFaz8OwxTnR_gnHOkHfAjhLse7e",
        "https://play-lh.googleusercontent.com/bPhRpYiSMGKwO9jkjJk1raR7cJjMgPcUFeHyTg_I8rM7_6GYIO9bQm6xRcS4Q2qr6mRx",
        "https://play-lh.googleusercontent.com/7DOCBRsIE5KncQ0AzSA9nSnnBh0u0u804NAgux992BhJllLKGNXkMbVFWH5pwRwHUg",
        "https://play-lh.googleusercontent.com/PCaFxQba_CvC2pi2N9Wuu814srQOUmrW42mh-ZPCbk_xSDw3ubBX7vOQeY6qh3Id3YE",
        "https://play-lh.googleusercontent.com/fQne-6_Le-sWScYDSRL9QdG-I2hWxMbe2QbDOzEsyu3xbEsAb_f5raRrc6GUNAHBoQ",
        "https://play-lh.googleusercontent.com/ql7LENlEZaTq2NaPuB-esEPDXM2hs1knlLa2rWOI3uNuQ77hnC1lLKNJrZi9XKZFb4I",
        "https://play-lh.googleusercontent.com/UIHgekhfttfNCkd5qCJNaz2_hPn67fOkv40_5rDjf5xot-QhsDCo2AInl9036huUtCwf",
        "https://play-lh.googleusercontent.com/7iH7-GjfS_8JOoO7Q33JhOMnFMK-O8k7jP0MUI75mYALK0kQsMsHpHtIJidBZR46sfU",
        "https://play-lh.googleusercontent.com/czt-uL-Xx4fUgzj_JbNA--RJ3xsXtjAxMK7Q_wFZdoMM6nL_g-4S5bxxX3Di3QTCwgw",
        "https://play-lh.googleusercontent.com/e5HMIP0FW9MCoAEGYzji9JsrvyovpZ3StHiIANughp3dovUxdv_eHiYT5bMz38bowOI",
        "https://play-lh.googleusercontent.com/nv2BP1glvMWX11mHC8GWlh_UPa096_DFOKwLZW4DlQQsrek55pY2lHr29tGwf2FEXHM",
        "https://play-lh.googleusercontent.com/xwWDr_Ib6dcOr0H0OTZkHupwSrpBoNFM6AXNzNO27_RpX_BRoZtKIULKEkigX8ETOKI",
        "https://play-lh.googleusercontent.com/AxHkW996UZvDE21HTkGtQPU8JiQLzNxp7yLoQiSCN29Y54kZYvf9aWoR6EzAlnoACQ",
        "https://play-lh.googleusercontent.com/xFouF73v1_c5kS-mnvQdhKwl_6v3oEaLebsZ2inlJqIeF2eenXjUrUPJsjSdeAd41w",
        "https://play-lh.googleusercontent.com/a1pta2nnq6f_b9uV0adiD9Z1VVQrxSfX315fIQqgKDcy8Ji0BRC1H7z8iGnvZZaeg80",
        "https://play-lh.googleusercontent.com/SDAFLzC8i4skDJ2EcsEkXidcAJCql5YCZI76eQB15fVaD0j-ojxyxea00klquLVtNAw",
        "https://play-lh.googleusercontent.com/H7BcVUoygPu8f7oIs2dm7g5_vVt9N9878f-rGd0ACd-muaDEOK2774okryFfsXv9FaI",
        "https://play-lh.googleusercontent.com/5LIMaa7WTNy34bzdFhBETa2MRj7mFJZWb8gCn_uyxQkUvFx_uOFCeQjcK16c6WpBA3E",
        "https://play-lh.googleusercontent.com/pzvdI66OFjncahvxJN714Tu5pHUJ_nJK--vg0tv5cpgaGNvjfwsxC-SKxoQh9_n_wEcCdSQF9FeuZeI"
      ]
    }
  ],
  "app_user_comments": [
    {
      "user_name": "Misha t",
      "user_avatar": "https://play-lh.googleusercontent.com/a/AATXAJxvYKOfPVaqDZg0FOUjJOV-W3qR6r_cMAz0XMgU\\u003dmo",
      "comment": "Fun game, but it does not warns you that only World 1 (out of 6) is free, others are behind paywall. Dont spend your time if you want full game for free",
      "user_app_rating": "1",
      "user_comment_likes": "9",
      "user_comment_published_at": "2021-09-07 19:01:46",
      "user_comment_id": "gp:AOqpTOFb_Fc_r33sWOwoSN8Zq4DDV7C9xuPTLUatfAplVowAb0NJbym2jv3j2DHBjT1o89y4z4vNZPblN60png"
    },
    {
      "user_name": "Daniel Dayton",
      "user_avatar": "https://play-lh.googleusercontent.com/a/AATXAJwWBeaKPKK1OjD3H2PH9GkiMNrg3SVyqwBFdTuG\\u003dmo",
      "comment": "This is a great game. Worth the $10 for the full game in my opinion. I do have a dislike though. The Toad Run levels are always like the same 5 or 6 levels. I think making more levels should be an objective for the creators. It would be appreciated for sure. Overall its a legit game. Again, definitely recommend buying the full game. Happy gaming folks.",
      "user_app_rating": "4",
      "user_comment_likes": "22",
      "user_comment_published_at": "2022-01-21 06:57:49",
      "user_comment_id": "gp:AOqpTOFCfzdf3J6kQVCfu5WgYLf6l9JL-du8yNutnuC5tPeDBNdFgbiLJwrTJbvJjmsYvUHLpEmBfTx9ZriFvQ"
    },
    {
      "user_name": "B D",
      "user_avatar": "https://play-lh.googleusercontent.com/a-/AOh14GgooCmK9PNBUby-Pbwyp6qqOGiXFWXjkCpT_Ulw",
      "comment": "Played the game for a week, decided I liked it and paid the $9.99 for it. Worked for 2 or 3 days, I built up mad rally tickets and coins. Now I try to play and it says \\support code...\\ and wont allow me to play. Sent an inquiry and was told the game doesnt work on all devices. Funny, I was playing it just fine prior to paying the $9.99. I expect to be refunded, I clearly wouldnt have purchased a game that wasnt compatible with my device. The game worked fine, until it didnt.",
      "user_app_rating": "1",
      "user_comment_likes": "34",
      "user_comment_published_at": "2022-01-20 12:04:05",
      "user_comment_id": "gp:AOqpTOGvKVLd7aqq77oixx60R2dX1h1Z4K2PgP0Pa_zktffqGl9jc_GRv9Fj3duvOIwNXthTx_Lkw3T6FKfCoQ"
    }
  ]
}
```
