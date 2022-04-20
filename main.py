#-----------------------------#-----------------------------#

  # import and global variables

from itertools import permutations

dict = {}
permMaster = []
word_lengths = []
prune_lens = []
prune_letters = []
cryptogram = ''
candidates2 = []
next_candidates_count = 0
counter = 0
lists = []
count = 0

#-----------------------------#-----------------------------#

  # read in the input and create the data contents needed to decode

with open('input.txt') as file:   
  contents = file.read()
  cryptogram = contents
  scrambled_word_list = contents.split(' ')
  num_of_words = len(scrambled_word_list)
  
  for word in scrambled_word_list:
    word_lengths.append(len(word))
    if len(word) not in prune_lens:
      prune_lens.append(len(word))

  for letter in cryptogram:
    if letter not in prune_letters:
      prune_letters.append(letter)
  

#-----------------------------#-----------------------------#

  # open dictionary.txt and convert to python dictionary. This is to enable O(1) permutation lookup
  with open('dictionary.txt') as file: 
    
    candidate_list_master = []
    contents = file.read()
    for i in scrambled_word_list:
      for j in contents.split('\n'): 
        if len(i) == len(j):
          if j not in candidate_list_master:
            candidate_list_master.append(j)

    
    
#-----------------------------#-----------------------------#

  # Defining functions

def isRepeated(word_list):
  candidates = {}
  print(word_list)
  for word in word_list:
    for letter in word:
      if letter in candidates.keys():
        candidates[letter].append([word_list.index(word),word.index(letter)])
      else:
        candidates[letter] = [[word_list.index(word),word.index(letter)]]
      
  return candidates

candidates = isRepeated(scrambled_word_list)


def hashWord(word):
  known_letters = []
  hash_val = 0
  out_going_hash = []
  string = ''
  
  for letter in word:
    if letter not in known_letters:
      known_letters.append(letter)
      hash_val += 1
      out_going_hash.append(str(hash_val))
    else:
      out_going_hash.append(str(known_letters.index(letter) + 1))
  return string.join(out_going_hash)




scrambled_hash = []

for word in scrambled_word_list:
  scrambled_hash.append(hashWord(word))

candidate_hash_dict = {}
candidate_hash_list = []


for word in candidate_list_master:
  hashed_word = hashWord(word)
  if hashed_word not in candidate_hash_dict.keys():
    candidate_hash_dict[hashed_word] = [word]
  else:
    candidate_hash_dict[hashed_word].append(word)


for scram in scrambled_hash:
  if scram in scrambled_hash:
    print(candidate_hash_dict[scram])
