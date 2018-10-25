from django.shortcuts import render

from collections import defaultdict
from random import choice

# Variable to store words
text_dict = defaultdict(list)

def index(request):
    if request.method == 'POST':
        text = request.POST['textInput'].split()
        output_length = int(request.POST['outputLength'])

        # Create dictionary of words, with list of words
        # that follow that word.
        for word, next_word in zip(text, text[1:]):
            text_dict[word].append(next_word)

        starting_word = text[0]

        text = markov(output_length, starting_word)

        context = {
            'text': text,
            'input': request.POST['textInput']
        }
        return render(request, 'mainsite/index.html', context)
    else:
        return render(request, 'mainsite/index.html')

def markov(length, word):
    result = ""

    # Loop picks random words from list, for each
    # word in dictionary.
    for i in range(length):
        print(word, end=' ')
        result += word + ' '
        # If list for the word is empty, make 'the',
        # the next word.
        try:
            word = choice(text_dict[word])
        except:
            word = 'the'
    return 'The ' + result[:-1] + '.'
