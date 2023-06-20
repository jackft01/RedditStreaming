import json
import socket
import praw
from datetime import datetime, timedelta
import pandas as pd

with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)  # Reading the config file
    print("Config data read successful", data)

reddit = praw.Reddit(
    client_id=data["client_id"],
    client_secret=data["client_secret"],
    user_agent="COM3021 Listener")

# Set up an empty pandas dataframe with the columns for the data we will be collecting.
cols = ["author", "id", "submission", "body", "subreddit", "created_utc", "collected_utc"]
data = pd.DataFrame(columns=cols)

stream = reddit.subreddit("AskUK+AskAnAmerican").stream

i = 0
start_datetime = []
hours = []

# Indicator of whether 24 hours has passed or not.
has24 = False

# While 24 hours has not passed do this.
while not has24:
    # If there is a network error during our runtime, it will be caught and we will return to the start of the for loop.
    # It will keep trying to reconnect until a network is found.
    try:
        for comments in stream.comments(skip_existing=True):

            # Datetime at the time the comment was retrieved.
            dt = datetime.now()

            # This is just an indicator of the code working.
            # Prints what hour it is at the turn of the hour.
            if dt.hour not in hours:
                print(dt.hour)
                hours.append(dt.hour)

            # This is the datetime when we started collecting comments.
            if i == 0:
                start_datetime.append(dt)

            # Check if 24 hours has passed since the start of the data collection.
            if start_datetime[0] + timedelta(days=1) < dt:
                has24 = True
                print("24 hours have passed since we started collecting data. \n Exiting loop!")
                break

            ts = datetime.timestamp(dt)

            # Append the row containing information about the column to our dataframe.
            data = data.append({"author": comments.author, "id": comments.id, "submission": comments.submission,
                                "body": comments.body,
                                "subreddit": comments.subreddit, "created_utc": comments.created_utc,
                                "collected_utc": ts}, ignore_index=True)

            i += 1
    except:
        print("Network Error. Reconnecting")

data.to_csv("reddit_data.csv", index=False)