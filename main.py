"""
Python twitter bot
"""

from twitter2 import Bot


if __name__ == '__main__':
    tw = Bot()
    tw.tweet("test")