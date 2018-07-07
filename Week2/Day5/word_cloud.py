import unittest
import re

class WordCloudData(object):

   import re
import string 

class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word
        
        self.s=input_string
        self.words_to_counts = {}
        
        sentence_enders = r"\:.|!|\?"
        sentences = re.split(sentence_enders, input_string)
        while '' in sentences: sentences.remove('')
        freq = {}
        for sentence in sentences:
            words = re.split(r"[^a-zA-Z0-9'-]+", sentence)
            for word in words:
                count = freq.get(word, 0)
                freq[word] = count + 1
        print(freq)
        def is_cap(word):
            ch = word[0:1]
            return ch in string.ascii_uppercase
        di={}
        l=['','-']
        for word, count in freq.items():
            # print("hello")
            if word in l:
                pass
            elif is_cap(word) and word.lower() in freq:
                count = freq[word]
                freq[word.lower()] += count
                if freq[word.lower()] in di:
                    self.words_to_counts[word.lower()]+=1
                else:
                    self.words_to_counts[word.lower()]=1
            else :
                self.words_to_counts[word]=freq[word]
        # print("di : ",self.words_to_counts)


















# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)