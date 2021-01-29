import random


def intro():
    print(':+'*50)
    print("""                                Welcome to Guess The Word""")
    print(':+'*50)
# Splitting the letters in a word


def split(word):
    return [char for char in word]


def get_new_word(w_list):
    # takes a random word in a list and word_guess is that random word.
    r_num = random.randrange(len(w_list))
    word_guess = w_list[r_num]
    word_guess_list = split(word_guess)
    return word_guess_list


wordlist = ['cat', 'dog', 'apple', 'program',
            'python', 'lawyer', 'anaconda', 'starter', 'water']
intro()
done = False
i_guess = 0
c_guess = 0
gameOver = False
while not done:
    new_word = get_new_word(wordlist)
    blanks = []
    for i in range(len(new_word)):
        blanks.append(' _ ')
    u_say = input("Would you like to play again? Yes or No: ").lower()
    if u_say == 'yes':
        i_guess = 0
        c_guess = 0
        gameOver = False
    elif u_say == 'no':
        done = True
    while not gameOver:
        if i_guess == 7:
            print("GAME OVER! ;(")
            gameOver = True
        elif c_guess == len(blanks):
            print(':+'*50)
            print("CONGRATZ! $$$$$$$$$$$$$$$$$")
            print(':+'*50)
            print(blanks)
            gameOver = True
        else:
            print(blanks)
            u_guess = input("Type a letter you want to guess?: ").lower()
            not_in = True
            for i in new_word:
                if u_guess == i and blanks[new_word.index(i)] == ' _ ':
                    blanks[new_word.index(i)] = u_guess
                    c_guess += 1
                else:
                    not_in = False
            if not_in:
                i_guess += 1
                print(f'Nope, try again you have {i_guess}/7.')

            # for i in range(0, len(new_word)):
            #     if u_guess == new_word[i] and blanks[i] == ' _ ':
            #         blanks[i] = u_guess
            #         c_guess += 1
            #         print('Nice!')
            #     elif u_guess != new_word[i]:
            #         i_guess += 1
            #         print(f'Nope, try again you have {i_guess}/7.')
            #         break


# new_word = get_new_word(wordlist)
# blanks = []
# for i in range(len(new_word)):
#     blanks.append(' _ ')
#     print(new_word)
#     if c_guess == len(blanks):
#         user_input = input('Play again? (Y)es (N)o: ').lower()
#         if user_input == 'yes':
#             i_guess = 0
#             c_guess = 0
#             new_word = []
#             blanks = []
#         if user_input == 'no':
#             done = True
#         elif i_guess == 7:
#             print("Game Over!")
#             user_input = input('Play again? (Y)es (N)o: ').lower()
#         if user_input == 'yes':
#             i_guess = 0
#             c_guess = 0
#             new_word = []
#             blanks = []
#         if user_input == 'no':
#             done = True
