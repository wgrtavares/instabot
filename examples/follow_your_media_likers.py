"""
    instabot example

    Workflow:
        Like and follow likers of last medias from your timeline feed.
"""

import argparse
import os
import random
import sys
import time

from tqdm import tqdm

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402


def follow(bot, user_id):
    bot.follow(user_id)
    return True

def follow_media_likers(bot, media):
    for user in tqdm(bot.get_media_likers(media), desc="Media likers"):
        follow(bot, user)
        time.sleep(10 + 20 * random.random())
    return True

def like_and_follow_your_feed_likers(bot):
    bot.logger.info("Starting follow_your_feed_likers")
    last_media = bot.get_your_medias()[0]
    return follow_media_likers(bot, last_media)

def follow_your_feed_likers(bot, seqNumber=0):
    bot.logger.info("Starting follow_your_feed_likers")
    last_media = bot.get_your_medias()[seqNumber]
    return follow_media_likers(bot, last_media)


parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="user")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
args = parser.parse_args()

bot = Bot(max_follows_per_day=500, filter_users=False)
bot.login(username=args.u, password=args.p)

follow_your_feed_likers(bot, 7)
