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
