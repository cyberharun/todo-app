try:
    width=float(input("Enter rectangle width: "))
    length=float(input("Enter rectangle length: "))

    if width==length:
        exit("That looks like a square.") #red color output, use print for white

    area=length*width

    print(area)
except ValueError:
    print("Please enter a number.")
