"""
    instabot example

    Workflow:
        Like and follow you last media likers.
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
        #time.sleep(10 + 20 * random.random())
        time.sleep(1)
    return True


parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
parser.add_argument("-media_id", type=str, help="media_id")
parser.add_argument("-follow_delay", type=float, help="follow_delay")
args = parser.parse_args()

bot = Bot(max_follows_per_day=500, follow_delay=args.follow_delay, filter_private_users=False)
bot.login(username=args.u, password=args.p)

follow_media_likers(bot, args.media_id)
