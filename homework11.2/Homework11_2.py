import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0

nome = input("Your Name?") 

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    #print("Top scores: " + str(score_list)) #This print will show the top scores in one row

for score_dict in score_list:
   print("Name: " + score_dict.get("Name")  + ", " + str(score_dict["attempts"]) + " attempts, " + "secret number was: " + str(score_dict["secret_number"]) +
    " " + "date: " + score_dict.get("date") + " " + str(score_dict.get("wrong_guesses")))

    
    


wrong_guesses = [] # To create a list with the wrong guess

while True:
   
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"Name": nome, "attempts": attempts, "date": str(datetime.datetime.now()), "secret_number": secret, "wrong_guesses": wrong_guesses })
        
        
        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
       

    elif guess < secret:
        print("Your guess is not correct... try something bigger")
    
    wrong_guesses.append(guess) # Add the guesses in the list
       