import random
print("RANDOM RECIPE GENERATOR")
proteins = ["chicken", "beef", "tofu", "fish", "eggs"]
veggies = ["broccoli", "carrots", "spinach", "bell peppers", "mushrooms"]
carbs = ["rice", "pasta", "potatoes", "quinoa", "bread"]
methods = ["baked", "grilled", "stir-fried", "roasted", "sautéed"]
flavors = ["garlic", "lemon", "spicy", "herb", "sweet & sour"]


while True:
    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flavor = random.choice(flavors)

    print(
        f"Your random recipe: {protein} {method} {carb} with {flavor} and {veggie} ")

    value = input("Generate another receipe? (y/n): ")

    if value.lower() == 'n':
        print("goodbye")
        break
