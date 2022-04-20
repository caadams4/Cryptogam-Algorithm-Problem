#-----------------------------#-----------------------------#

  # import and global variables

from itertools import permutations

dict = {}
permMaster = []

#-----------------------------#-----------------------------#

  # open dictionary.txt and convert to python dictionary. This is to enable O(1) permutation lookup

with open('dictionary.txt') as file:   
  contents = file.read()
  for i in contents.split('\n'):               
    dict[i] = i

#-----------------------------#-----------------------------#

  # read in the input and create the data contents needed to decode

with open('input.txt') as file:   
  contents = file.read()
  scrambled_word_list = contents.split(' ')
  num_of_words = len(scrambled_word_list)
  print(scrambled_word_list)

#-----------------------------#-----------------------------#

  # Defining functions

def construct_permutaions(scrambled_word_list):
  
    # Argument -> scrambled_word_list = list of scrambled words read in from input.txt
    # Func Descption:  uses itertools permutations method to create all permutations of each cryptogram
    #                  creates a list (permList) of permutations for each word, stores them in permMaster.              
  for word in scrambled_word_list:
    permList = []
    permutes = permutations(word)
    for perms in permutes:
      scram = ''
      for item in perms:
        scram = scram + item
      permList.append(scram)
    permMaster.append(permList) 
  return 


def findSolution(permutations,k,scrambled_input):
  
    # Argument -> permutations = list of all permutation for each word
    #             k = index of permutations of the scrambled_input word
    #             scrambled_input = scrambled word we're trying to find the dictionary word
    # Func Descption: checks each permutation for a dictioney entry. Discounts the permutation given as
    #                 the scrambled word. 
  
  for word in permutations[k]:
    if (word != scrambled_input):
      try:
        if (dict[word]):
          return word + ' ' + scrambled_input
      except:
        x=1  


def decode( scrambled_word_list ):
  
    # Argument -> scrambled_word_list = list of scrambled words read in from input.txt
    # Func Descption: gets permutations with 'construct_permutaions()' 
                      #searches the dictionary.txt/dict{} to find a match with 'findSolution()'
                      #creates a list of of sorted results with the built in python sorted 'method'
                      #prints the sorted results
  
  results = []
  k = 0
  print(num_of_words)
  construct_permutaions(scrambled_word_list)
  
  for word in range(num_of_words):
    found_word = findSolution(permMaster,k,scrambled_word_list[k])
    k += 1
    results.append(found_word)
  sorted_results = sorted(results)
  
  for res in sorted_results:
    print(res)
  return


#-----------------------------#-----------------------------#

  # decode function call
  
decode( scrambled_word_list )



