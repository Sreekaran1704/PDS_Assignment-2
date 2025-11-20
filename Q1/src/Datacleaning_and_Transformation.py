from Data_Acessing import df, log_dir
import re
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


script_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(script_dir, "..", 'reports')
data_dir = os.path.join(script_dir, "..", 'Data')
if not os.path.exists(reports_dir):
    os.makedirs(reports_dir)

# Drop the first column which is unnamed
df.drop(df.columns[0], axis=1, inplace=True)

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Data Cleaning and Transformation\n")
    f.write("--------------------------------\n")
    f.write("Dataframe after dropping the first column named Unnamed: 0\n")
    f.write(df.head().to_string())
    f.write("--------------------------------\n")
    f.write("Null values in the dataframe\n")
    f.write(df.isnull().sum().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

# Removing the cc in engine column and filling the missing values with the conditional median values

def cc_to_litres(engine):
    try:
        cc = int(str(engine).split()[0])
        return round(cc / 1000, 1)
    except:
        return None

def extract_engine_model(name):
    match = re.search(r'(\d\.\d)', str(name))
    return match.group(1) if match else None

df['Engine_Model'] = df['Engine'].apply(cc_to_litres)

# Extracting the engine info from name
df_temp = df.loc[df['Engine_Model'].isna(), 'Name'].apply(extract_engine_model)
df_temp = df_temp.astype(float) 

df.loc[df['Engine_Model'].isna(), 'Engine_Model'] = df_temp

df['Engine_Model'] = df['Engine_Model'].astype(float)

df['Model'] = df['Name'].str.split().str[:2].str.join(' ')
df['Brand'] = df['Name'].str.split().str[0]

# Model-level median fill
df['Engine_Model'] = df.groupby('Model')['Engine_Model'].transform(
    lambda x: x.fillna(x.median())
)
# Brand-level median fill
df['Engine_Model'] = df.groupby('Brand')['Engine_Model'].transform(
    lambda x: x.fillna(x.median())
)

# Final fallback
df['Engine_Model'] = df['Engine_Model'].fillna(1.4)

df.drop('Engine', axis=1, inplace=True)
df.rename(columns={'Engine_Model': 'Engine'}, inplace=True)

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had removed the cc in engine column and filled the missing values with the conditional median values\n")
    f.write("--------------------------------\n")
    f.write(df.head().to_string())
    f.write("--------------------------------\n")
    f.write("Null values in the dataframe after doing the engine model cleaning and transformation")
    f.write(df.isnull().sum().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

with open(os.path.join(reports_dir, 'report.txt'), 'w') as f:
    f.write("--------------------------------\n")
    f.write("Engine model was first derived from Engine CC for accuracy, then extracted from the Name string when CC was missing. Remaining gaps were filled using model-level and brand-level medians because they best represent real engine patterns while avoiding outlier distortion. Median ensures stable, realistic imputation compared to mean or mode.")
    f.write("--------------------------------\n")

# Power cleaning and transformation using the median value

def clean_power(x):
    if pd.isna(x):
        return None
    match = re.search(r'([\d\.]+)', str(x))
    return float(match.group(1)) if match else None

df['Power'] = df['Power'].apply(clean_power)


# POWER
df['Power'] = df.groupby(
    ['Model', 'Engine', 'Fuel_Type']
)['Power'].transform(lambda x: x.fillna(x.median()))

df['Power'] = df.groupby(
    ['Model', 'Engine']
)['Power'].transform(lambda x: x.fillna(x.median()))

df['Power'] = df.groupby('Engine')['Power'].transform(
    lambda x: x.fillna(x.median())
)

df['Power'] = df.groupby('Brand')['Power'].transform(
    lambda x: x.fillna(x.median())
)

df['Power'] = df['Power'].fillna(75)

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had cleaned the power column and filled the missing values with the median value\n")
    f.write("--------------------------------\n")
    f.write(df.head().to_string())
    f.write("--------------------------------\n")
    f.write("Null values in the dataframe after doing the power cleaning and transformation")
    f.write(df.isnull().sum().to_string())
    f.write("--------------------------------\n")

with open(os.path.join(reports_dir, 'report.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Power values were cleaned by extracting numeric bhp. Missing values were filled hierarchically: first using Model–Engine–Fuel groups, then Model–Engine, then Engine alone, and finally Brand medians because this preserves realistic horsepower patterns across variants. Median was chosen to avoid distortion from extreme high-bhp outliers.")
    f.write("--------------------------------\n")

# Seats cleaning and transformation using the median value
df['Seats'] = df.groupby('Model')['Seats'].transform(
    lambda x: x.fillna(x.median())
)

df['Seats'] = df.groupby('Brand')['Seats'].transform(
    lambda x: x.fillna(x.median())
)

df['Seats'] = df['Seats'].fillna(5)

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had cleaned the seats column and filled the missing values with the median value\n")
    f.write("--------------------------------\n")
    f.write(df.head().to_string())
    f.write("--------------------------------\n")
    f.write("Null values in the dataframe after doing the seats cleaning and transformation")
    f.write(df.isnull().sum().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

with open(os.path.join(reports_dir, 'report.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Seats were filled using model-level medians because cars of the same model almost always have identical seating capacity. Brand-level medians were used next since manufacturers follow consistent design patterns. Median avoids distortion from rare variants. Remaining missing values were set to 5, the most common seating capacity in the dataset.”")
    f.write("--------------------------------\n")

# Drop the rows where mileage is null
df.dropna(subset=['Mileage'], inplace=True)

with open(os.path.join(log_dir, 'log.txt'), 'w') as f:
    f.write("--------------------------------\n")
    f.write("Here we had dropped the rows where mileage is null\n")
    f.write("--------------------------------\n")
    f.write(df.head().to_string())
    f.write("--------------------------------\n")
    f.write("Null values in the dataframe after dropping the rows where mileage is null")
    f.write(df.isnull().sum().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

with open(os.path.join(reports_dir, 'report.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Rows with missing mileage were removed because only two entries lacked this information, making imputation unreliable. With such a small count, filling values could introduce noise or distort patterns. Dropping them preserves dataset integrity, avoids artificial values, and has no meaningful impact on model performance due to minimal loss.")
    f.write("--------------------------------\n")

#

def extract_mileage_value(x):
    if pd.isna(x):
        return None
    match = re.search(r'([\d\.]+)', str(x))
    return float(match.group(1)) if match else None

df['Mileage_Num'] = df['Mileage'].apply(extract_mileage_value)

def detect_mileage_unit(x):
    x = str(x).lower()
    if 'kg' in x:     # km/kg → CNG
        return 'km/kg'
    return 'kmpl'     # petrol/diesel etc.

df['Mileage_Unit'] = df['Mileage'].apply(detect_mileage_unit)

df.loc[df['Mileage_Unit']=='kmpl', 'Mileage_Num'] = \
df.groupby(['Model','Engine','Fuel_Type'])['Mileage_Num'].transform(
    lambda x: x.fillna(x.median())
)

df.loc[df['Mileage_Unit']=='kmpl', 'Mileage_Num'] = \
df.groupby(['Model','Fuel_Type'])['Mileage_Num'].transform(
    lambda x: x.fillna(x.median())
)

df.loc[df['Mileage_Unit']=='kmpl', 'Mileage_Num'] = \
df.groupby('Fuel_Type')['Mileage_Num'].transform(
    lambda x: x.fillna(x.median())
)

df.loc[df['Mileage_Unit']=='km/kg', 'Mileage_Num'] = \
df.groupby(['Model','Fuel_Type'])['Mileage_Num'].transform(
    lambda x: x.fillna(x.median())
)

df.loc[df['Mileage_Unit']=='km/kg', 'Mileage_Num'] = \
df.groupby('Fuel_Type')['Mileage_Num'].transform(
    lambda x: x.fillna(x.median())
)

df.loc[df['Mileage_Unit']=='km/kg', 'Mileage_Num'] = \
df.loc[df['Mileage_Unit']=='km/kg', 'Mileage_Num'].fillna(
    df[df['Mileage_Unit']=='km/kg']['Mileage_Num'].median()
)

df['Mileage_Clean'] = df['Mileage_Num']
df.drop(['Mileage', 'Mileage_Num'], axis=1, inplace=True)

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had cleaned the mileage column and filled the missing values with the median value\n")
    f.write("--------------------------------\n")
    f.write(df.head().to_string())
    f.write("--------------------------------\n")
    f.write("Null values in the dataframe after doing the mileage cleaning and transformation")
    f.write(df.isnull().sum().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

with open(os.path.join(reports_dir, 'report.txt'), 'a') as f:
    f.write("------------------------------------------------------------------------------------------------\n")
    f.write("Mileage required separate handling because kmpl (liquid fuels) and km/kg (CNG) represent different units and cannot be directly compared. Group-based median imputation preserves realistic mileage patterns within each fuel–model combination while avoiding distortion from outliers. Treating CNG and Petrol/Diesel separately prevents incorrect conversions and ensures accurate, unit-aware feature representation.")
    f.write("------------------------------------------------------------------------------------------------\n")

# Clean new price using the median value
def clean_new_price(x):
    if pd.isna(x):
        return None
    
    x = str(x).lower().strip()
    match = re.search(r'([\d\.]+)', x)
    if not match:
        return None
    num = float(match.group(1))
    
    if "lakh" in x or "lac" in x:
        return num * 100000
    elif "cr" in x or "crore" in x:
        return num * 10000000
    else:
        return num

df['New_Price'] = df['New_Price'].apply(clean_new_price)

# Fill missing using hierarchy
df['New_Price'] = df.groupby(
    ['Model', 'Engine', 'Year']
)['New_Price'].transform(lambda x: x.fillna(x.median()))

df['New_Price'] = df.groupby(
    ['Model', 'Engine']
)['New_Price'].transform(lambda x: x.fillna(x.median()))

df['New_Price'] = df.groupby('Model')['New_Price'].transform(
    lambda x: x.fillna(x.median())
)

df['New_Price'] = df.groupby('Brand')['New_Price'].transform(
    lambda x: x.fillna(x.median())
)

df['New_Price'] = df['New_Price'].fillna(df['New_Price'].median())

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had cleaned the new price column and filled the missing values with the median value\n")
    f.write("--------------------------------\n")
    f.write(df.head().to_string())
    f.write("--------------------------------\n")
    f.write("Null values in the dataframe after doing the new price cleaning and transformation\n")
    f.write(df.isnull().sum().to_string())
    f.write("\n")
    f.write("--------------------------------\n")

with open(os.path.join(reports_dir, 'report.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("New_Price was first converted into numeric rupee values by handling ‘Lakh’ and ‘Crore’ units to standardize price scale. Missing values were filled using medians within Model–Engine–Year groups, then broader groups, because cars of similar model and engine share realistic showroom prices. Median avoids skew from luxury outliers, ensuring stable price estimation.")
    f.write("--------------------------------\n")


# Export the dataframe to a csv file
df.to_csv(os.path.join(data_dir, 'cleaned_data.csv'), index=False)

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had exported the dataframe to a csv file\n")
    f.write("--------------------------------\n")
    f.write(df.head().to_string())
#
