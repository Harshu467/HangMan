import random
from hangman_life import lives 
from hangman_guessing import guess_list
from hangman_life import game_name
word = random.choice(guess_list).lower()
letters = len(word)
game_over = False
tries = 6
print(game_name)
Result = []
for _  in range(letters):
    Result+= '_'
while not game_over:
    user_guess = input("Guess a letter : ")
    if user_guess in Result:
        print("Letter you have guessed is ", user_guess)
    for position in range(letters):
        letter = word[position]
        if letter == user_guess:
            Result[position] = letter
    if user_guess not in word:
        print("You guessed ", user_guess,".This is not in word , You lose try again.")
        tries-=1
        if tries==0:
            game_over = True
            print("Game Over. You lose . Try Again .")
    print(f"{' '.join(Result)}")
    
    if '_' not in Result:
        game_over = True
        print("Congratulation, You win.")
    print(lives[tries])
