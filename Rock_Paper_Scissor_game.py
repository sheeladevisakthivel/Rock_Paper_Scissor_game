import random

def getting_choice():
    player_choice = input("enter your choice(rock,paper,scissors): ")
    option = ['rock','paper','scissor']
    computer_choice = random.choice(option)
    choice = {'player': player_choice,'computer': computer_choice}
    return choice
def check_win(player,computer):
    print(f"you chose {player} , computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == 'rock':
        if computer == 'scissor':
            return 'Rock smashes scissor! You win'
        else:
            return 'Paper covers rock! You lose!'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers rock! You win'
        else:
            return 'Sciccors cut paper! You lose!'
    elif player == 'scissor':
        if computer == 'paper':
            return 'Scissor cuts paper! You win'
        else:
            return 'Rock smashes scissors! You lose!'

choice = getting_choice()
result = check_win(choice['player'],choice['computer'])
print (result)