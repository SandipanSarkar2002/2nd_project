# This is a perfect guess game where the user have to guess the perfect number

from random import randint
n=randint(1,100)

guesses=[] #taking an empty list to store the guesses

while True:
    a=int(input("Guess the number between 1 to 100 : "))
    if(1<=a<=100):
        guesses.append(a) #a=attempts taken
        if(a>n):
            print("Lower number please !")
        elif(a<n):
            print("Higher number please !")
        elif(a==n):
            print(f"You guessed the number {n} right in {len(guesses)} guesses !")
            break
    else:
        print("Enter a Valid number !")
