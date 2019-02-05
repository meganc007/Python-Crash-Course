cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#since checking for equality is case sensitive, convert the value using lower() beforehand to check the value