"""
Dropbox question

"""

def get_autocomplete_score(substr, hashmap):
    score = 0
    keys = hashmap.keys()

    potential_words = []

    # O(N)
    for key in keys:
        if substr in key:
            potential_words.append((key, hashmap[key]))

    # O(N)
    if potential_words:
        max_word = max(potential_words, key=lambda x:x[1])  # (ANIMALS, 10)
        score = max_word[1]

    return score


def main():
    titles = ['ANIMALS', 'DOG FACTS']
    bodies = ['ANT ANTELOPE CAMEL CAT DOG', 'FURRY FURRY LOYAL']

    hashmap = {}

    # O(N) space
    for title in titles:
        words = title.split()

        for word in words:
            hashmap[word] = hashmap.get(word, 0) + 10


    for body in bodies:
        words = body.split()

        for word in words:
            hashmap[word] = hashmap.get(word, 0) + 1


    print(get_autocomplete_score('AN', hashmap))
    print(get_autocomplete_score('CAT', hashmap))
    print(get_autocomplete_score('DOG', hashmap))
    print(get_autocomplete_score('FURRY', hashmap))
    print(get_autocomplete_score('DO', hashmap))
    print(get_autocomplete_score('FUR', hashmap))
    print(get_autocomplete_score('ELEPH', hashmap))

main()

# N is # of words
# TIME: O(N)
# SPACE: O(N)