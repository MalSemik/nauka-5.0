my_number = -1
while my_number < 0 or my_number > 100:
    my_number = int(input("Wybierz liczbe od 0 do 100: "))

start = 0
end = 100
computer_guess = (start + end) // 2

while computer_guess != my_number:
    if computer_guess < my_number:
        start = computer_guess
    else:
        end = computer_guess
    computer_guess = (start + end) // 2

print("Wygralem, twoja liczba to: ", computer_guess)
input()
