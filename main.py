cars = {
    "honda": 3000,
    "Hyundai": 3000,
    "BMW": 4000,
    "Audi": 4500,
    "Bentley": 100000,
}
# For loop
# Price = (cars.values())
for car in enumerate(cars):
    print(f'{car} ')

name = input("Car's name: ")
quantity = input("Quantity: ")
x = float(cars[name]) * float(quantity)

print(f"{x} $")

pay = input("Do you want to pay? y/n")
if pay == "y":
    print("thanks")
