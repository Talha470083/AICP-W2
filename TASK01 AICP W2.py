print("------------------Task1----------------------")
print("Enter the number of senior citizens who want to go on a trip:")
people = int(input())
if people > 36 or people < 10:
    raise ValueError("Number of people should be between 10 to 36")
if 10 <= people <= 16:
    cost = (people + 2) * 150 * 14 * 21
    print(f"The total cost for this trip is {cost}")
    print(f"The cost per person for this trip is {cost/people}")
    people += 2
elif 17 <= people <= 23:
    cost = (people + 2) * 190 * 13.50 * 20.00
    print(f"The total cost for this trip is {cost}")
    print(f"The cost per person for this trip is {cost/people}")
    people += 2
elif 24 <= people <= 26:
    cost = (people + 3) * 190 * 13.50 * 20.00
    print(f"The total cost for this trip is {cost}")
    print(f"The cost per person for this trip is {cost/people}")
    people += 3
elif 27 <= people <= 36:
    cost = (people + 3) * 225 * 13 * 19
    print(f"The total cost for this trip is {cost}")
    print(f"The cost per person for this trip is {cost/people}")
    people += 3
















