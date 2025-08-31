justice_league = ['Wonder Woman', 'Superman', 'batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']

position = justice_league.index("Superman")
order = justice_league.pop(position)
justice_league.insert(3,order)

print(f"Seperating Flash and Aquaman due to their conflict and the new Justice League is {justice_league}")