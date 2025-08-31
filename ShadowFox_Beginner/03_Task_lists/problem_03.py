justice_league = ['Superman', 'batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']

place = justice_league.index("Wonder Woman")
leader = justice_league.pop(place)
ranking = justice_league.insert(0,leader)

print(f"The order of justice_league after new Leader is assigned: {justice_league}")