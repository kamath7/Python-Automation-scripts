from dotenv import load_dotenv
import os
import praw

load_dotenv()


reddit = praw.Reddit(user_agent=True, client_id=os.environ["REDDIT_CLIENT_ID"], client_secret = os.environ["REDDIT_CLIENT_SECRET"], username=os.environ["REDDIT_USERNAME"],password=os.environ["REDDIT_PASS"])
url = "https://www.reddit.com/r/UnethicalLifeProTips/comments/x63343/ulpt_request_disable_the_microwave_without_my/"

post = reddit.submission(url=url)
print(post.title)
print(post.selftext)

for comment in post.comments:
    print(comment.body)