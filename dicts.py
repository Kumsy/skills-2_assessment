"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_count = {}
    phrase = phrase.split(" ")

    for words in phrase:
        word_count[words] = word_count.get(words, 0) + 1

    return word_count

# TEST_CASES:
# print(count_words("each word appears once"))
# print(count_words("rose is a rose is a rose"))
# print(count_words("Porcupine see, porcupine do."))

def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

    Honeydew 2.50
    Cantaloupe 2.50
    Watermelon 2.95
    Musk 3.25
    Crenshaw 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If there are no melons at that price print "None found"

        >>> print_melon_at_price(2.50)
        Cantaloupe
        Honeydew

        >>> print_melon_at_price(2.95)
        Watermelon

        >>> print_melon_at_price(5.50)
        None found
    """

    melon_inventory = { 'Honeydew': 2.50,
                        'Cantaloupe': 2.50,
                        'Watermon': 2.95,
                        'Musk': 3.25,
                        'Crenshaw': 3.25,
                        'Christmas': 14.25}

    customer_price_melon = []                    
    
    for melons in melon_inventory:
        if (melon_inventory[melons] == price):
            customer_price_melon.append(melons)

    if customer_price_melon:
        for melons in sorted(customer_price_melon):
            print(melons)
    else:
        print("None found")
    
# TEST_CASES:
# print_melon_at_price(2.50)
# print_melon_at_price(2.95)
# print_melon_at_price(5.50)


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    pirate_dict =  {'sir': 'matey',
                    'hotel': 'fleabag inn',
                    'student': 'swabbie',
                    'man': 'matey',
                    'professor': 'foul blaggart',
                    'restaurant': 'galley',
                    'your': 'yer',
                    'excuse': 'arr',
                    'students': 'swabbies',
                    'are': 'be',
                    'restroom': 'head',
                    'my': 'me',
                    'is': 'be'}

    phrase_list = phrase.split()
    translated_phrase = []
    # translated_phrase = ''
    
    # Loop through user phrase word by word
    for word in phrase_list:
        # For each key in priate
        if word in pirate_dict:
            word = pirate_dict[word]

        translated_phrase.append(word)
        # translated_phrase = translated_phrase + ' ' + word

    return (" ".join(translated_phrase))

# TEST_CASES:
# print(translate_to_pirate_talk('get this man a shield'))
# print(translate_to_pirate_talk('get your man, a shield'))
# print(translate_to_pirate_talk("excuse me miss, where is the restaurant in your hotel"))
# print(translate_to_pirate_talk('before I leave the hotel I will use the restroom'))


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    used_names_dict = {}
    results_list = []
    letter = None

    while True:

        word_found = False

        # ***************************************
        for word in names:
            # If letter is not set word OR word[0] equals letter, run.
            if letter == None or (word[0] == letter 
                                    and word not in used_names_dict):
                # Add word to results, get last character in word
                # then put in dict 
                results_list.append(word)
                letter = word[-1:]
                used_names_dict[word] = None # Dict: Key and Value
                word_found = True
                break 
        # ****************************************

        if word_found == False:
            break

    return results_list
           
# TEST_CASES:
# print(kids_game(["bagon", "baltoy", "yamask", "starly", 
#                 "nosepass", "kalob", "nicky", "booger"]))
# print(kids_game(["apple", "berry", "cherry"]))
# print(kids_game(["noon", "naan", "nun"])) 