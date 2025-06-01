import csv
import pandas as pd
import os

food_nutrient = pd.read_csv("foundation-foods/food_nutrient.csv", usecols=["fdc_id", "nutrient_id", "amount"])
nutrient = pd.read_csv("foundation-foods/nutrient.csv")
foods = pd.read_csv("foundation-foods/food.csv", usecols=["fdc_id", "description", "data_type", "food_category_id"])

# print(list(food_nutrient.columns))
# print(nutrient.head())

df = pd.read_csv("foundation-foods/nutrient.csv", usecols=["id", "name", "unit_name"])
dictt = df.to_dict('dict')

pairs_nut= {}
pairs_unit= {}
for key,value in dictt['id'].items():
    if value == 2047 or value == 1003 or value == 1004 or value == 1258 or value == 1005 or value == 2000 or value == 1079:
        pair = {value : dictt['name'][key]}
        pairs_nut.update(pair)

for key,value in pairs_nut.items():
    print("     " + str(key) + ": " + str(value))

print("/n")

for key,value in dictt['id'].items():
    if value == 2047 or value == 1003 or value == 1004 or value == 1258 or value == 1005 or value == 2000 or value == 1079:
        pair = {value : dictt['unit_name'][key]}
        pairs_unit.update(pair)

print("\n")
for key,value in pairs_unit.items():
    print("     " + str(key) + ": " + str(value))

food_nutrient_ids = food_nutrient["nutrient_id"].to_list()
dc_ids = food_nutrient["fdc_id"].to_list()

print("\n")
print(food_nutrient.head())

print("\n")
df_foods = foods[foods["data_type"] == "foundation_food"]
df_foods.drop('data_type', inplace=True, axis=1)

df_foods2 = df_foods.pop('food_category_id')

fdc_food_pairs = {}

print(df_foods)

print(df_foods2.head())
#print(nutrient_ids)

