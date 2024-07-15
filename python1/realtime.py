
import random

start = int(input("enter the starting value of the range: "))
end= int(input("enter the ending value of the range: "))

while start >= end:
    print("starting value must be less than ending value, please enter the values correctly")
    start = int(input("enter the starting value of the range: "))
    end= int(input("enter the ending value of the range: "))

generaterandom = random.randint(start,end)

print(f"guess the number between {start} and {end}.you ave 3 tries left")

attempts = 3

while attempts > 0:
    guess = int(input("enter your guess: "))
    attempts -=1

    if guess < generaterandom:
        print(f"your guessed value is less than generated value.{attempts} tries left")
    elif guess > generaterandom:
        print(f"your guessed value is more than generated value.{attempts} tries left")
    else:
        print("congratulations! your guessed number is correct")
        break

else:
    print(f"sorry,you have ran out of your attempts,the genarated value is:")


