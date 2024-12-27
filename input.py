DIRECTIONS = ['n', 'north', 'e', 'east', 's', 'south', 'w', 'west', 'u', 'up', 'd', 'down']
VERBS = ['get', 'drop', 'fill', 'wield', 'kick', 'hit', 'look', 'dig', 'pick', 'dig', 'plant', 'grind', 'catch', 'sing']
NOUNS = ['sunflower', 'bench', 'jug', 'shovel', 'seeds', 'berry', 'apple', 'bowl', 'butterfly', 'net', 'book']
PREPOSITIONS = ['in', 'on', 'from']
ARTICLES = ['a', 'an', 'the']

# 0-VERB, 1-NOUN, 2-PREPOSITION, 3-NOUN

def remove_articles(input_list, ARTICLES):
    for word in input_list:
        if word in ARTICLES:
            input_list.remove(word)
    return input_list

def parse_input(input):
    raw_txt = input.strip().lowercase()
    split_txt = raw_txt.split()
    # if split_txt

