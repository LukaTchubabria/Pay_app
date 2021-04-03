cars = {
    "honda": 3000,
    "hyundai": 3000,
    "bmw": 4000,
    "audi": 4500,
    "bentley": 100000,
}

for num, (name, price) in enumerate(cars.items(), 1):
    print(f'{num}) {name}: {price}$')

carname = input("Car's name: ")
quantity = input("Quantity: ")
x = float(cars[carname.lower()]) * float(quantity)

print(f"{x} $")

pay = input("Do you want to pay? [Yes/No]")

if pay.lower() == "yes":
    print("thanks")
elif pay.lower() == "no":
    print('Ok, stop')
else:
    print('SORRY')