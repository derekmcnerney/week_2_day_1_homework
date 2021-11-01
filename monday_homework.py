
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
