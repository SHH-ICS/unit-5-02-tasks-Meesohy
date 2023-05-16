# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
word= str()
word= input ("Welcome! Enter a word:") 
while word != "quit": 
  print ("Length of word is", len(word), "letters long")
  word= input("Enter another word:")
print ("Goodbye! See you!") 
