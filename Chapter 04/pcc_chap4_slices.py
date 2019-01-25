animals = ['parrot', 'monitor lizard', 'capybara']

for animal in animals:
    print("I like " + animal.title()+ "s.")
print("These would certainly be interesting pets.")

animals.append('fox')
animals.append('axolotl')
animals.append('venezuelan potoo')
animals.append('czechoslovakian vlcak')

print("The first three items in the list are:")
print(animals[:3])

print("Three items from the middle of the list are:")
print(animals[3:6])

print("The last three items in the list are:")
print(animals[-3:])