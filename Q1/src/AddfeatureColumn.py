from datetime import datetime
from OneHotencoding import df, log_dir, reports_dir
import os
import pandas as pd

current_year = datetime.now().year
df['Car_Age'] = current_year - df['Year']
df['Car_Age'] = df['Car_Age'].clip(lower=0)

with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("\n")
    f.write("--------------------------------\n")
    f.write("Here we had added the Car_Age column\n")
    f.write("--------------------------------\n")
    f.write(df.head().to_string())
    f.write("--------------------------------\n")


