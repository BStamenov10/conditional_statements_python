trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())


total_sum = (puzzles_count * 2.60) + (dolls_count * 3) + (teddy_bears_count * 4.10) + (minions_count * 8.2) +\
      (trucks_count * 2)
total_count_toys = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count

if total_count_toys >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum = total_sum - (total_sum * 0.1)


diff = abs(trip_price - total_sum)
if trip_price <= total_sum:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")








