squares = []
for value in range(1,11):
    #square = value**2
    #squares.append(square)

    squares.append(value**2)

print(squares)

#list comprehension combines the for loop and the
# creation of new elements into one line and automatically appends each new element
squares2 = [value**2 for value in range(1,11)]
print(squares2)