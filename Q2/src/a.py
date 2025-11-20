import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Acessing import df, log_dir
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(script_dir, "..", 'reports')
if not os.path.exists(reports_dir):
    os.makedirs(reports_dir)

# ----- Part (a) -----

# Population stats for Glucose
pop_glucose_mean = df['Glucose'].mean()
pop_glucose_max = df['Glucose'].max()

# Sample of 25 (reproducible)
np.random.seed(123)           # fixed seed
sample_25 = df.sample(n=25, random_state=123)

# Sample stats
sample_glucose_mean = sample_25['Glucose'].mean()
sample_glucose_max = sample_25['Glucose'].max()


with open(os.path.join(log_dir, 'log.txt'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Part (a)\n")
    f.write("--------------------------------\n")
    f.write(f"Population Glucose mean: {pop_glucose_mean}\n")
    f.write(f"Sample(25) Glucose mean: {sample_glucose_mean}\n")
    f.write(f"Population Glucose max : {pop_glucose_max}\n")
    f.write(f"Sample(25) Glucose max : {sample_glucose_max}\n")
    f.write("--------------------------------\n")

# --- Chart 1: Mean Glucose comparison ---
plt.figure()
labels = ['Population', 'Sample (n=25)']
means = [pop_glucose_mean, sample_glucose_mean]
plt.bar(labels, means)
plt.ylabel("Glucose")
plt.title("Mean Glucose: Population vs Sample (n=25)")

plt.savefig(os.path.join(reports_dir, 'chart_1.png'))

with open(os.path.join(reports_dir, 'report.md'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Chart 1: Mean Glucose comparison\n")
    f.write("--------------------------------\n")
    f.write("Here is the chart 1: Mean Glucose comparison\n")
    f.write("![Chart 1](chart_1.png)\n")
    f.write("\n")
    f.write("--------------------------------\n")

# --- Chart 2: Max Glucose comparison ---
plt.figure()
max_vals = [pop_glucose_max, sample_glucose_max]
plt.bar(labels, max_vals)
plt.ylabel("Glucose")
plt.title("Max Glucose: Population vs Sample (n=25)")
plt.savefig(os.path.join(reports_dir, 'chart_2.png'))

with open(os.path.join(reports_dir, 'report.md'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Chart 2: Max Glucose comparison\n")
    f.write("--------------------------------\n")
    f.write("Here is the chart 2: Max Glucose comparison\n")
    f.write("![Chart 2](chart_2.png)\n")
    f.write("\n")
    f.write("--------------------------------\n")


