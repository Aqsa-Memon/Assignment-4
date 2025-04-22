
def print_multiple(message: str, repeats: int): 
    for i in range(repeats):
        print(message)


def main(): 
    message = input("Please type a Number: ")
    repeats = int(input("Enter a number of times to repeat your Number: ")) 
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
