import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../Data/train.csv')

# get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# print the first 5 rows of the dataframe in the logfile
log_dir = os.path.join(script_dir, "..", "log")

# create the log directory if it doesn't exist
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# print the first 5 rows of the dataframe in the logfile
with open(os.path.join(log_dir, 'log.txt'), 'w') as f:
    f.write(df.head().to_string())
