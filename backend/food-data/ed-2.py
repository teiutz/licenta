import csv
import pandas as pd
import os

food_nutrient = pd.read_csv("foundation-foods/food_nutrient.csv", usecols=["fdc_id", "nutrient_id"])
nutrient = pd.read_csv("foundation-foods/nutrient.csv")
foods = pd.read_csv("foundation-foods/food.csv", usecols=["fdc_id", "description", "data_type", "food_category_id"])
food_categories = pd.read_csv("foundation-foods/food_category.csv")
food_categories.pop('code')


df_foods = foods[foods["data_type"] == "foundation_food"]
df_foods.drop('data_type', inplace=True, axis=1)

# print(df_foods.head())
# print(food_categories.head())

dic1 = food_categories.to_dict('dict')
dict_food_categories = {}

# print(dic1)
# print("\n")

for key,value in dic1['id'].items():
    pair = {value : dic1['description'][key]}
    dict_food_categories.update(pair)

# print(dict_food_categories)

for key,value in dict_food_categories.items():
    print("     " + str(key) + ": " + str(value))


df = pd.read_csv("foundation-foods/nutrient.csv", usecols=["id", "name", "unit_name"])
dictt = df.to_dict('dict')

print("")

pairs_nut= {}
pairs_unit= {}
for key,value in dictt['id'].items():
    if value == 2047 or value == 1003 or value == 1004 or value == 1258 or value == 1005 or value == 2000 or value == 1079:
        pair = {value : dictt['name'][key]}
        pairs_nut.update(pair)

for key,value in pairs_nut.items():
    print("     " + str(key) + ": " + str(value))

for key,value in dictt['id'].items():
    if value == 2047 or value == 1003 or value == 1004 or value == 1258 or value == 1005 or value == 2000 or value == 1079:
        pair = {value : dictt['unit_name'][key]}
        pairs_unit.update(pair)

print("\n")
for key,value in pairs_unit.items():
    print("     " + str(key) + ": " + str(value))

print("")

print(df_foods.head().to_string(index=False))

#df_foods['food_category'] = df_foods["food_category_id"].apply(lambda x: dict_food_categories[x])

df_foods.loc[:, 'food_category'] = df_foods["food_category_id"].apply(lambda x: dict_food_categories[x])

#dict_food_categories[df_foods['food_category_id']]

df_foods.pop("food_category_id")

print(df_foods.head().to_string(index=False))

