# Zadanie 1

shooping = {
    "bakery": ["bread", "buns", "doughnut"],
    "greengrocer": ["carrots", "celery", "rocket"],
}


for shop, items in shooping.items():
    print(
        f"I'm going to the {shop.capitalize()} and buy there {', '.join(item.capitalize() for item in items).split()}."
    )
print(f"I buy {sum(len(items) for items in shooping.values())} products in total.")


print("\n")


# Zadanie 2


divisible_by_5 = [number for number in range(101) if number % 5 == 0]

print("Numbers from 0 to 100 divisible by 5:")
print(divisible_by_5)

numbers_to_power_of_3 = [number**3 for number in divisible_by_5]

print("\nThe same numbers raised to the power of 3:")
print(numbers_to_power_of_3)