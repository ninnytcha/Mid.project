# 2.3. თამაში 2: Hangman

import random

def choose_word():
    # სია, საიდანაც პროგრამა შემთხვევით ირჩევს სიტყვას
    words = ["პითონი", "კომპიუტერი", "თამაში", "სათამაშო", "სწავლა", "პროგრამა", "ჰანგმენი", "ცოდნა"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # აჩვენებს სიტყვის ასოებს ქვედა ტირეებით ან გამოცნობილ ასოებს
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts_left = 10  # მოთამაშეს აქვს 10 მცდელობა
    guessed = False

    print("გამარჯობა! ეს არის Hangman-ის თამაში.")
    print(f"სიტყვა შეიცავს {len(word)} ასოს.")
    print("გთხოვთ, შეიყვანეთ მხოლოდ ერთი ქართული ასო.")

    while not guessed and attempts_left > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"მცდელობები დარჩა: {attempts_left}")

        guess = input("გამოიცანი ასო: ").strip().lower()


        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("ეს ასო უკვე გამოცნობილი გაქვს.")
            elif guess not in word:
                print("ასო არ არის სიტყვაში.")
                attempts_left -= 1
            else:
                print("სწორი პასუხია!" )
                guessed_letters.add(guess)
        else:
            print("კიდევ სცადეთ")

        # ვამოწმებთ, გამოიცნო თუ არა მოთამაშემ მთელი სიტყვა
        if all(letter in guessed_letters for letter in word):
            guessed = True
        else:
            print("გთხოვთ, შეიყვანეთ მხოლოდ ერთი ქართული ასო.")

        if guessed:
            print(f"\nგილოცავ! შენ გამოიცანი სიტყვა: {word}")

    if attempts_left == 0:
         print (f"\nსამწუხაროდ, დამარცხდი. სიტყვა იყო: {word}")


hangman()