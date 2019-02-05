alien_color = 'green'

if alien_color == 'green':
    points = 5
else:
    points = 10
print("You earned " + str(points) + " points!")

alien_color = 'purple'
if alien_color == 'green':
    points = 5
if alien_color != 'green':
    points = 10
print("You earned " + str(points) + " points!")