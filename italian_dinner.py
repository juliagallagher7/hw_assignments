# This code will serve the family italian food

def make_pasta():
    print('Fill pot with water')
    print('Place pasta in water')
    print('Heat tomato sauce on stove')
    print('Place pasta in bowl')
    print('Place sauce on pasta')
    print('Add desired ingredients')
    pasta = 'yummy pasta'

def make_pizza():
    print('Flour surface')
    print('Stretch out dough')
    print('PLace dough on surface')
    print('Cover in tomato sauce')
    print('Cover in cheese')
    pizza = 'delicious pizza'

def make_jeremys_pizza(ingredients):
    make_pizza()
    pizza = 'Jeremys {} pizza'.format(ingredients)
    return pizza

def make_jessies_pizza(ingredients):
    make_pizza()
    pizza = 'Jessies {} pizza'.format(ingredients)
    return pizza

def make_johns_pizza(*ingredients):
    make_pizza()
    pizza = 'Johns pizza with {} ingredients' .format(len(ingredients))

# Make pizza and pasta for the family
print(make_pasta)
print(make_jeremys_pizza('pepperoni'))
print(make_jessies_pizza('veggie'))
print(make_johns_pizza('pepperoni', 'sausage', 'peppers'))
