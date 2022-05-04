applePrice = 0.50

customerName = input("Please enter your name: ")

numOfApples = int(input(f"Hi {customerName}. Apples cost ${applePrice:.2f} each. How many would you like to buy?"))

print(f"Thank you {customerName} for your purchase of {numOfApples} apples at a cost of ${applePrice:.2f} each.")

print(f"Your total is: ${(applePrice * numOfApples):.2f}")