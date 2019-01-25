players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

#show players from the beginning to 5th index
print(players[:5])

#show players from the 2nd index to last index
print(players[2:])

#show last three players
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())