# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
word = input("Enter a word: ")
times = int(input("How many times would you like that word repeated? "))
print(word * times)

#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name = input("Enter your name: ")
age = int(input("Enter your age: "))
next_year_age = age + 1
print("To the human named " + name + "! You are " + str(age) + " years old. Next year, you will be " + str(next_year_age) + " years old.")

#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence = input("Enter a sentence: ")
w2f = input("Enter a word to find in the sentence-->: ")
print(w2f in sentence)

# Prompt the user for a word, a first index, and a last index
word = input("Enter a word: ")
first_index = int(input("Enter the starting index: "))
last_index = int(input("Enter the ending index: "))

# Slice the word at the indexes provided by the user and print to the screen
sliced_word = word[first_index:last_index]
print("Sliced word: " + sliced_word)

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
print("Cavin", "Patrick", "Krenik", sep="|")
