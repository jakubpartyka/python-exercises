import difflib
import json


def print_res(res_word):
    definition = data[res_word]
    print(len(definition), 'definition(s) found:\n')
    c = 1
    for res in definition:
        print(f"{c}.", res)
        c += 1


data = json.load(open('data/data.json'))

word = input("Provide a word:\n> ")
word = word.lower()

if word in data:
    print_res(word)
elif word.capitalize() in data:
    print_res(word.capitalize())
elif word.upper() in data:
    print_res(word.upper())
else:
    # print(f'No entry for \'{word}\' was found, double check the provided word')
    similar = difflib.get_close_matches(possibilities=data, word=word, n=1, cutoff=0.8)
    if len(similar) == 0:
        print(f'No entry for \'{word}\', please double-check this word')
    else:
        print(f'Hm, did you mean \'{similar[0]}\'?')
        resp = input("y/N > ")
        if resp == 'y':
            print_res(similar[0])
        else:
            print('ok, bye')
            exit()
