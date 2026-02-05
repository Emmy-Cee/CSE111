import random


def main():
    numbers = [10, 5, 2]
    # call with one argument (uses default quantity=1)
    append_random_numbers(numbers)
    # call with two arguments (provide quantity explicitly)
    append_random_numbers(numbers, 2)
    print(numbers)
    
    word_list = ['hello', 'world']
    # call with one argument (uses default quantity=1)  
    append_random_words(word_list)
    # call with two arguments (provide quantity explicitly)
    append_random_words(word_list, 3)
    print(word_list)


def append_random_numbers(numbers_list, quantity=1):
    """Append `quantity` random integers (1-100) to `numbers_list`.

    Returns the modified list for convenience.
    """
    for _ in range(quantity):
        numbers_list.append(random.randint(1, 100))
    return numbers_list

def append_random_words(words_list, quantity=1):
    """Append `quantity` random words to `words_list`.

    Returns the modified list for convenience.
    """
    sample_words = ['apple', 'banana', 'cherry', 'date', 'elderberry',
                    'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    for _ in range(quantity):
        words_list.append(random.choice(sample_words))
    return words_list
    


if __name__ == "__main__":
    main()