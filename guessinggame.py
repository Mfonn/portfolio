import random
#importing it
n = random.randint(1, 99)
#picking a random number from 1-99
x = 5
#creating a variable for my counts
print ("you have only", x , "chances to guess the number")
count = 0
#giving my count variable a value of 0
   
guess = int(input("Enter any number from 1 to 99: "))
#user should input number
while n != "guess":
    print
    if guess < n:
        count += 1
        print ("guess is low")
        print ("You have", 6 - count, "tries left" )
        guess = int(input("Enter an integer from 1 to 99: "))

    elif guess > n:
        count += 1
        print ("guess is high")
        print ("You have", 6 - count, "tries left")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("Congratulations!!!!!!!! you guessed it! in", count, "tries")
        break
    if count == 5:
        print("The number is ", n)
        print("game over!")
        break
    print