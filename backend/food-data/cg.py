import csv
import pandas as pd
import os
import re
import numpy as np

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

merged_df3 = merged_df3[merged_df3["id"].isin([2047, 1003, 1004, 1258, 1005, 1079, 2000, 1149])]

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
        stop_words = ["Commercially", "with","not", "fluid", "for", "milkfat", "vitamin", "broiler", "broilers", "or", "fryers", "without", "added", "with", "for", "prepared", "drained", "solids", "and"] # Add more as needed

        if "Restaurant" not in words:
            for word in words:
                if word not in stop_words and len(word) > 2 and word[0] is not "(" and not word.endswith(")"): # Filter out short and stop words
                    important_words.append(word.capitalize()) # Capitalize for consistency
        else:
            important_words = words

        return " ".join(important_words)
    else:
        return long_name # Return as is if not a string
    

def change_category_name(category_name):
    switch = {
        "Legumes and Legume Products" : 9,
        "Dairy and Egg Products" : 6,
        "Vegetables and Vegetable Products" : 8,
        "Sausages and Luncheon Meats" : 4,
        "Nut and Seed Products" : 10,
        "Soups, Sauces, and Gravies" : 18,
        "Baked Products" : 11,
        "Spices and Herbs" : 18, 
        "Fats and Oils" : 3,
        "Poultry Products" : 4,
        "Finfish and Shellfish Products" : 5,
        "Sweets" : 13,
        "Beef Products" : 4,
        "Pork Products" : 4,
        "Cereal Grains and Pasta" : 2,
        "Beverages" : 7,
        "Lamb, Veal, and Game Products" : 4
    }
    return switch.get(category_name, 19)



# Assuming your DataFrame is named 'merged_df3'
merged_df3["name"] = merged_df3["name"].apply(standardize_food_name)

merged_df3["name"] = merged_df3["name"].apply(lambda x: " ".join(x.split()[0:3]) if "Restaurant" not in x else x)


#merged_df3["name"] = merged_df3["name"].apply(lambda x: " ".join(x) if isinstance(x, list) else x)

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
# pivot_df = pivot_df.reset_index()

#pivot_df.pop('nutrient')

cols_to_rename = {'fdc_id' : 'id','category' : 'category_id', 'Carbohydrate, by difference' : 'carbs_100g', 'Total lipid (fat)' : 'fats_100g', 'Fatty acids, total saturated' : 'saturated_fats_100g', 'Protein' : 'protein_100g', 'Total Sugars' : 'sugar_100g', 'Fiber, total dietary' : 'fibre_100g', 'Energy (Atwater General Factors)' : 'calories_100g', 'Total Sugars' : 'sugar_100g'}
pivot_df.rename(columns=cols_to_rename, inplace=True)

print(pivot_df.head().to_string(index=False))

pivot_df['category_id'] = pivot_df['category_id'].apply(lambda x: change_category_name(x))

pivot_df.insert(2, "brand", "USDA FoodData")
pivot_df.insert(11, "salt_100g", 0.0)
pivot_df = pivot_df.fillna(0)


print()



print(pivot_df.head().to_string(index=False))



pivot_df.to_csv("incercare-foods.csv")



# 0            Legumes and Legume Products          ->      Legumes
# 1                 Dairy and Egg Products          ->      Dairy & Egg 
# 2      Vegetables and Vegetable Products          ->      Vegetables
# 8            Sausages and Luncheon Meats          ->      Meat
# 9                  Nut and Seed Products          ->      Nuts & Seeds
# 15            Soups, Sauces, and Gravies          ->      
# 22               Fruits and Fruit Juices          ->      Fruits & Juices 
# 26                        Baked Products          ->      Baked Goods 
# 31                      Spices and Herbs          ->      Other
# 48                         Fats and Oils          ->      Fats & Oils 
# 49                      Poultry Products
# 59        Finfish and Shellfish Products          ->      Fish
# 62                                Sweets          ->      Sweets
# 63                      Restaurant Foods          ->      Restaurant Foods
# 67                         Beef Products          ->      Meat
# 119                        Pork Products          ->      Meat
# 150              Cereal Grains and Pasta          ->      Cereal & Pasta 
# 177                            Beverages          ->      
# 390        Lamb, Veal, and Game Products          ->      Meat

# 1	Fruits & Juices
# 2	Cereal & Pasta
# 3	Fats & Oils
# 4	Meat
# 5	Fish
# 6	Dairy & Egg
# 7	Plant-Based Drinks
# 8	Vegetables
# 9	Legumes
# 10	Nuts and Seed
# 11	Baked Goods
# 12	Snacks
# 13	Sweets
# 14	Restaurant Foods
# 15	Fast Foods
# 16	Alcoholic Beverages
# 17	Other