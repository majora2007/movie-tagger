import re
import os


##wordlist = ['nudity', 'nude', 'topless', 'completly naked', 'naked', 'full frontal genitalia', 'breasts', 'penises', 'penis', 'nipples']

#wordlist_w = [{'keyword': 'nudity', 'weight': 1}, {'keyword': 'nudity', 'weight': 1}, {'keyword': 'no nudity', 'weight': -1}]


with open('wordlist.txt', 'r') as in_file:
    words = in_file.readlines()

wordlist = []
for word_pair in words:
    tokens = word_pair.split(':')
    if len(tokens) is 0:
        weight = 0
    else:
        weight = tokens[1]
    wordlist.append({'keyword': tokens[0], 'weight': float(weight)})

def parse_nudity(nude_list):
    """ Given a list of strings, calculate a score for if there is nudity or not """

    word_dict = count_words(nude_list)

    score = 0.0
    total = 0
    for pair in wordlist:
        score += (word_dict[pair['keyword']] * pair['weight'])
        total += word_dict[pair['keyword']]

    print('score: {0}'.format(score))
    print('total: {0}'.format(total))

    if total == 0:
        prob = 0
    else:
        prob = score / total

    return prob > 0.75, prob

def count_words(nude_list):
    word_dict = {}
    for pair in wordlist:
        word_dict[pair['keyword']] = 0    
    for nude_str in nude_list:
        for _, pair in enumerate(wordlist):
            word = pair['keyword']
            count = sum(1 for _ in re.finditer(r'\b(%s)\b' % re.escape(word), nude_str, re.IGNORECASE))
            word_dict[word] += count
    return word_dict

    