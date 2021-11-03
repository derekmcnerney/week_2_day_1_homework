def area (length, width):
    return length * width
    
length = int(input("What is the length of the room in feet? "))
width = int(input("What is the width of the room in feet? "))
result = length * width
print("You entered dimensions of " + str(length) + str(" feet by ") + str(width) +str(" feet."))
print(result)