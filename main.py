import random
import json
import datetime


def play_game():
    secretNumber = random.randint(1, 30)
    attempts = 0
    wrong_guesses = []
    score_list = get_score_list()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')

    playerName = input("Enter your name, please: ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secretNumber:
            score_data = {"name": playerName, "number": secretNumber, "attempts": attempts,
                          "listWrongNumbers": wrong_guesses, "date": current_time}
            score_list.append(score_data)

            with open("score_list.txt", "w") as score_file:
                b = json.dumps(score_list)
                score_file.write(b)

            print("You've guessed it - congratulations! It's number " + str(secretNumber))
            print("You've needed " + str(attempts) + " attempts.")
            break
        elif guess > secretNumber:
            print("Your guess is not correct... try something smaller")
        else:
            print("Your guess is not correct... try something bigger")
        wrong_guesses.append(guess)


def get_score_list():  # lista de resultados
    with open("score_list.txt", "r") as score_file:
        a = score_file.read()
        score_list = json.loads(a)

        return score_list


def get_top_scores():  # lista de mejores resultados
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    print("Top 3: ")

    for score_dict in top_score_list:
        print("Player name: " + str(score_dict.get("name"))
              + " / Secret number: " + str(score_dict.get("number"))
              + " / Attempts: " + str(score_dict.get("attempts"))
              + " / Wrong guesses: " + str(score_dict.get("listWrongNumbers"))
              + " / Date: " + str(score_dict.get("date")))
    return top_score_list


while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")
    selection = selection.upper()

    if selection == "A":
        play_game()
    elif selection == "B":
        get_top_scores()
    else:
        break