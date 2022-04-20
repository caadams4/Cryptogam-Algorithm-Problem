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
cnt = 0
scrambled_hash = []
perms = []
y = {}

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


def build_candidates():

  

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

  '''
  for scram in scrambled_hash:
    if scram in scrambled_hash:
      print(candidate_hash_dict[scram])
     ''' 
  
  return candidate_hash_dict


# a_list is the dictionary 

# k is where in the diction







  

candidate_hash_dict = build_candidates()
crypto_hash = hashWord(cryptogram)

print(crypto_hash)

def construct_candidates(a_list,k,crypto_hash,c,n_candidates1):
  #print(crypto_hash[k])
  #print(candidate_hash_dict[crypto_hash[k]])
  
    



  
  return

def isSolution(a_list,k,crypto_hash):
  

  return

def processSolution(a_list,k,crypto_hash):

  return







# pass in for in next
              # for next 



# define backtrack

def backtrack(master_list,a_list,k,scrambled_hash):

  
  if (isSolution(a_list,k,scrambled_hash)):
    processSolution(a_list,k,scrambled_hash)
    
  else:
    k = k+1
    
    n_candidates = len(candidate_hash_dict[scrambled_hash[k]])
    
    for i in range(n_candidates): 
    
      perm = []
      perm.append(candidate_hash_dict[scrambled_hash[k]][i])
      a_list.append(perm)
      #rint(candidate_hash_dict[scrambled_hash[k]][i])
      #print(k)
      '''
        for j in range(len(candidate_hash_dict[scrambled_hash[k+1]])):
          next_poss = candidate_hash_dict[scrambled_hash[k+1]][j]
          print(new_poss, next_poss)
          a_list.append([new_poss, next_poss])
      '''  
      
      if k < len(scrambled_hash)-1:
        backtrack(master_list,perm,k,scrambled_hash)
        
  return a_list

      
  
p_rick = backtrack(perms,[],-1,scrambled_hash)
print(p_rick[100])

print(crypto_hash)
print(perms)