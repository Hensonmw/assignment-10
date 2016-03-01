#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2 to Write a program to count word usage in the text
count the most 10 common words use collection module
"""
from collections import Counter

string = """Stars burn a very light type of air that is packed very tight in the
         middle of the star. The tiny pieces of the air join to form a slightly
         heavier type of air that can't burn in the star without the middle
         being much hotter and tighter.
         After a long time, all the very light air in the middle is used up.
         Then the star gets much hotter and tighter in the middle, so it can
         burn the slightly heavier air.
         It also also gets much bigger and cooler outside. But it is still
         so hot it will burn up any close-in worlds.The sun is a star and will
         do this after a very long time. It will get so big that it will burn
         our world all up. This will not happen for at least ten hundred
         hundred hundred hundred years, so we don't have to worry about it now.
         Long after that, a star like the sun will burn up all the slightly
         heavier air, too. Then it will become very tiny and hot and white, but
         will be so tiny it won't be able to keep its worlds warm. It will keep
         cooling off over a very very long time. The worlds that are left will
         be all ice.
         But stars that are heavier can go on to burn heavier and heavier
         things, until finally they make the biggest flash we know. That is
         their end. """


def lowercase_replace(string):
    """
    remove, and change all characters to lower case. count the top 10 common
    words
    """
    text_1 = string.replace(",", " ").replace(".", " ").casefold()
    text_2 = text_1.split()
    mostcommon = Counter(text_2).most_common(10)
    return mostcommon


def main():
    result = lowercase_replace(string)
    print(result)

if __name__ == '__main__':
    main()
