import unittest


def find_rotation_point(words):

    # Find the rotation point in the list
    i = BinarySearch(words,0,len(words)-1)
    
    return i
def BinarySearch(words,low,high):
    while(high>low+1):
        print high 
        print low
        if(words[low]>words[high]):
            mid = (low+high)//2
            if(words[mid]>words[high]):
                low = mid
            else:
                high = mid
        else:
            return low
    print words[low]
    print words[high]
    if words[low] <= words[high]:
        return low
    else:
        return high

# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)