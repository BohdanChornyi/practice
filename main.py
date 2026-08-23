# main.py

#  Самая важная схема:

#                 изменил файл
#                      ↓
#                   git diff          ← вижу изменения в рабочей папке
#
#                    git add
#                      ↓
#                   git diff          ← пусто
#              git diff --staged      ← изменения здесь
#
#                   git commit
#                      ↓
#          изменения сохранены в истории


name = input("Enter your name: ")

print(f"Hello, {name.title()}!")
print("Welcome to the program")