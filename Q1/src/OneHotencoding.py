from Data_Acessing import log_dir
from Datacleaning_and_Transformation import df, reports_dir
import pandas as pd
import os

# Do OneHOt encoding for column Fuel_type
df = pd.get_dummies(df, columns=['Fuel_Type'])
df = pd.get_dummies(df, columns=['Transmission'])

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Here we had done the one hot encoding for the Fuel_Type and Transmission columns\n")
    f.write("--------------------------------\n")
    f.write(df.head().to_string())