import random
wordList = 'Fortune Temperance Justice Magician Judgement Devil Death Jester Aeon World Star Sun Moon Hermit Hierophant Chariot Priestess Emperor Empress Lovers Strength'.split()
# .split() will split a string into seperate elements, by default based on SPACE

# VARIABLE_NAMES that are ALL CAPS are CONSTANTS not meant to change.
HANGMAN_BOARD = ['''
    +----+
          |
          |     
          |       
          |       
         ====''', ''' 
    +----+
    0     |
          |     
          |       
          |       
         ====''', ''' 
    +----+
    0     |
    |     |     
          |       
          |       
         ====''', '''
    +----+
    0     |
   /|     |     
          |       
          |       
         ====''', '''
    +----+
    0     |
   /|\    |     
          |       
          |       
         ====''', ''' 
    +----+
    0     |
   /|\    |     
   /      |       
          |       
         ====''', '''     
    +----+
    0     |
   /|\    |     
   / \    |       
          |       
         ====''']                     

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) -1)
    # len(listName) -1 IS MOST COMMON WAY TO PREVENT INDEX OUT OF RANGE
    # print(wordIndex)
    return wordList[wordIndex]

i = 0
while i < 500000:
     getRandomWord(wordList)
     i += 1