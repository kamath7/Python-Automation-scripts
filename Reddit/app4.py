from re import sub
from dotenv import load_dotenv
import os
import praw
from datetime import datetime, timedelta

load_dotenv()


reddit = praw.Reddit(user_agent=True, client_id=os.environ["REDDIT_CLIENT_ID"], client_secret = os.environ["REDDIT_CLIENT_SECRET"], username=os.environ["REDDIT_USERNAME"],password=os.environ["REDDIT_PASS"])
subreddit = reddit.subreddit("test")

for post in subreddit.new():
    current_time = datetime.utcnow()
    post_time = datetime.utcfromtimestamp(post.created)

    delta_time = current_time - post_time 
    if delta_time <= timedelta(hours=24):
        if "bot" in post.title.lower():
            print(post.title)
            post.reply("This is a bot response")