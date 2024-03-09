#Name: Lehi Chaves
#CSE111 - Programming with functions
#Week 2
#Activity - Prove Milestone: Sentences


import random

def main():

    quantity = 1
    tense = "past"
    sentence = make_sentence(quantity, tense)
    print(f"{sentence}")

    quantity = 1
    tense = "present"
    sentence = make_sentence(quantity, tense)
    print(f"{sentence}")

    quantity = 1
    tense = "future"
    sentence = make_sentence(quantity, tense)
    print(f"{sentence}")

    quantity = 2
    tense = "past"
    sentence = make_sentence(quantity, tense)
    print(f"{sentence}")

    quantity = 2
    tense = "present"
    sentence = make_sentence(quantity, tense)
    print(f"{sentence}")

    quantity = 2
    tense = "future"
    sentence = make_sentence(quantity, tense)
    print(f"{sentence}")

def make_sentence(quantity, tense):

    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    return f"{determiner} {noun} {verb}."

def get_determiner(quantity):
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    cap_word = word.capitalize()
    return word and cap_word

def get_noun(quantity):
      
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    cap_noun = noun.capitalize()
    return noun and cap_noun

def get_verb(quantity, tense):
    
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    verb = random.choice(verbs)
    cap_verb = verb.capitalize()
    return verb and cap_verb

main()