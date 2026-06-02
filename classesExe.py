class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"The Name of the restaurant is :{self.restaurant_name}")
        print(f"The type of cuisine which is offered here is :{self.cuisine_type}")
    def open_restaurant(self):
        print(f"The Restaurant '{self.restaurant_name}' is OPEN !")

my_restaurant=Restaurant('Hansh Regency','North Indian')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
