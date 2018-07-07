import unittest


def get_permutations(string):

    # Generate all permutations of the input string
    
    set1=set()
    print permute("",list(string),set1)




def permute(prefix,s,set1):
    n=len(s)
    if(n==0):
        set1.add(prefix)
    else:
        for i in range(n):
            permute(prefix+s[i],s[0:i]+s[i+1:n],set1)
    return set1












# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abcd')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)