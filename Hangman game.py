print("WELCOME TO THE HANGMAN GAME")
print("------------------------")
l1=["cat","dog","horse","tiger","lion"]
l2=["---","---","-----","-----","----"]
n=2
pt=0
len=len(l1[n])
print("Hint : the word is of ",len," letters")
for i in l2[n]:
    Ltem=[]
    Ltem=l2[n].append()
for j in l2[n]:
    en=input("Enter the letter you guessed:")
    if en in l1[n]:
        x=