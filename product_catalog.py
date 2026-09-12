from product_data import products

# Print the first few products to see how the data is organized
print(products[:3])

customer_preferences = []
response = ""

# Ask the customer for their preferences
while response != "N":
    preference = input("Input a preference:\n").strip().lower()

    if preference:
        customer_preferences.append(preference)

    response = input(
        "Do you want to add another preference? (Y/N): "
    ).strip().upper()

# Remove duplicate preferences
customer_preferences = set(customer_preferences)

# Convert each product's tags into a set
converted_products = []

for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }
    converted_products.append(converted_product)


# Count how many tags match
def count_matches(product_tags, customer_tags):
    matching_tags = product_tags.intersection(customer_tags)
    return len(matching_tags)


# Find and sort the recommended products
def recommend_products(products, customer_tags):
    recommendations = []

    for product in products:
        match_count = count_matches(
            product["tags"],
            customer_tags
        )

        if match_count > 0:
            recommendations.append({
                "name": product["name"],
                "matches": match_count
            })

    recommendations.sort(
        key=lambda item: item["matches"],
        reverse=True
    )

    return recommendations


# Run the recommendation function
recommended_products = recommend_products(
    converted_products,
    customer_preferences
)

# Print the results
print("\nRecommended Products:")

if len(recommended_products) == 0:
    print("No matching products found.")
else:
    for product in recommended_products:
        print(
            f'- {product["name"]} '
            f'({product["matches"]} match(es))'
        )