pizzas = ['meat lovers', 'bbq chicken', 'stuffed crust cheese']
for pizza in pizzas:
    print("I like " + pizza.title() + " pizza.")

print("It's not my favorite food, but I thoroughly enjoy a good pizza.")

friend_pizzas = pizzas[:]

pizzas.append('apple pie pizza')
friend_pizzas.append('pineapple pizza')

print("My favorite pizzas are:")
print(pizzas)

print("My friend's favorite pizzas are:")
print(friend_pizzas)