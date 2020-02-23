import twitter
import os
import re
from dotenv import load_dotenv

dotenv_path = './.env'
load_dotenv(dotenv_path)

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN_KEY = os.getenv("ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)

users = ["adeam_kai", "daminist",
         "ITASHIKATANASHI", "likeparadox", "yaruki_kun", "savannah_mach", "norio_hangover", "rei_blue_", "akagohinehine", "gohikuniha3", "Sapporobrownman", "676141po", "e5rock", "anti_chikuwa", "meikyu_106", "STOP_TOMARE", "ten_cho_u", "100nincho_tiger", "8_niso", "Sgt_karaage", "Barbattler", "road_Loharu", "specialgenki", "Kuyou_again", "long_thrower", "sssgantan", "FAXXXX", "tonari_no_shiba", "ewe_your_you"]
with open("tweets.txt", mode="w") as f:
    for user in users:
        try:
            tweets = api.GetUserTimeline(
                screen_name=user, count=200, include_rts=False, exclude_replies=True)
        except:
            pass
        for t in tweets:
            text = t.text
            text = re.sub(
                r"(https?:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "", text)
            text = text.strip()
            print(text)
            f.write(text + '\n')
