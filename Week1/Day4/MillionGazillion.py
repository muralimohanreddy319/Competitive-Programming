import unittest

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.EndofWord = False


class Trie(object):

    def __init__(self):
        self.root = self.getNode()
    # Implement a trie and use it to efficiently store strings

    def getNode(self):
        return TrieNode()
    def _chartoindex(self,ch):
        return ord(ch)-ord('a')
    def add_word(self,word):
        
        # print "hello"
        length = len(word)
        # print length
        node = self.root
        # print node
        for level in range(length):
            index=self._chartoindex(word[level])
            # print word[level]
            # print node.children[index]
            if(node.children[index]==None):
                node.children[index]=self.getNode()
            node = node.children[index]
        if(node.EndofWord==True):
            return False
        else:
            node.EndofWord = True
            return True


# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)