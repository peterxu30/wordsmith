#!/usr/bin/env python3

import keyboard, enchant
import regex as re
from collections import defaultdict

DICTIONARY = enchant.Dict("en_US")

record = keyboard.start_recording()

if __name__ == '__main__':
    closeInput = input("Press ENTER to exit and see summary")
    print("Generating summary...")

    keyboard.stop_recording()
    events = list(record[0].queue)
    strings = keyboard.get_typed_strings(events, allow_backspace=True)

    new_words = defaultdict(int)
    for string in strings:
        print("s: "+string)
        words = re.split("(?![\-'])\W+", string)
        print(words)
        for word in words:
            if word == '':
                continue

            if not DICTIONARY.check(word):
                new_words[word] += 1
    print(new_words)
