class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._mydict = {}


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        # word len as key
        for v in dict:
            self._mydict.setdefault(len(v), []).append(v)


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        key = len(word)
        result = False
        # search all same len result
        if key in self._mydict:
            for v in self._mydict[key]:
                count = 0
                for w1, w2  in zip(word, v):
                    if w1 == w2:
                        continue
                    else:
                        count += 1
                if count == 1:
                    return True
                    break

        return False




# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
