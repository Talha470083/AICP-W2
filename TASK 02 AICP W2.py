
print("------------------Task2----------------------")

names = [0] * people
amount = [0] * people
i = 0
while i < people:
    print("Enter the name of the person:")
    names[i] = input()
    print(f"Enter the amount paid by {names[i]}:")
    amount[i] = int(input())
    i += 1

i = 0
while i < people:
    print(f"{names[i]}  {amount[i]}")
    i += 1
