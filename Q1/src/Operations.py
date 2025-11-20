from AddfeatureColumn import df, log_dir
import pandas as pd
import os

# Select the columns Name, Year, Fuel_Type, Price
df_select = df[['Name', 'Year', 'Fuel_Type_Diesel', 'Fuel_Type_Petrol', 'Price']]

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had selected the columns Name, Year, Fuel_Type_Diesel, Fuel_Type_Petrol, Price\n")
    f.write("--------------------------------\n")
    f.write(df_select.head().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

# Filter the dataframe where Year is greater than 2015
df_filter = df[df['Year'] > 2015]

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had filtered the dataframe where Year is greater than 2015\n")
    f.write("--------------------------------\n")
    f.write(df_filter.head().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

# Filter the dataframe where Fuel_Type is Diesel and get the head
df_diesel = df[df['Fuel_Type_Diesel'] == 1]

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had filtered the dataframe where Fuel_Type is Diesel\n")
    f.write("--------------------------------\n")
    f.write(df_diesel.head().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

# Rename the columns Kilometers_Driven to KM_Driven, New_Price to NewPrice, Mileage_Clean to Mileage
df_rename = df.rename(columns={
    'Kilometers_Driven': 'KM_Driven',
    'New_Price': 'NewPrice',
    'Mileage_Clean': 'Mileage'
})

df = df_rename

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had renamed the columns Kilometers_Driven to KM_Driven, New_Price to NewPrice, Mileage_Clean to Mileage\n")
    f.write("--------------------------------\n")
    f.write(df.head().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

# Group by Model and get the average Price, Mileage, Power and count of the cars
df_groupby = df.groupby('Model').agg(
    Avg_Price=('Price', 'mean'),
    Avg_Mileage=('Mileage', 'mean'),
    Avg_Power=('Power', 'mean'),
    Count=('Name', 'count')
).reset_index()

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had grouped by Model and got the average Price, Mileage, Power and count of the cars\n")
    f.write("--------------------------------\n")
    f.write(df_groupby.to_string())
    f.write("\n")
    f.write("--------------------------------\n")

# Group by Fuel_Type and get the average Mileage
df_fueltype = df.groupby('Fuel_Type_Diesel')['Mileage'].mean().reset_index(name='Avg_Mileage')

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had grouped by Fuel_Type and got the average Mileage\n")
    f.write("--------------------------------\n")
    f.write(df_fueltype.head().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

