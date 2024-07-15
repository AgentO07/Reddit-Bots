import praw
import time
import random

reddit = praw.Reddit(
    client_id="V2nUjlnyQRhPfywfwLDafw",
    client_secret="Z1qR3KeOwkTjfK4Xbi6xlXLKOoqdAA",
    user_agent="Bitch-Umbridge_Insulter 1.0",
    username= "Umbridge-Bot",
    password= "Gryffindor")
subreddit = reddit.subreddit("harrypotter")

Insults = ["Hem Hem. Detention",
           "Students will raise their hands when they speak in my class.",
           "So silly of me but it sounds as if you're questioning my authority in my own classroom.",
           "Things at Hogwarts are far worse than I feared.",
           "The Cruiciatus Curse ought to loosen your tounge.",
           "Enough! I will have order!"]

for submission in subreddit.hot(limit=30):   
   for comment in submission.comments:
      if hasattr(comment, "body"):
         comment_lower = comment.body.lower()
      if " umbridge " in comment_lower:
         print("_ _ _ _ _ _ _ _")
         print(comment.body)
         random_index = random.randint(0, len(Insults) - 1)
         comment.reply(Insults[random_index])
         time.sleep(200)

