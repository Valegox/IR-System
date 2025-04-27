Love songs (25):

pertinent = [
    "attention",
    "badromance",
    "creep",
    "despacito",
    "heartbreaker",
    "iWantitthatWay",
    "IWantToHoldYourHand",
    "IWantYouBack",
    "IWantYouToWantMe",
    "IWillAlwaysLoveYou",
    "JustTheWayYouAre",
    "LivinOnAPrayer",
    "NewRules",
    "PokerFace",
    "RollingInTheDeep",
    "Smooth",
    "StayWithMe",
    "TakeABow",
    "TeenageDream",
    "TheNightWeMet",
    "TheWayYouMakeMeFeel",
    "Umbrella",
    "UptownGirl",
    "WakeMeUpBeforeYouGoGo",
    "YouCantHurryLove",
]


Songs to dance (13):

pertinent = [
    "BeautyandaBeat",
    "CantStopTheFeeling",
    "DANCE",
    "Firework",
    "Imsoexcited",
    "Justanillusion",
    "StayinAlive",
    "Summer",
    "Thriller",
    "Titanium",
    "UptownFunk",
    "WakeMeUp",
    "WakeMeUpBeforeYouGoGo",
    "iloverocknroll",
    "hipsdontlie",
]


Songs about breakup / heartache (7):

pertinent = [
    "Creep",
    "Rollinginthedeep",
    "TakeABow",
    "Heartbreaker",
    "TheNightWeMet",
    "NewRules",
    "MrBrightside",
]





Précision:
    docs pertinents récupérés / docs total récupérés

Recall:
    docs pertinents récupérés / docs total pertinents


    print(f"----- {len(result)} unsorted results: -----")
    p = 0
    for doc in result:
        a = ''
        if docNames[doc].lower() in [x.lower() for x in pertinent]:
            a = '*'
            p += 1
        print(f'{doc} {docNames[doc]} {a}')
    print("--------------------")
    print(f"Pertinent documents: {p} out of {len(result)}")
