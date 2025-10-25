#Python Program to Compute all the Permutation of the String

from itertools import permutations

String=input("Enter a string:")
permutations_list=permutations(String)

print("All possible permutations are:")

for p in permutations_list:
    print("".join(p))