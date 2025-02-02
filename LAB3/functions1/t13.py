def cheack(like,name,sum):
    
    if like < 19:
        print("Your guess number is too low\nTake a guess")
        return True
    elif like > 19:
        print("Your guess number is too high\nTake a guess")
        return True
    else:
        print(f"Good job, {name}! You guessed my number in {sum} guesses!")
        return False
print("Hello! What is your name?")
name=input()
print(f"Well, {name}, I am thinking of number between 1 and 20.\nTake a guess.")

sum = 0
b = True
while b:
    num=int(input())
    sum+=1
    b = cheack(num,name,sum)

