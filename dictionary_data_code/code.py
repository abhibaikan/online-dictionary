import json

data=json.load(open('data.json'))

i='y'

def loc(word):
    word = word.lower()
    if word in data:
      return data[word]
    else:
        return "no word found or the word is incorrectw"

while i == 'y':
    
    word = input ('enter word: ')
    print(loc(word))
    
    i = input('do you wish to cont. y/n: ')

    if i=='y':
     continue
    elif i=='n':
      break

        
