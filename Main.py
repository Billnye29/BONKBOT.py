#USE THIS VIDEO AS A GUIDE IF YOU GET STUCK!! https://www.youtube.com/watch?v=3FpqXyJsd1s
#GO TO reddit.com/prefs/apps to get your client id and client secret.
#SET REDIRECT URL TO http://localhost

import praw
import time
import os
import random

def bot_login():
    print("Logging in...")
    r = praw.Reddit(client_id="B0WEhLD7ajioKL_-YsFPhA",
                    client_secret="_qpgwEA6qWl_17qH9Agf2qLRoF4UEg",
                    user_agent="<console:43434fdE:4.0>",
                    username='ProfessionDull4738',
                    password='G4mer1234567890~')
    print("Logged in!")

    return r


def run_bot(r, comments_replied_to):
    #Bot shilling responses

    #Adds a dogebonk meme at the end of each reply, to add new memes format the response as shown below
    meme_linkers = [
        "[BONK!!!](https://imgur.com/a/3RZr2OU)",
        "[BONK!!!](https://imgur.com/a/PJ5OAFy)",
        "[BONK!!!](https://imgur.com/a/y9jq5xy)",
        "[BONK!!!](https://imgur.com/a/BOSBdQk)",
        "[BONK!!!](https://imgur.com/a/ra6T0Gj)",
        "[BONK!!!](https://imgur.com/a/7xHO16H)",

    ]
    horny_responses = [
        "Get Bonked!",
        "Bonk!",
        "Get Bonked!",
        "Bonk!",

    ]
    buying_Dogebonk = [
        "You can go to https://bonkswap.com/?utm_source=dogebonk.com or https://pancakeswap.finance/ to buy DogeBonk. Remember, the official DogeBonk contract is 0xae2df9f730c54400934c06a17462c41c08a06ed8 . If you are still having issues buying DogeBonk use this reddit post as a buying guide https://www.reddit.com/r/DogeBONK/comments/qawj0w/how_to_buy_bonks_now_with_pictures/! "
    ]
    #Bot Controls for r/dogebonk subreddit
    print("Searching last 1,000 comments in dogebonk")
    #Words that the bot looks for to respond to.
    keywords = ["horny", " horny ", "Horny", " horny ",  "Dogebonk is a rug", " Dogebonk is a rug ", " Dogebonk is a scam ", " Dogebonk is a scam ", "sex", " sex ", "cumming", " cumming ", " sexy ", "sexy"]
    shillKeyWords = [" how to buy ", " buy dogebonk ", " how to use pancakeswap", " buying dogebonk ", " help buying dogebonk ", " buy dobo ", "buy dobo"]
    #Controls what subreddit the bot is shilling in
    subreddits1 = r.subreddit("dogebonk")
    for comment in subreddits1.comments(limit=10000000):
        for keyword in keywords:
            comment_lower = comment.body.lower()
            if keyword in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with KEYWORD found in comment " + comment.id)
                random_index = random.randint(0, len(horny_responses) -1)
                random_index2 = random.randint(0, len(meme_linkers) -1)
                comment.reply(horny_responses[random_index] + "             -This comment was automatically BONKED!     " + meme_linkers[random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                #Prevents the bot from replying to itself and the same comments over and over again.
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
        for shillKeyWord in shillKeyWords:
            comment_lower = comment.body.lower()
            if shillKeyWord in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with SHILLKEYWORD found in comment " + comment.id)
                random_index2 = random.randint(0, len(meme_linkers) - 1)
                comment.reply(buying_Dogebonk[0] + " -This comment was automatically BONKED! " + meme_linkers[random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
    #These keywords are used for shilling in multiple subreddits
    #If you want to use diffrent keywords for diffrent subs you just need to copy this block of code, rename the vars to something else and change all instances of the old vars to the new name.
    horny_responses2 = [
        "Get Bonked!",
        "Bonk!",
        "Bonked!",
    ]
    buying_Dogebonk2 = [
        "Doctors recommend that you should avoid DogeBonk if you are allergic to money! DogeBonk contract 0xae2df9f730c54400934c06a17462c41c08a06ed8"
    ]
    keywords2 = ["horny", " horny ", "Horny", " horny ",  "Dogebonk is a rug", " Dogebonk is a rug ", " Dogebonk is a scam ", " Dogebonk is a scam ",  "sex", " sex ", "cumming", " cumming ", " sexy ", "sexy"]
    shillKeyWords2 = [" dogebonk ", "dogebonk", " how to buy dogebonk", " buying dogebonk ",
                     " help buying dogebonk ", "dobo", " dobo "]
    #Subreddit list ontrols what sub the bot is shilling in
    print("Searching last 1,000 comments in dogecoin")
    subreddits_list = ("dogecoin")
    subreddits = r.subreddit(subreddits_list)
    for comment in subreddits.comments(limit=10000000):
        for keyword in keywords2:
            comment_lower = comment.body.lower()
            if keyword in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with KEYWORD2 found in comment " + comment.id)
                random_index = random.randint(0, len(horny_responses) -1)
                random_index2 = random.randint(0, len(meme_linkers) - 1)
                comment.reply(horny_responses2[random_index] + "     -This comment was automatically BONKED! " + meme_linkers[random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
        for shillKeyWord in shillKeyWords2:
            comment_lower = comment.body.lower()
            if shillKeyWord in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with SHILLKEYWORD2 found in comment " + comment.id)
                random_index2 = random.randint(0, len(meme_linkers) - 1)
                comment.reply(buying_Dogebonk2[0] + " -This comment was automatically BONKED! " + meme_linkers[random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
     #Inorder to add more subreddits to shill in copy this entire block of code from here
    #If you are copying this block of code to shill in other subs make sure to rename the var subreddits3 to another name
    #Make sure to update all instances of the old var with your new name or it won't work
    print("Searching last 1,000 comments in ShibArmy")
    subreddits3 = r.subreddit("ShibArmy")
    for comment in subreddits3.comments(limit=10000000):
        for keyword in keywords2:
            comment_lower = comment.body.lower()
            if keyword in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with KEYWORD3 found in comment " + comment.id)
                random_index = random.randint(0, len(horny_responses) - 1)
                random_index2 = random.randint(0, len(meme_linkers) - 1)
                comment.reply(horny_responses2[random_index] + "     -This comment was automatically BONKED! " + meme_linkers[random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
        for shillKeyWord in shillKeyWords2:
            comment_lower = comment.body.lower()
            if shillKeyWord in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with SHILLKEYWOR3 found in comment " + comment.id)
                random_index2 = random.randint(0, len(meme_linkers) - 1)
                comment.reply(buying_Dogebonk2[0] + " -This comment was automatically BONKED! " + meme_linkers[random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
        #copy to here
    print("Searching last 1,000 comments in Cryptocurrency")
    subreddits4 = r.subreddit("CryptoCurrency")
    for comment in subreddits4.comments(limit=10000000):
        for keyword in keywords2:
            comment_lower = comment.body.lower()
            if keyword in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with KEYWORD4 found in comment " + comment.id)
                random_index = random.randint(0, len(horny_responses) - 1)
                random_index2 = random.randint(0, len(meme_linkers) - 1)
                comment.reply(
                    horny_responses2[random_index] + "     -This comment was automatically BONKED! " +
                    meme_linkers[random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
        for shillKeyWord in shillKeyWords2:
            comment_lower = comment.body.lower()
            if shillKeyWord in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with SHILLKEYWOR4 found in comment " + comment.id)
                random_index2 = random.randint(0, len(meme_linkers) - 1)
                comment.reply(
                    buying_Dogebonk2[0] + " -This comment was automatically BONKED! " + meme_linkers[
                        random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
    print("Searching last 1,000 comments in SatoshiStreetBets")
    subreddits5 = r.subreddit("SatoshiStreetBets")
    for comment in subreddits5.comments(limit=10000000):
        for keyword in keywords2:
            comment_lower = comment.body.lower()
            if keyword in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with KEYWORD5 found in comment " + comment.id)
                random_index = random.randint(0, len(horny_responses) - 1)
                random_index2 = random.randint(0, len(meme_linkers) - 1)
                comment.reply(
                    horny_responses2[random_index] + "    -This comment was automatically BONKED! " +
                    meme_linkers[random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
        for shillKeyWord in shillKeyWords2:
            comment_lower = comment.body.lower()
            if shillKeyWord in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with SHILLKEYWOR5 found in comment " + comment.id)
                random_index2 = random.randint(0, len(meme_linkers) - 1)
                comment.reply(
                    buying_Dogebonk2[0] + " -This comment was automatically BONKED! " + meme_linkers[
                        random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
    print("Searching last 1,000 comments in CryptoMoonShots")
    subreddits5 = r.subreddit("CryptoMoonShots")
    for comment in subreddits5.comments(limit=10000000):
        for keyword in keywords2:
            comment_lower = comment.body.lower()
            if keyword in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with KEYWORD6 found in comment " + comment.id)
                random_index = random.randint(0, len(horny_responses) - 1)
                random_index2 = random.randint(0, len(meme_linkers) - 1)
                comment.reply(
                    horny_responses2[random_index] + "     -This comment was automatically BONKED! " +
                    meme_linkers[random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
        for shillKeyWord in shillKeyWords2:
            comment_lower = comment.body.lower()
            if shillKeyWord in comment_lower and comment.id not in comments_replied_to and comment.author != r.user.me():
                print("String with SHILLKEYWOR6 found in comment " + comment.id)
                random_index2 = random.randint(0, len(meme_linkers) - 1)
                comment.reply(
                    buying_Dogebonk2[0] + " -This comment was automatically BONKED! " + meme_linkers[
                        random_index2])
                print("Replied to comment " + comment.id)
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
                    time.sleep(10)
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

while True:
    run_bot(r, comments_replied_to)

