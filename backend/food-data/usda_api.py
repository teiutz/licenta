import requests
import json
import pandas as pd

api_key = "OzXbiXucatRzcaa1KYUQIh2suvFJq6x2PSPZFCby"
base_url = "https://api.nal.usda.gov/fdc/v1"
endpoint = "/foods/search"

food_items = [
    "Apple Granny Smith raw",
    "Apricot raw",
    "Quince raw",
    "Avocado raw all commercial",
    "Banana Raw",
    "blackberries raw -wild",
    "blueberry Raw",
    "cherry Raw",
    "coconut Raw",
    "date Raw",
    "fig Raw",
    "grape muscadine Raw",
    "grapefruit Raw",
    "Kumquats Raw",
    "lemon juice Raw",
    "lime juice Raw",
    "mangos Raw",
    "Melons, cantaloupe, raw",
    "Nectarines raw",
    "Oranges raw all commercial values",
    "Papayas Raw",
    "passion fruit granadilla raw",
    "peach Raw",
    "pears raw",
    "pineapple raw all varieties",
    "plums raw",
    "raspberries raw",
    "strawberries raw -guavas",
    "oat bran raw",
    "Cereals, oats, regular and quick, not fortified, dry",
    "oat flour",
    "Wheat, durum",
    "Wheat flour, white, all-purpose, unenriched",
    "Wheat flour, white, all-purpose, self-rising, enriched",
    "wheat sprouted -bread",
    "wheat bran crude",
    "Rice, white, long-grain, regular, raw, unenriched",
    "Rice, white, long-grain, regular, unenriched, cooked without salt",
    "Cornmeal, degermed, unenriched, yellow",
    "Corn flour, whole-grain, yellow",
    "Barley flour or meal",
    "Barley, pearled, raw",
    "Barley, pearled, cooked",
    "Rye flour, dark",
    "Millet flour",
    "Quinoa, uncooked",
    "Quinoa cooked -ancient",
    "Buckwheat groats, roasted, dry",
    "Buckwheat groats, roasted, cooked",
    "Buckwheat flour, whole-groat",
    "Pasta, dry, unenriched",
    "Pasta, cooked, unenriched, with added salt",
    "Pasta, cooked, unenriched, without added salt",
    "Pasta, homemade, made with egg, cooked",
    "\"Butter salted”",
    "”Butter, without salt” -seeds",
    "”Oil, coconut”",
    "Oil, olive, salad or cooking",
    "Oil, sunflower, high oleic (70% and over)",
    "Oil, sesame, salad or cooking",
    "Oil, avocado",
    "Chicken, broilers or fryers, breast, meat and skin, raw",
    "Chicken, broiler or fryers, breast, skinless, boneless, meat only, raw -solution",
    "chicken breast grilled -solution",
    "Chicken, broilers or fryers, breast, meat and skin, cooked, roasted",
    "Chicken, broilers or fryers, thigh, meat and skin, raw",
    "Chicken, broilers or fryers, dark meat, thigh, meat only, raw",
    "Chicken, broilers or fryers, thigh, meat and skin, cooked, roasted",
    "Chicken, broilers or fryers, thigh, meat only, cooked, roasted",
    "Chicken, broilers or fryers, thigh, meat only, cooked, fried",
    "Chicken, broilers or fryers, wing, meat and skin, raw",
    "Chicken, broilers or fryers, wing, meat and skin, cooked, roasted",
    "Chicken, broilers or fryers, wing, meat and skin, cooked, fried, batter",
    "Chicken, broilers or fryers, drumstick, meat and skin, raw",
    "Chicken, broilers or fryers, drumstick, meat and skin, cooked, roasted",
    "Chicken, ground, raw",
    "Chicken, ground, crumbles, cooked, pan-browned",
    "Chicken, liver, all classes, raw",
    "Chicken, liver, all classes, cooked, simmered",
    "Chicken, liver, all classes, cooked, pan-fried",
    "Pork, fresh, loin, center loin (chops), bone-in, separable lean and fat, raw",
    "Pork, fresh, loin, center loin (chops), bone-in, separable lean only, raw",
    "Pork, fresh, loin, top loin (chops), boneless, separable lean and fat, raw -solution",
    "Pork, fresh, loin, center loin (chops), bone-in, separable lean and fat, cooked, broiled",
    "Pork, fresh, loin, center loin (chops), bone-in, separable lean only, cooked, broiled",
    "Pork, fresh, blade, (chops), boneless, separable lean and fat, cooked, broiled",
    "Pork, fresh, loin, blade (chops or roasts), boneless, separable lean and fat only, raw",
    "Pork, fresh, loin, blade (chops), bone-in, separable lean and fat, cooked, broiled",
    "Pork, fresh, loin, blade (chops or roasts), bone-in, separable lean and fat, raw",
    "Pork, fresh, loin, center rib (chops), bone-in, separable lean and fat, cooked, broiled",
    "Pork, fresh, loin, blade (chops), boneless, separable lean only, boneless, cooked, broiled",
    "Pork, fresh, loin, sirloin (chops), boneless, separable lean and fat, cooked, braised",
    "Turkey, whole, breast, meat only, raw -solution",
    "Turkey, all classes, breast, meat and skin, raw",
    "Turkey, whole, breast, meat only, cooked, roasted",
    "Turkey, all classes, breast, meat and skin, cooked, roasted",
    "Turkey, Ground, raw -fat",
    "Turkey, Ground, cooked",
    "Turkey, retail parts, thigh, meat and skin, raw",
    "Turkey, retail parts, thigh, meat only, raw",
    "Turkey, retail parts, thigh, meat and skin, cooked, roasted",
    "Turkey, retail parts, thigh, meat only, cooked, roasted",
    "Lamb, New Zealand, imported, loin chop, separable lean and fat, raw",
    "Lamb, New Zealand, imported, loin chop, separable lean and fat, cooked, fast fried",
    "Lamb, New Zealand, imported, loin chop, separable lean only, raw",
    "Lamb, New Zealand, imported, loin chop, separable lean only, cooked, fast fried",
    "Beef, grass-fed, ground, raw",
    "Beef, ground, unspecified fat content, cooked",
    "Beef, grass-fed, strip steaks, lean only, raw",
    "Veal, sirloin, separable lean and fat, cooked, roasted",
    "Ribeye",
    "Ground Beef",
    "Ham, smoked, extra lean, low sodium",
    "Ham, turkey, sliced, extra lean, prepackaged or deli",
    "Pork, cured, bacon, unprepared",
    "Pork, cured, bacon, cooked, baked",
    "Pork, cured, bacon, pre-sliced, cooked, pan-fried",
    "Frankfurter, chicken",
    "Frankfurter, pork",
    "Frankfurter, turkey",
    "Fish, cod, Pacific, cooked -dry",
    "Fish, cod, Atlantic, raw",
    "Fish, pollock, Alaska, raw -may",
    "Fish, pollock, Alaska, cooked -may",
    "Fish, bass, striped, raw",
    "Fish, bass, freshwater, mixed species, cooked, dry heat",
    "Fish, salmon, pink, raw",
    "Fish, salmon, pink, cooked, dry heat",
    "Fish, salmon, chinook, smoked -alaska -lox",
    "Fish, tuna, fresh, bluefin, raw",
    "Fish, tuna, fresh, bluefin, cooked, dry heat",
    "Fish, tuna, white, canned in oil, drained solids -salt",
    "Fish, tuna, light, canned in water, drained solids  -salt",
    "Fish, trout, mixed species, raw",
    "Fish, trout, mixed species, cooked, dry heat",
    "Crustaceans, shrimp, raw -mixed",
    "Crustaceans, shrimp, cooked -mixed",
    "Mollusks, mussel, blue, raw",
    "Mollusks, mussel, blue, cooked, moist heat",
    "Mollusks, octopus, common, raw",
    "Mollusks, octopus, common, cooked, moist heat",
    "Mollusks, squid, mixed species, raw",
    "Mollusks, squid, mixed species, cooked, fried",
    "Milk, reduced fat, fluid, 2% milkfat, without added vitamin A and vitamin D",
    "Milk, fluid, 1% fat, without added vitamin A and vitamin D",
    "Milk, canned, condensed, sweetened",
    "Sour cream, imitation, cultured",
    "Yogurt, Greek, plain, nonfat -chobani",
    "Yogurt, plain, whole milk -greek",
    "Cheese, mozzarella, whole milk -low",
    "Cheese, ricotta, whole milk",
    "Cheese, feta",
    "Cheese, cream -spread -cottage -fat -ready",
    "Cheese, cream, low fat",
    "Cheese, parmesan, grated -fat",
    "Cheese, camembert",
    "Cheese, brie",
    "Cheese, cheddar, sharp, sliced",
    "Gorgonzola",
    "Egg, whole, raw, fresh -duck -goose -quail -turkey",
    "Egg, whole, cooked, hard-boiled",
    "Egg, whole, cooked, poached",
    "Egg, whole, cooked, fried",
    "Egg, white, raw, fresh",
    "Egg, yolk, raw, fresh",
    "Tofu, fried -calcium",
    "Tofu, raw, regular, prepared with calcium sulfate",
    "Tempeh -cooked",
    "tempeh cooked",
    "Beverages, almond milk, unsweetened, shelf stable -fortified",
    "Beverages, coconut milk, sweetened, fortified with calcium, vitamins A, B12, D2",
    "Beverages, rice milk, unsweetened",
    "artichokes raw globe",
    "Asparagus, raw",
    "asparagus cooked -salt",
    "beet raw -greens",
    "pak choi raw",
    "broccoli raw -chinese -leaves -raab -stalks -flower",
    "broccoli cooked -raab -chinese -frozen without salt",
    "brussel sprout raw",
    "brussel sprout cooked without salt -frozen",
    "Squash, winter, butternut, raw",
    "butternut squash cooked without salt baked",
    "cabbage raw -savoy -red -chinese -common",
    "cabbage cooked -chinese -red -savoy -napa -common",
    "Carrots, raw -baby",
    "carrots cooked -peas without salt -frozen",
    "cauliflower raw -green",
    "cauliflower cooked -green without salt -frozen",
    "celery raw",
    "chives raw",
    "corn raw sweet yellow",
    "corn yellow cooked without -frozen -grits salt",
    "\"cucumber with peel raw\"",
    "Edamame, frozen, unprepared",
    "Edamame, frozen, prepared",
    "Eggplant, raw",
    "Eggplant, cooked, boiled, drained, without salt",
    "Garlic, raw",
    "mushroom raw white -light",
    "Mushrooms, white, cooked, boiled, drained, without salt",
    "Peppers, sweet, red, raw",
    "Peppers, sweet, yellow, raw",
    "Peppers, sweet, green, raw",
    "Potatoes, white, flesh and skin, raw",
    "Potatoes, white, flesh and skin, baked",
    "sweet potato raw -leaves",
    "sweet potato cooked -leaves without salt -frozen baked",
    "pumpkin raw -flowers -seed -leaves",
    "pumpkin cooked without salt -flowers -leaves",
    "zucchini raw -baby",
    "zucchini cooked -frozen without salt",
    "tomatoes raw red",
    "tomato cooked red -stewed -salt",
    "black beans canned -soup -low",
    "black beans raw -turtle",
    "black beans cooked without salt -turtle",
    "white  beans raw -small",
    "white  beans canned",
    "white beans cooked without salt -small",
    "navy beans raw -sprouted",
    "navy beans canned",
    "chickpeas canned drained -tap",
    "chickpea raw",
    "chickpea cooked without salt",
    "kidney beans raw red -california -royal",
    "kidney beans red canned drained -tap",
    "kidney beans red cooked without salt -california -royal",
    "green peas raw -mature",
    "green peas canned -soup drained -baby -salt",
    "green peas cooked without salt -frozen",
    "green peas cooked without salt frozen",
    "red lentils raw",
    "Lentils, mature seeds, cooked, boiled, without salt",
    "Green Lentils",
    "almonds oil roasted  salt added -smoke -without",
    "\"Nuts, almonds, oil roasted, without salt added\"",
    "almond nuts -oil -butter -paste -blanched -honey -dry",
    "brazil nuts",
    "cashews raw",
    "cashews roasted with salt -without -oil",
    "Nuts, hazelnuts or filberts, dry roasted, without salt added",
    "Nuts, hazelnuts or filberts",
    "Nuts, macadamia nuts, raw",
    "Nuts, macadamia nuts, dry roasted, with salt added -without",
    "Nuts, macadamia nuts, dry roasted, without salt added",
    "Nuts, pistachio nuts, raw",
    "pistachio roasted -planters -without",
    "pistachio roasted without salt -planters",
    "pine nuts -pinyon",
    "sesame seeds dried -kernels",
    "Seeds, chia seeds, dried",
    "pumpkin seed roasted with salt -without -kernels",
    "poppy seed",
    "sunflower seed roasted -without dry -shell",
    "bread white wheat -enriched -schar",
    "whole wheat bread commercially -toasted -refrigerated -frozen",
    "sourdough bread -toasted",
    "rye bread -toasted -calorie",
    "Focaccia, Italian flatbread, plain",
    "pita bread unenriched",
    "croissant butter",
    "tortilla wheat -fry",
    "potato chip plain salted -soybean",
    "tortilla chips salted yellow",
    "pretzels hard salted unenriched",
    "Snacks, popcorn, oil-popped, white popcorn, salt added",
    "marshmallow candies -fudge",
    "chocolate chip cookie commercially regular unenriched",
    "vanilla ice cream -light -rich -fat -sugar -french -low",
    "chocolate ice cream -light -rich -soft -fat -bar -regular -sugar -nuts",
    "strawberry ice cream -light -rich -soft -fat -bar -regular -sugar -nuts",
    "jam -apricot -sweetened -sugar",
    "Chocolate-flavored hazelnut spread",
    "Beverages, carbonated, cola, regular",
    "apple juice -babyfood -canned -light -blend -with without added ascorbic -3",
    "Beverages, Orange juice drink -canned -pineapple -pulp",
    "Beverages, tea, black, ready-to-drink, lemon, sweetened",
    "catsup -low",
    "mustard -greens -oil -seed yellow",
    "mayonnaise regular -salt",
    "hot sauce sriracha -tuong -cha",
    "soy sauce tamari",
    "pesto classico"
]

