alien_color = 'green'
# alien_color = 'yellow'
# alien_color = 'red'
# alien_color = 'purple'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
else:
    points = 0

print("You earned " + str(points) + " points!")