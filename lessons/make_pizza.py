"""Practice instantiating pizza class"""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)
sals_pizza: Pizza = Pizza("small", 2, False)

# def price(pizza_order: Pizza) -> float:
#     """Calculate and return cost of pizza."""
#     cost: float = 0.0
#     if pizza_order.size == "large":
#         cost = 6.0
#     else:
#         cost = 5.0
#     # charge .75 per topping
#     cost += .75 * pizza_order.toppings
#     if pizza_order.gluten_free == True:
#         cost += 1.0
#     return cost

print(my_pizza.price)