# Define your search parameters
# params = {
#     "api_key": api_key,
#     "query": "strawberries raw -guavas",  
#     "pageSize": 1,   
#     "dataType": ["SR Legacy"],
#     "pageNumber": 1    
# }

df = pd.DataFrame(columns=['id', 'name', 'category', 'calories_100g', 'carbs_100g', 'fats_100g', 'saturated_fats_100g', 'protein_100g', 'fibre_100g', 'sugar_100g','salt_100g'])

fdc_ids = []
descriptions = []
categories = []
cals = []
carbs = []
fats = []
sat_fats = []
proteins = []
fibre = []
sugar = []
salt = []

pt_semafor = {
    0 : cals,
    1 : fats,
    2 : sat_fats,
    3 : carbs,
    4 : proteins,
    5 : sugar,
    6 : fibre,
    7 : salt
}

for food_name in food_items:
    api_query = food_name

    # Define the parameters for the API request
    params = {
        "query": api_query,
        "api_key": api_key,
        "dataType": ["SR Legacy"],
        "pageSize": 1 
    }

    print(f"....Searching for: {food_name} .....")

    try:
        response = requests.get(base_url + endpoint, params=params)
        response.raise_for_status() 

        data = response.json()

        # print(data.keys())

        # with open('test-json2.json', 'x') as f:
        #     json_object = json.dumps(data, indent=4)
        #     f.write(json_object)
        #     f.close()
        # break
        # print(data['foods'])

        if data and data.get('foods'):
            
            for food in data["foods"]:
                fdc_ids.append(food["fdcId"])
                descriptions.append(food["description"])
                categories.append(food["foodCategory"])

                semafor = [0,0,0,0,0,0,0,0]

                for nutrient in food["foodNutrients"]:
                    if nutrient["nutrientId"] == 1008:
                        semafor[0] = 1
                        cals.append(nutrient["value"])

                    elif nutrient["nutrientId"] == 1004:
                        semafor[1] = 1
                        fats.append(nutrient["value"])

                    elif nutrient["nutrientId"] == 1258:
                        semafor[2] = 1
                        sat_fats.append(nutrient["value"])
                        # print(nutrient["value"])

                    elif nutrient["nutrientId"] == 1005:
                        semafor[3] = 1
                        carbs.append(nutrient["value"])

                    elif nutrient["nutrientId"] == 1003:
                        semafor[4] = 1
                        proteins.append(nutrient["value"])

                    elif nutrient["nutrientId"] == 2000:
                        semafor[5] = 1
                        sugar.append(nutrient["value"])

                    elif nutrient["nutrientId"] == 1079:
                        semafor[6] = 1
                        fibre.append(nutrient["value"])

                    elif nutrient["nutrientId"] == 1093:
                        semafor[7] = 1
                        salt.append(nutrient["value"] * 2.54 / 1000)
                        
                for i in range(0, 8):
                    if semafor[i] == 0:
                        nutrient = pt_semafor[i]
                        nutrient.append(0.0)
        else:
            print(f"  No results found for '{food_name}'.")

    except requests.exceptions.RequestException as e:
        print(f"  Error searching for '{food_name}': {e}")
    except json.JSONDecodeError:
        print(f"  Error decoding JSON response for '{food_name}'.")

df['id'] = fdc_ids
df['name'] = descriptions
df['category'] = categories
df['calories_100g'] = cals
df['carbs_100g'] = carbs
df['fats_100g'] = fats
df['saturated_fats_100g'] = sat_fats
df['protein_100g'] = proteins
df['fibre_100g'] = fibre
df['sugar_100g'] = sugar
df['salt_100g'] = salt

print(df.head())



df.to_csv('victorie.csv', index=False)


# try:
#     response = requests.get(base_url + endpoint, params=params)
#     with open('test-json.json', 'x') as f:
#         json_object = json.dumps(response.json(), indent=4)
#         f.write(json_object)
#         f.close()


#     print(base_url + endpoint)
#     response.raise_for_status()  
#     data = response.json()
    

# except requests.exceptions.RequestException as e:
#     print(f"Error during API request: {e}")
# except ValueError as e:
#     print(f"Error decoding JSON: {e}")

# for food in food_items:


# - Fruit:
#     Pre-Packaged Fruit & Vegetables
