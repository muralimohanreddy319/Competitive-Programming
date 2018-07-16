import unittest


def find_duplicate(int_list):

    # Find a number that appears more than once ... in O(n) time
    if(len(int_list)==0 or len(int_list)==1):
        raise Exception("invalid input")
    
    slow = int_list[0]
    fast = int_list[int_list[0]]
    while(slow!=fast):
        # print slow
        # print fast
        slow = int_list[slow]
        fast = int_list[int_list[fast]]
    fast = 0
    while(slow!=fast):
        # print slow 
        # print fast
        slow = int_list[slow]
        fast = int_list[fast]
    return fast



















# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2,3,2,5,4])
        expected = 2
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)