# 2.2. თამაში 1: გამოიცანით რიცხვი

from random import randint
a = (randint(1, 10))

print (a)
mcdeloba = 0
while True:
    cifri = int(input("დაასახელეთ ციფრი :  "))
    mcdeloba += 1

    if cifri > a:
        print ("დასახელებული ციფრი მეტია ჩაფიქრებულ ციფრზე")

    if cifri < a:
       print ("დასახელებული ციფრი ნაკლებია ჩაფიქრებულ ციფრზე")

    if a == cifri:
        print(f"გილოცავთ თქვენ გამოიცანით ჩაფიქრებული ციფრი! ციფრი შეარჩიეთ {mcdeloba} მცდელობით.")
        break

