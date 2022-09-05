from dotenv import load_dotenv
import os
import praw
from datetime import datetime, timedelta

load_dotenv()


reddit = praw.Reddit(user_agent=True, client_id=os.environ["REDDIT_CLIENT_ID"], client_secret = os.environ["REDDIT_CLIENT_SECRET"], username=os.environ["REDDIT_USERNAME"],password=os.environ["REDDIT_PASS"])
subreddit = reddit.subreddit("greentext")

posts = []
for post in subreddit.new():
    current_time = datetime.utcnow()
    post_time = datetime.utcfromtimestamp(post.created)
    # print(current_time, post_time)

    delta_time = current_time - post_time 
    # print(delta_time)
    if delta_time <= timedelta(hours=24):
        # print(post.title, post.selftext)
        posts.append({post.title, post.selftext})


print(posts)

