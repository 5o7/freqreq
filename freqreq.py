# Import tools

import praw
import time

# Credentials and website access

creds = {"client_id": "X",
         "client_secret": "X",
         "password": "X",
         "user_agent": "X",
         "username": "X"}

reddit = praw.Reddit(client_id=creds["client_id"],
                     client_secret=creds["client_secret"],
                     password=creds["password"],
                     user_agent=creds["user_agent"],
                     username=creds["username"])

# Variables to store the wiki page, the genres, and their data groups

wiki = reddit.subreddit("X").wiki["X"].content_md.split("##")
categories = []
tables = []

# Grab data from the wiki page and store it in lists

for i in wiki:
    categories.append(i.split("|")[0].split("\n")[0].lower() + "!")
    tables.append(i.split("\n\n\n")[0])

# Grab ten new submissions, store the comment forests into a list

while True:
    for submission in reddit.subreddit("5o7bot").new(limit=1):
        comments = submission.comments.list()

        # Safeguard to avoid spamming

        task_complete = False
        for comment in comments:
            if str(comment.author) == "X":
                task_complete = True
                break

        # If any comment contains a category name, comment the category and table

        if not task_complete:
            for comment in comments:
                if not task_complete:
                    for i in range(1, 58):
                        if not task_complete:
                            if categories[i] in comment.body.lower():
                                entry = tables[i]
                                comment.reply(entry)
                                print(entry)
                                task_complete = True
                                break

    # Take a nap

    time.sleep(900)

