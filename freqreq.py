# Import tools

import praw
import time

# Two variables to hold user credentials and one is an instance of the website

creds = {"client_id": "X",
         "client_secret": "X",
         "password": "X",
         "user_agent": "Assign flair",
         "username": "5o7bot"}

reddit = praw.Reddit(client_id=creds["client_id"],
                     client_secret=creds["client_secret"],
                     password=creds["password"],
                     user_agent=creds["user_agent"],
                     username=creds["username"])

# Grab the frequently requested movies wiki

wiki = reddit.subreddit("5o7bot").wiki["faq"].content_md.split("##")

# a block of code that runs every 15 minutes

while True:

    # Examine 10 new submissions one at a time

    for submission in reddit.subreddit("5o7bot").new(limit=10):

        # Put comment forest into a single list

        comments = submission.comments.list()

        # Do not comment if I already commented

        task_complete = False
        for comment in comments:
            if str(comment.author) == "5o7bot":
                task_complete = True
                break

        # If I have not commented, check the comments for triggers

        if not task_complete:

            # For each comment in the submission, do the following

            for comment in comments:

                # Make the comment all lower case

                comment_lower = comment.body.lower()

                # A loop that runs 54 times

                for i in range(1, 54):

                    # Check if any  of the 54 FRM categories are in the comment string

                    if wiki[i].split("|")[0].split("\n")[0].lower() in comment_lower:

                        # compose an entry of the category's table

                        entry = "Frequently requested " + wiki[i].split("\n\n\n")[0]

                        # Publish a comment

                        comment.reply(entry)

                        # Print the comment

                        print(entry)
                        break

    # Take a 15 minute nap

    time.sleep(900)