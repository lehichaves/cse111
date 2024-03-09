#Name: Lehi Chaves
#CSE111 - Programming with functions
#Week 2
#Assignment - W02 Prove: Writing Functions

#I did Exceeding the Requirements to assignment - def get_adjective


import random

print()

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

    determiner = get_determiner(quantity).capitalize()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    adjective = get_adjective()
    return f"{determiner} {noun} {verb} {prepositional_phrase} {adjective}."

def get_prepositional_phrase(quantity):
    
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

def get_determiner(quantity):
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    
    word = random.choice(words)
    return word 

def get_noun(quantity):
      
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    return noun

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
    return verb

def get_preposition():

    list_preposition = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
   
    preposition = random.choice(list_preposition)
    return preposition

#Exceeding the Requirements to assignment

def get_adjective():

    list_adjective = ["golden", "silver", "sad", 
    "invisible", "green", "beautiful", "happy", 
    "tall", "short", "famous", "angry", "hungry"]

    adjective = random.choice(list_adjective)
    return adjective

main()

print()