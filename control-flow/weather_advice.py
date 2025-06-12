current_condition =input(" What's the weather like today? (sunny/rainy/cold): ")
if current_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif current_condition == "rainy":
    print(" Don't forget your umbrella and a raincoat.")
elif current_condition == "cold":
    print(" Make sure to wear a warm coat and a scarf.")
else:
    print(" Sorry, I don't have recommendations for this weather.")