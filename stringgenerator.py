from random import randint

def random_string(wordlen):
    letters = 'abcdefghijklmnopqrstuvwxyz '
    word = ''
    for i in range(0, wordlen):
        letter_loc = randint(0, (len(letters) -1))
        word += letters[letter_loc]
    return word

def main():
    while True:
        try:
            wordlen = int(input('Length of random string: '))
            break
        except:
            print('Please input a whole number')
    print(random_string(wordlen))


if __name__ == '__main__':
    main()