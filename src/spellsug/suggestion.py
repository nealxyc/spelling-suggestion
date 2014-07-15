'''
Created on Jul 15, 2014
@author: nealx
'''
import read_words
from word_dict import WordDict

if __name__ == '__main__':
    if read_words.readWords():
        wd = WordDict()
        wd.addWords(read_words.words)
        #print "Built dictionary with size={}".format(wd.trie.size)
        #print wd.trie
        # repl
        word = str(raw_input('> '))
        while word:
            #print word
            #print 'size=' + str(len(word))
            #print type(word)
            print wd.findSuggestion(word)
            word = str(raw_input('> '))
        
        
                
                
            
        
            