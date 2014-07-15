'''
@author: nealx
'''

class WordDict(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.wordSet = set()
        self.trie = Trie()

        pass
    def addWord(self, word):
        if word not in self.wordSet:
            self.wordSet.add(word)
            self.trie.insert(word)
    
    def addWords(self, words):
        for word in words:
            self.addWord(word)
            
    def findSuggestion(self, word):
        if word in self.wordSet:
            return word
        opened = []
        
        opened.append(SearchNode(self.trie.rootNode, 0))
        length = len(word)
        while opened:
            sn = opened[0]
            
            index = sn.count
            node = sn.trieNode
            if sn.count == length:
                # might be an answer
                if node.isKey:
                    return node.content
                
            else:
                #continue search
                nextLetter = word[index]
                if nextLetter.upper() in node:
                    # move forward to next trie node and next letter
                    candidate = SearchNode(node[nextLetter.upper()], index + 1)
                    if candidate not in opened:
                        opened.append(candidate)
                        
                if nextLetter.lower() in node:
                    # move forward to next trie node and next letter
                    candidate = (SearchNode(node[nextLetter.lower()], index + 1))
                    if candidate not in opened:
                        opened.append(candidate)
                if index + 1 < length and word[index] == word[index + 1]:
                    # move to next letter, remain at current trie node
                    candidate = (SearchNode(node, index + 1))
                    if candidate not in opened:
                        opened.append(candidate)
                    
                if nextLetter.lower() in 'aeiou':
                    for vowel in 'aeiouAEIOU':
                        if vowel in node:
                            # move forward to next trie node and next letter
                            candidate = (SearchNode(node[vowel], index + 1))
                            if candidate not in opened:
                                opened.append(candidate)
            # if-else end
            opened.remove(sn)
        # while end
        return "NO SUGGESTION"
                            
    
class Trie:
    def __init__(self):
        self.rootNode = TrieNode("")
        self.size = 0
        #self.
        
    def insert(self, word):
        node = self.rootNode
        key = ""
        for letter in word:
            key += letter
            if letter in node.subNodes:
                node = node[letter]
            else:
                node[letter] = TrieNode(key) 
                node = node[letter]
                  
        node.isKey = True        
        self.size += 1
    
    def __repr__(self):
        return "Trie<size={}>\n{}".format(self.size, self.rootNode.__str__(0)) 
    
        
class TrieNode:
    def __init__(self, content, isKey=False):
        self.isKey = isKey
        self.content = content
        self.subNodes = {}
    
    def __getitem__(self, letter):
        return self.subNodes[letter]
    
    def __setitem__(self, letter, node):
        self.subNodes[letter] = node
    
    def __contains__(self, item):
        return item in self.subNodes
    
    def __repr__(self):
        return 'TrieNode<\'{}\', {}>'.format(self.content, self.subNodes.keys())
    
    def __str__(self, level=0):
        ret = ''
        indent = ' ' * level
        if self.isKey:
            ret += '{}  {}  {}'.format(indent, self.content, '\n')
        else:
            ret += '{} ({}) {}'.format(indent, self.content, '\n')

        for key, value in self.subNodes.iteritems():
            ret += '{}-{}:{}'.format(indent + ' ', key , value.__str__(level + 1))
        return ret    
     
class SearchNode:
    def __init__(self, tNode, matchCount):
        self.trieNode = tNode
        self.count = matchCount # count of matched letters in word so far
        
    def __eq__(self, other):
        return isinstance(other, SearchNode) and self.trieNode == other.trieNode and self.count == other.count
    def __ne__(self, other):
        return not self.__eq__(other)