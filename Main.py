#USE THIS VIDEO AS A GUIDE IF YOU GET STUCK!! https://www.youtube.com/watch?v=3FpqXyJsd1s
#GO TO reddit.com/prefs/apps to get your client id and client secret.
#SET REDIRECT URL TO http://localhost

import praw
import time
import os
import random

print("Logged in!")


def bot_login():
    print("Logging in...")
    r = praw.Reddit(client_id="ENTER CLIENT ID HERE",
                    client_secret="ENTER SECRET ID HERE",
                    user_agent="<console:CREATE A NAME HERE:4.0>",
                    username='ACCOUNT USERNAME',
                    password='ACCOUNT PASSWORD')
    print("Logged in!")

    return r


try:
    def run_bot(r, comments_replied_to):
        # Bot shilling responses
        # Adds a dogebonk meme at the end of each reply, to add new memes format the response as shown below


        horny_responses2 = [
            "No horny!",
            "Control yourself or I'll have to send you to horny jail",
            "You've been bonked! for being indecent"
        ]
        meme_linkers = [
            "[BONK!!!](https://imgur.com/a/3RZr2OU)",
            "[BONK!!!](https://imgur.com/a/PJ5OAFy)",
            "[BONK!!!](https://imgur.com/a/y9jq5xy)",
            "[BONK!!!](https://imgur.com/a/BOSBdQk)",
            "[BONK!!!](https://imgur.com/a/ra6T0Gj)",
            "[BONK!!!](https://imgur.com/a/7xHO16H)",
        ]
        buying_Dogebonk2 = [
            "Doctors recommend that you should avoid DogeBonk if you are allergic to getting BONKED! DogeBonk contract 0xae2df9f730c54400934c06a17462c41c08a06ed8"
        ]
        # These keywords are used for shilling in multiple subreddits
        # If you want to use diffrent keywords for diffrent subs you just need to copy this block of code, rename the vars to something else and change all instances of the old variables
        keywords2 = ["horny", " horny ", "Horny", " horny ", "sex", " sex ", "cumming", " cumming ", " sexy ",
                     "sexy"]
        shillKeyWords2 = [ "What is dogebonk", "how to buy dogebonk", "buying dogebonk",
                           "What is dobo",  "Dogebonk is a rug",
                     "Dogebonk is a scam", "Dogebonk is a scam", "DogeBonk", " dogebonk "]
        random_index = random.choice(horny_responses2)
        random_index2 = random.choice(meme_linkers)
        # Subreddit list Controls what sub the bot is shilling in
        subreddits_list = "dogecoin+CryptoMoonShots+SatoshiStreetBets"
        subreddits = r.subreddit(subreddits_list)
        print("Starting Scan!")
        for comment in subreddits.comments(limit=10000000):
            for keyword in keywords2:
                comment_lower = comment.body.lower()
                if keyword in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                    try:
                        print("String with KEYWORD2 found in comment " + comment.id)
                        comment.reply(
                        random_index + "    -This comment was automatically BONKED! " + random_index2)
                        print("Replied to comment " + comment.id)
                        comments_replied_to.append(comment.id)
                        with open("comments_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                            time.sleep(10)
                    except:
                        print("Something went wrong, thread may be locked?")

            for shillKeyWord in shillKeyWords2:
                comment_lower = comment.body.lower()
                if shillKeyWord in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                    try:
                        print("String with SHILLKEYWORD2 found in comment " + comment.id)
                        comment.reply(
                        buying_Dogebonk2[0] + " -This comment was automatically BONKED! " + random_index2)
                        print("Replied to comment " + comment.id)
                        comments_replied_to.append(comment.id)
                        with open("comments_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                            time.sleep(10)
                    except:
                        print("Something went wrong, thread may be locked?")





        print("Search Completed.")

        print(comments_replied_to)

        print("Sleeping for 10 seconds...")
        # Sleep for 10 seconds...
        time.sleep(10)


    def get_saved_comments():
        if not os.path.isfile("comments_replied_to.txt"):
            comments_replied_to = []
            comments_replied_to = list(comments_replied_to)
        else:
            with open("comments_replied_to.txt", "r") as f:
                comments_replied_to = f.read()
                comments_replied_to = comments_replied_to.split("\n")
                comments_replied_to = filter(None, comments_replied_to)
                comments_replied_to = list(comments_replied_to)

        return comments_replied_to


    r = bot_login()
    comments_replied_to = get_saved_comments()
    print(comments_replied_to)


except:
 { print("Trying again") }
while True:
    run_bot(r, comments_replied_to)


