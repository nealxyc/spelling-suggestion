'''
@author: nealx
'''
from src.spellsug.wordDict import WordDict
from src.spellsug.wordDict import SearchNode


if __name__ == '__main__':
    wd = WordDict()
    wd.addWord("sheep")
    wd.addWord("shap")
    wd.addWord("job")
    wd.addWord("inside")
    wd.addWord("can")
    wd.addWord("cAt")
    wd.addWord("wake")
    wd.addWord("conspiracy")
    
    print wd.findSuggestion("SHEEP")
    print wd.findSuggestion("Sheeple")
    print wd.findSuggestion("inSIDE")
    print wd.findSuggestion("jjoobbb")
    print wd.findSuggestion("cat")
    print wd.findSuggestion("weeke")
    print wd.findSuggestion("CUNsperrICY")
    