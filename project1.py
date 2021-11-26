myString=input("enter a string:")
characterCount=0
wordCount=1
for i in myString :
    characterCount=characterCount+1
    if(i==' '):
        wordCount=wordCount+1
print("Number of Word in myString: ")
print(wordCount)
print("Number of character in my string:")
print(characterCount)

