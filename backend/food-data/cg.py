import csv
import pandas as pd
import os
import re

food_nutrient = pd.read_csv("foundation-foods/food_nutrient.csv", usecols=["fdc_id", "nutrient_id", "amount"])
nutrient = pd.read_csv("foundation-foods/nutrient.csv", usecols=['id', 'name', 'unit_name'])
foods = pd.read_csv("foundation-foods/food.csv", usecols=["fdc_id", "description", "data_type", "food_category_id"])
food_categories = pd.read_csv("foundation-foods/food_category.csv")
food_categories.pop('code')

# print(foods.head().to_string(index=False))
# print()
# print(food_categories.head().to_string(index=False))
# print()


merged_df = pd.merge(
    foods,
    food_categories,
    how="left",
    left_on="food_category_id",   # foreign key column in foods
    right_on="id"            # primary key column in categories
)

merged_df.pop('id')

merged_df = merged_df[merged_df["data_type"] == "foundation_food"]
merged_df.pop('data_type')
merged_df.pop('food_category_id')

# print(merged_df.head().to_string(index=False))

# print()

# print(food_nutrient.head().to_string(index=False))

# print()

# print(nutrient.head().to_string(index=False))

merged_df2 = pd.merge(
    merged_df,
    food_nutrient,
    how="left",
    left_on="fdc_id",   # foreign key column in foods
    right_on="fdc_id"            # primary key column in categories
)

# print()

# print(merged_df2.head().to_string(index=False))

merged_df3 = pd.merge(
    merged_df2,
    nutrient,
    how="left",
    left_on="nutrient_id",   # foreign key column in foods
    right_on="id"            # primary key column in categories
)

# print()

merged_df3 = merged_df3[merged_df3["id"].isin([2047, 1003, 1004, 1258, 1005, 1079, 2000])]

merged_df3 = merged_df3.rename(columns={'name' : 'nutrient','description_x' : 'name', 'description_y' : 'category'})
merged_df3.pop('id')
merged_df3.pop('nutrient_id')

stop_words = ["with", "not", "fluid", "and", "for", "broiler", "or", "fryers"]

# print(merged_df3.head().to_string(index=False))
# print()

# merged_df3["name"] = merged_df3["name"].str.split().str[0 : 3]

# merged_df3["name"] = merged_df3["name"].apply(lambda x: " ".join(x) if isinstance(x, list) else x)
# merged_df3["name"] = merged_df3["name"].apply(lambda x: x[:-1] if x[len(x) - 1] == "," else x)
# merged_df3["name"] = merged_df3["name"].str.split()
# merged_df3["name"] = merged_df3["name"].apply(lambda x: )

def standardize_food_name(long_name):
    if isinstance(long_name, str):
        important_words = []
        words = re.split(r'[, ]+', long_name.lower()) # Split by comma and space
        stop_words = ["with","not", "fluid", "for", "milkfat", "vitamin", "broiler", "broilers", "or", "fryers", "without", "added", "with", "for", "prepared", "drained", "solids", "and"] # Add more as needed

        for word in words:
            if word not in stop_words and len(word) > 2 and word[0] is not "(": # Filter out short and stop words
                important_words.append(word.capitalize()) # Capitalize for consistency

        return " ".join(important_words)
    else:
        return long_name # Return as is if not a string

# Assuming your DataFrame is named 'merged_df3'
merged_df3["name"] = merged_df3["name"].apply(standardize_food_name)

merged_df3["name"] = merged_df3["name"].str.split().str[0 : 3]

merged_df3["name"] = merged_df3["name"].apply(lambda x: " ".join(x) if isinstance(x, list) else x)

# Print the original and standardized names for comparison
pd.set_option('display.max_rows', 100)

# Now print the head
print(merged_df3.head(100))

print()

pivot_df = pd.pivot_table(merged_df3,
                           index=['fdc_id', 'name', 'category'],
                           columns='nutrient',
                           values='amount').reset_index()

# Reset the index to make 'food' a regular column if needed
pivot_df = pivot_df.reset_index()


print(pivot_df.head().to_string(columns=pivot_df.columns))


pivot_df.to_csv("incercare-foods.csv")



