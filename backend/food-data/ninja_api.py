import requests
import pandas as pd


api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
query = '100g carrots and a chicken sandwich'
response = requests.get(api_url + query, headers={'X-Api-Key': 'TFNDowda4Y+TVjiTZCT4ng==uCW8jbkaOnw65xHz'})
if response.status_code == requests.codes.ok:
    print(type(response))
else:
    print("Error:", response.status_code, response.text)

food_names = ["apple"]

for food in food_names:
    response = requests.get(api_url + food, headers={'X-Api-Key': 'TFNDowda4Y+TVjiTZCT4ng==uCW8jbkaOnw65xHz'})

    temp_df = pd.DataFrame(response.json())

try:
        response = requests.get(api_url + food, headers={'X-Api-Key': 'TFNDowda4Y+TVjiTZCT4ng==uCW8jbkaOnw65xHz'})
        response.raise_for_status()  # Raise an exception for bad status codes
        food_data = response.json()
        if food_data and 'items' in food_data:
            # The provided JSON structure has the data directly in 'items'
            items = food_data['items']
            df = pd.DataFrame(items)

            # Process the DataFrame
            if 'cholesterol_mg' in df.columns:
                df = df.drop(columns=['cholesterol_mg'])
            if 'sodium_mg' in df.columns:
                df['salt_g'] = df['sodium_mg'] * 2.5 / 1000
                df = df.drop(columns=['sodium_mg'])

            print(f"Processed data for {food}:\n{df}\n")
            all_food_data.extend(df.to_dict('records')) # Append processed data as dictionaries
        elif isinstance(food_data, list): # Handle if the API returns a list directly
            df = pd.DataFrame(food_data)
            if 'cholesterol_mg' in df.columns:
                df = df.drop(columns=['cholesterol_mg'])
            if 'sodium_mg' in df.columns:
                df['salt_g'] = df['sodium_mg'] * 2.5 / 1000
                df = df.drop(columns=['sodium_mg'])
            print(f"Processed data for {food}:\n{df}\n")
            all_food_data.extend(df.to_dict('records'))
        else:
            print(f"No or unexpected nutritional data found for: {food}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data for {food}: {e}")

if all_food_data:
    final_df = pd.DataFrame(all_food_data)
    print("\nFinal Processed DataFrame:\n", final_df)
else:
    print("No food data was successfully retrieved and processed.")