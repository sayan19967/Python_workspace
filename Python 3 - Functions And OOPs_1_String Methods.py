zenPython = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
'''

words = [i for i in zenPython.split()]
print(len(words))
words = [str.strip(' ,.-*!') for str in words]
print(words[3])
words = [str.lower() for str in words]
print(words[3])
unique_words = set(words)
print(len(unique_words))
word_frequency = {str:words.count(str) for str in words}
print(word_frequency['the'])
#print(word_frequency)
word_frequency = {str:word_frequency[str] for str in word_frequency.keys() if word_frequency[str] > 5}
print(len(word_frequency))
print(word_frequency)
