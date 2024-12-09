# 2.1. კალკულატორი

Pirveli_ricxvi = int(input("შეიყვანეთ რიცხვი:     "))
Meore_ricxvi = int(input("შეიყვანეთ მეორე რიცხვი:    "))
Moqmedeba = input("მიუთითეთ ერთ-ერთ შემდეგი მოქმედება: plus, minus, divide, multiply:     ")
Archeuli_moqmedeba = Moqmedeba.lower()

if Archeuli_moqmedeba == "plus":
    print (Pirveli_ricxvi + Meore_ricxvi)
elif Archeuli_moqmedeba == "minus":
    print (Pirveli_ricxvi - Meore_ricxvi)
elif Archeuli_moqmedeba == "divide":
    print (Pirveli_ricxvi / Meore_ricxvi)
elif Archeuli_moqmedeba == "multiply":
    print (Pirveli_ricxvi * Meore_ricxvi)
else:
    print("თქვენს მიერ არჩეული ქმედება არასწორია, კიდევ სცადეთ!")
