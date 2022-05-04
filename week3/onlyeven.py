number = input("Please enter a positive number: ")

while (number.isdigit() == False) or int(number) <= 0:
    number = input("Invalid input. Please enter a positive number: ")

def only_evens():
    for x in range(0, int(number) + 1, 2):
        print(x)
only_evens()