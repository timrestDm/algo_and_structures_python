#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

import string

first_letter = input("Введите первую букву: ")
second_letter = input("Введите вторую букву: ")

first_number = ord(first_letter) - 96
second_number = ord(second_letter) - 96

print(f"Буква {first_letter} находится на {first_number} позиции, буква {second_letter} на {second_number}. "
      f"Между ними {abs(first_number - second_number)  - 1} букв.")
