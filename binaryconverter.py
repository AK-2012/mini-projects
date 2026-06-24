def main():
    # main function running the console stuff and helpers
    print("This program will convert a number between 0 and 255 to binary. ")
    number = intput("Enter a number between 0 and 255 inclusive: ")
    binary = convert(number)
    print(f"{number} in binary: {binary}")


def intput(prompt):
    # helper function to get input between 0 and 255
    while True:
        try:
            number = int(input(prompt))
            if number > 255 or number < 0:
                raise ValueError
            return number
        except ValueError:
            print("Enter a valid number. ")

  
def convert(number):
    # helper function converting to binary
    chars = []
    for i in range(7, -1, -1):
        if number - 2**i >= 0:
            chars.append(1)
            number -= 2**i
        else:
            chars.append(0)
    return "".join(str(char) for char in chars)

  
if __name__ == "__main__":
    main()
