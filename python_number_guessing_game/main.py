import random
import time

def play_game(input_list,guess_number):
    
    number_of_attempt = 1
    user_points = 100
    result_dic = dict()

    while number_of_attempt <= 5:

        print("Attempt Number :-", number_of_attempt)
        time.sleep(1)

        user_input = int(input("Guess and integer between 0 to 9 :- "))
        time.sleep(1)

        if user_input not in input_list:
            result_dic['message'] = "Please guess the number between 0 to 9."
            break            

        elif user_input == guess_number:
            result_dic['message'] = "Congrats!!! You guessed the correct number"
            result_dic['actual_number'] = guess_number
            result_dic['points'] = user_points
            result_dic['number_of_attempts'] = number_of_attempt
            break

        elif user_input > guess_number:
            print("Oops!! You guessed the wrong number. Try guessing a lesser number")
            user_points-=20
            number_of_attempt+=1

        elif user_input < guess_number:
            print("Oops!! You guessed the wrong number. Try guessing a greater number")
            user_points-=20
            number_of_attempt+=1

        else:
            print("Oops!!! You guessed the wrong number. Try again!!!")
            user_points-=20
            number_of_attempt+=1
    else:
        result_dic['message'] = "Sorry Buddy!! Number of attempts Exceeded. Better Luck Next Time"
        result_dic['actual_number'] = guess_number
        result_dic['points'] = user_points

    return result_dic

print("Welcome User!!! Let's Start The Game")
time.sleep(1)

input_list = list(range(10))
guess_number = random.choice(input_list)

game_result = play_game(input_list,guess_number)
print(game_result)
