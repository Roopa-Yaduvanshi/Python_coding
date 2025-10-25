#Python Program to Count the Number of Each Vowel

#Take input from user
sentence=input("Enter a sentence:")

'''Convert sentence into lowercase to handle capital letter 
So "A" and "a" are treated as same'''
sentence=sentence.lower()

#Initialize counts for each variable
a_count=e_count=i_count=o_count=u_count=0

#loop through each character in the sentence
for char in sentence:
    if char=="a":
        a_count+=1
    elif char=="e":
        e_count+=1
    elif char=="i":
        i_count+=1
    elif char=="o":
        o_count+=1
    elif char=="u":
        u_count+=1
        
        #Print the counts
        print("Vowels Counts:")
        print("a:",a_count)
        print("e:",e_count)
        print("i:",i_count)
        print("o:",o_count)
        print("u:",u_count)