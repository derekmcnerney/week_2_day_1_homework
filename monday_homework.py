#Homework 1
num_1 = int(input("First number:"))
num_2 = int(input("Second number:"))

print("{} + {} = ".format(num_1, num_2))
print(num_1 + num_2)

print("{} - {} = ".format(num_1, num_2))
print(num_1 - num_2)

print("{} * {} = ".format(num_1, num_2))
print(num_1 * num_2)

print("{} / {} = ".format(num_1, num_2))
print(num_1 / num_2)

while True:
    while True:
        answer = str(input("Run again? (y/n): "))
        if answer in ("y", "n"):
            break
        print("invalid input.")
    if answer == "y":
        continue
    else:
        print("Goodbye")
        break

#Home work 2

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("X ", end="")
    print("\n")


eye = {
    "derek" :
        "first_name": "Derek",
        "last_name": "Mcnerney",
        "eye_color": "Blue"

    "lucas": {
        "first_name": "Lucas",
        "last_name": "Lang",
        "eye_color": "Hazel"
    }
    "racheal":{
        "first_name": "Rachael",
        "last_name": "Something",
        "eye_color": "Blue"
    }

for i in information.items():
    print(i[1]["eye"])

a_list = [23, 3, 94, 43, 2]

sorted(a_list)