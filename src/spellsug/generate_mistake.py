'''
Created on Jul 15, 2014

@author: NXIONG
'''
import read_words

def generateMistakes(word):
    ret = []
    length = len(word)
    half = length / 2
    ret.append(word) 
    ret.append(word[0:half].lower() + word[half:length].upper()) # half lower half upper
    repeat = ''
    swapVowel = ''
    vowels = set(['a','e','i','o','u'])
    for letter in word:
        repeat += 3 * letter ## repeat every letter 3 times
        if letter.lower() in vowels:
            swapVowel += (vowels - set(letter)).pop() # change to any different vowel from the set
        else:
            swapVowel += letter
        
    ret.append(repeat)
    ret.append(swapVowel)
    return ret

if __name__ == '__main__':
    if read_words.readWords():
        for word in read_words.words:
            for wrong in generateMistakes(word):
                print wrong
    # terminates repl loop           
    print '\n'
        