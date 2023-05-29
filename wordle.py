import random
with open("wordle1.txt", 'r', encoding='utf-8') as f:
    data = f.read()
    fives = data.split()
play_again = 'yes'
while play_again.lower() == 'yes':

    word = random.choice(fives)
    a = True
    count = 0
    while a:
        i = input("try a word ")
        if len(i) != 5:
            continue
        if i not in fives:
            print(word, "is not in list")
            continue
        if i == word:
            print(word + " is true")
            a = False
        elif i != word and count == 5:
            print(word)
            a = False
        else:
            for j in range(5):
                if i[j] == word[j]:
                    print(i[j]+" green")
                elif i[j] in word:
                    print(i[j] + " yellow")
                else:
                    print(i[j] + " gray")
            count += 1
    play_again = input('Would you like to play again? yes to play again ')
