from dotenv import load_dotenv
import os
import praw
from datetime import datetime, timedelta

load_dotenv()


reddit = praw.Reddit(user_agent=True, client_id=os.environ["REDDIT_CLIENT_ID"], client_secret = os.environ["REDDIT_CLIENT_SECRET"], username=os.environ["REDDIT_USERNAME"],password=os.environ["REDDIT_PASS"])
subreddit = reddit.subreddit("test")
title = "Testing Reddit bot"
content = """
Hello there!
"""
subreddit.submit(title=title, selftext=content)