budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_cards_price = video_cards * 250
processors_price = processors * (video_cards_price * 0.35)
ram_memory_price = ram_memory * (video_cards_price * 0.1)

total_price = video_cards_price + processors_price + ram_memory_price
if processors < video_cards:
    total_price = total_price - (total_price * 0.15)
diff = abs(budget - total_price)
if total_price <= budget:
    print(f"You have {diff:.2f} leva left!")

else:
    print(f"Not enough money! You need {diff:.2f} leva more!")