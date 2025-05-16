def popular_words(text, words):
    word_list = text.lower().split()
    return {word: word_list.count(word) for word in words}

# Тест
assert popular_words('''When I was One 
I had just begun 
When I was Two 
I was nearly new''', 
['i', 'was', 'one', 'two', 'three']) == {
    'i': 3,
    'was': 3,
    'one': 1,
    'two': 1,
    'three': 0
}, 'Test failed'

print('OK')