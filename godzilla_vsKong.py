budget = float(input())
statist_count = int(input())
clothes_price_one = float(input())

decor = budget * 0.1

if statist_count > 150:
    clothes_price_one -= clothes_price_one * 0.1

all_clothes = clothes_price_one * statist_count

diff = abs((decor + all_clothes) - budget)

if (decor + all_clothes) > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
