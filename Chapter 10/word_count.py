def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print("Sorry, the file " + filename + " does not exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

# filename = 'Chapter 10/alice.txt'
filenames = ['Chapter 10/alice.txt', 'Chapter 10/siddhartha.txt', 'Chapter 10/moby_dick.txt', 'Chapter 10/little_women.txt']
for filename in filenames:
    count_words(filename)