#taking a sentence and storing each word in a list and displaying the smallest word

sent=input("Enter a sentence: ")
brk=sent.strip(" ")
x=len (brk[0])
wrd=""
for i in range (len (brk)):
    if len(brk[i])<x:
         x=len (brk[i])
         wrd=brk[i]
print("The smallest word is: ",wrd)