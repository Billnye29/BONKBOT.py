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

    try:
        def run_bot(r, comments_replied_to):
            # Response to words detected in the keywords section
            bonk_responses = [
                "No horny!",
                "Control yourself or I'll have to send you to horny jail",
                "You've been bonked! for being indecent"
            ]
            # Adds a dogebonk meme at the end of each reply, to add new memes format the response as shown below
            bonk_meme_linkers = [
                "[BONK!!!](https://imgur.com/a/3RZr2OU)",
                "[BONK!!!](https://imgur.com/a/PJ5OAFy)",
                "[BONK!!!](https://imgur.com/a/y9jq5xy)",
                "[BONK!!!](https://imgur.com/a/BOSBdQk)",
                "[BONK!!!](https://imgur.com/a/ra6T0Gj)",
                "[BONK!!!](https://imgur.com/a/7xHO16H)",
            ]
            shill_response = [
                "Doctors recommend that you should avoid DogeBonk if you are allergic to getting BONKED! DogeBonk contract 0xae2df9f730c54400934c06a17462c41c08a06ed8"
            ]
            # Words that the bot looks for to respond to.
            keywords = ["horny", " horny ", "Horny", " horny ", "sex", " sex ", "cumming", " cumming ", " sexy ",
                        "sexy"]
            shillKeyWords = ["What is dogebonk", "how to buy dogebonk", "buying dogebonk",
                             "What is dobo", "Dogebonk is a rug",
                             "Dogebonk is a scam", "Dogebonk is a scam", "DogeBonk", " dogebonk "]
            # Handles the random selection of responses in the lists.
            random_bonk_response = random.choice(bonk_responses)
            random_bonk_meme = random.choice(bonk_meme_linkers)
            random_bonk_shill = random.choice(shill_response)
            # Subreddit list Controls what sub the bot is shilling in
            subreddits_list = "dogecoin+CryptoMoonShots+SatoshiStreetBets"
            subreddits = r.subreddit(subreddits_list)
            print("Starting Scan!")
            # Limit controls how many comments the bot scans
            for comment in subreddits.comments(limit=10000000):
                for keyword in keywords:
                    comment_lower = comment.body.lower()
                    if keyword in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                        try:
                            print("String with KEYWORD found in comment " + comment.id)
                            comment.reply(
                                random_bonk_response + "    -This comment was automatically BONKED! " + random_bonk_meme)
                            print("Replied to comment " + comment.id)
                            # Prevents the bot from replying to itself and the same comments over and over again.
                            comments_replied_to.append(comment.id)
                            with open("comments_replied_to.txt", "a") as f:
                                f.write(comment.id + "\n")
                                time.sleep(10)
                        except:
                            print("Something went wrong, thread may be locked?")

                for shillKeyWord in shillKeyWords:
                    comment_lower = comment.body.lower()
                    if shillKeyWord in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                        try:
                            print("String with SHILLKEYWORD found in comment " + comment.id)
                            comment.reply(
                                random_bonk_shill + " -This comment was automatically BONKED! " + random_bonk_meme)
                            # Prevents the bot from replying to itself and the same comments over and over again.
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
            # Sleeps for 10 seconds, prevents the bot from getting rate limited
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
        {
            print("Trying again")
        }
    while True:
        run_bot(r, comments_replied_to)
