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
num_of_results = 0
results = []

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

  for word in candidate_list_master:
    hashed_word = hashWord(word)
    if hashed_word not in candidate_hash_dict.keys():
      candidate_hash_dict[hashed_word] = [word]
    else:
      candidate_hash_dict[hashed_word].append(word)

  return candidate_hash_dict


def backtrack(master_list,a_list,k,scrambled_hash):
  
  k = k+1
  n_candidates = len(candidate_hash_dict[scrambled_hash[k]])
  
  for i in range(n_candidates): 
    perm = [candidate_hash_dict[scrambled_hash[k]][i]]
    a_list.append(perm)
    if k < len(scrambled_hash)-1:
      backtrack(master_list,perm,k,scrambled_hash)
        
  return a_list





candidate_hash_dict = build_candidates()
crypto_hash = hashWord(cryptogram)


len_cryptogram = len(cryptogram)

p_rick = backtrack(perms,[],-1,scrambled_hash)

#print(p_rick[0])
#print(p_rick[0][0])
#print(p_rick[0][1][0])
#print(p_rick[0][1][1][0])

#for p in p_rick: # root node
  
  #for i in p[1:-1]: 

    #for j in i[1:-1]:
    
      #str_2_hash = p[0] + ' ' + i[0] + ' ' + j[0]
      #hashed_perm = hashWord(str_2_hash)
    
    #if hashed_perm[0:len_cryptogram] == crypto_hash[0:len_cryptogram]:
      #print(str_2_hash)


def print_results(num_of_results):
  print(num_of_results)
  print(results)
  for res in results:
    print(res[0])


# 1 word
def search_4_1(p_rick):
  num_of_results = 0
  for p in p_rick:
      str_2_hash = p[0]
      hashed_perm = hashWord(str_2_hash)
      if hashed_perm[0:len_cryptogram] == crypto_hash[0:len_cryptogram]:
        results.append([str_2_hash])
        num_of_results += 1
  return num_of_results    

# 2 word
def search_4_2(p_rick):
  num_of_results = 0
  for p in p_rick:
    for i in p[1:-1]:
      str_2_hash = p[0] + ' ' + i[0]
      hashed_perm = hashWord(str_2_hash)
      if hashed_perm[0:len_cryptogram] == crypto_hash[0:len_cryptogram]:
        results.append([str_2_hash])
        num_of_results += 1
  return num_of_results    
  
# 3 word
  
def search_4_3(p_rick):
  num_of_results = 0
  for p in p_rick:
    for i in p[1:-1]:
      for j in i[1:-1]:  
        str_2_hash = p[0] + ' ' + i[0] + ' ' + j[0]
        #print(str_2_hash)
        hashed_perm = hashWord(str_2_hash)
        #print(hashed_perm)
        if hashed_perm[0:len_cryptogram] == crypto_hash[0:len_cryptogram]:
         # print(hashed_perm)
          results.append([str_2_hash])
          num_of_results += 1
  return num_of_results 

# 4 word
def search_4_4(p_rick):
  num_of_results = 0
  for p in p_rick:
    for i in p[1:-1]:
      for j in i[1:-1]: 
        
        for k in j[1:-1]:  
          str_2_hash = p[0] + ' ' + i[0] + ' ' + j[0]
          #print(str_2_hash)
          hashed_perm = hashWord(str_2_hash)
          #print(hashed_perm)
          if hashed_perm[0:len_cryptogram] == crypto_hash[0:len_cryptogram]:
         # print(hashed_perm)
            results.append([str_2_hash])
            num_of_results += 1
  return num_of_results 


# 5 word
# 5 word

# 6 word

# 7 word

# 8 word
      
# 9 word

# 10 word

# 11 word

# 12 word

# 8 word

res = search_4_4(p_rick)
print_results(res)