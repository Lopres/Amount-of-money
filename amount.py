Amount_money = int(input("How much money do you have?"))
The_price_of_apple = int(input("the price of apple?"))
maximum_apples = int(Amount_money / The_price_of_apple)
Remaining_money = int(Amount_money - (maximum_apples * The_price_of_apple))
print(f"You can buy {maximum_apples} apples and your change is {Remaining_money} pesos. ")