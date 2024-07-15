import praw
import time
import random

reddit = praw.Reddit(
    client_id="liS6RK9BS1PERdC0N-l6iA",
    client_secret="N-Z5o7R9adpMNyXYUFMnytaCvx0guQ",
    user_agent="Mr.Malfoy_Insulter 1.0",
    username= "Draco-Malfoy-Bot",
    password= "Gryffindor")
subreddit = reddit.subreddit("harrypotter")

Insults = ["My Father Will Hear About This",
           "No one asked for your opinion you Filthy Little Mudblood!",
           "God, This Place has gone to the Dogs!",
           "This comment is Ridikulus!"]

for submission in subreddit.hot(limit=66):   
   for comment in submission.comments:
      if hasattr(comment, "body"):
         comment_lower = comment.body.lower()
      if " malfoy " in comment_lower:
         print("_ _ _ _ _ _ _ _")
         print(comment.body)
         random_index = random.randint(0, len(Insults) - 1)
         comment.reply(Insults)
         time.sleep(200)
