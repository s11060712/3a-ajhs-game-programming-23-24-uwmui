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

i = 0
while i < len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i += 1