

import pandas as pd
import re

df = pd.read_csv('victorie.csv')

name_to_id = {
    "Fruits and Fruit Juices" : 3,
    "Nut and Seed Products" : 9,
    "Cereal Grains and Pasta" : 4,
    "Breakfast Cereals" : 4,
    "Dairy and Egg Products" : 6,
    "Fats and Oils" : 10,
    "Poultry Products" : 7,
    "Pork Products" : 7,
    "Lamb, Veal, and Game Products" : 7,
    "Beef Products" : 7,
    "Sausages and Luncheon Meats" : 7,
    "Finfish and Shellfish Products" : 8,
    "Legumes and Legume Products" : 2,
    "Beverages" : 14,
    "Vegetables and Vegetable Products" : 1,
    "Spices and Herbs" : 11,
    "Baked Products" : 5,
    "Snacks" : 13,
    "Sweets" : 12,
    "Soups, Sauces, and Gravies" : 11
}

import re

def simplify_name(name):
    original = name.lower()

    name = re.sub(r'\([^)]*\)', '', name)

    name = name.lower().strip()
    name = re.sub(r'[\"\']', '', name)
    name = re.sub(r'\s*,\s*', ' ', name)
    name = re.sub(r'\s+', ' ', name)

    filler_words = [
        "broilers", "broiler", "fryer", "fryers", "all", "classes", "retail", "parts", "prepared", "unenriched",
        "not", "added", "made", "includes", "including", "foods", "distribution", "program", 
        "without", "with", "salt", "drained", "solids", "mixed", "species", "flesh", "skin", 
        "sliced", "prepackaged", "commercially", "whole", "year", "round", "average", "extra", 
        "lean", "from", "vitamin", "a", "b12", "d2", "fluid", "sweetened", "unsweetened", 
        "fortified", "stable", "regular", "drink", "usda", "for", "percent", "%", "or", "and"
    ]

    trailing_keywords = ["raw", "uncooked", "cooked", "baked", "boiled", "fried", "grilled", 
                         "roasted", "broiled", "pan-fried", "simmered", "steamed", "moist", "dry", "heat"]

    words = name.split()

    if words[0] != "milk":
        filler_words.append("milk")

    trailing = [w for w in words if w in trailing_keywords]
    cleaned = [w for w in words if w not in filler_words and w not in trailing_keywords]

    meat_keywords = ["chicken", "pork", "beef", "turkey", "veal", "lamb", "duck", "fish"]
    has_meat = any(meat in original for meat in meat_keywords)

    skin_label = None
    if has_meat:
        if "meat and skin" in original:
            skin_label = "with skin"
        elif "meat only" in original:
            skin_label = "skinless"
        
        # Remove "meat", "meat and skin", or "meat only" tokens
        cleaned = [w for w in cleaned if w not in ("meat", "meatonly", "meatandskin")]

    # Rebuild and capitalize
    final = " ".join(word.capitalize() for word in cleaned)

    # Append skin label and cooking info
    parts = [final]
    if skin_label:
        parts.append(skin_label.capitalize())
    if trailing:
        parts.extend([word.capitalize() for word in trailing])

    return ", ".join(parts)


    

df['category'] = df['category'].apply(lambda x: name_to_id[x])
df['name'] = df['name'].apply(lambda x: simplify_name(x))
# df.drop(df.columns[0])


print(df.head(200))

df.to_csv('victorie2.csv', index=False)