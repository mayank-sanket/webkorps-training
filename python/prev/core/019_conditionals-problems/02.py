


age = int(input("Enter age: "))
day = input("enter day: ").lower()

price = 12 if age >=18 else 8

if day == "wednesday":
    price -= 2

print(f"Ticket price is ${price}")