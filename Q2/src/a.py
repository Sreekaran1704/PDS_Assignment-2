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

plt.savefig(os.path.join(reports_dir, '../plots/chart_1.png'))

with open(os.path.join(reports_dir, 'report.md'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("\n")
    f.write(f"Population Glucose mean: {pop_glucose_mean}\n")
    f.write(f"Sample(25) Glucose mean: {sample_glucose_mean}\n")
    f.write("\n")
    f.write(f"Population Glucose max: {pop_glucose_max}\n")
    f.write(f"Sample(25) Glucose max: {sample_glucose_max}\n")
    f.write("\n")
    f.write("--------------------------------\n")
    f.write("Chart 1: Mean Glucose comparison\n")
    f.write("--------------------------------\n")
    f.write("Here is the chart 1: Mean Glucose comparison\n")
    f.write("\n")
    f.write("![Chart 1](../plots/chart_1.png)\n")
    f.write("\n")
    f.write(f"The first figure compares the mean Glucose level of the full population with the mean from a random sample of 25 observations. The sample mean is expected to be close to the population mean, but slight differences occur due to sampling variability. Since the sample contains only a small portion of the population, its average depends heavily on which individuals happened to be selected. This illustrates how small samples can reasonably estimate central tendency but still fluctuate around the true value. The second figure compares the maximum Glucose value in the population with the maximum value in the sample. Here, the difference is much larger. Because extreme values are rare, a small sample of 25 is unlikely to capture the highest Glucose measurement found in the population. This visual gap highlights a key concept: small samples are poor at representing population extremes, even though they may approximate the mean reasonably well.")
    f.write("\n")
    f.write("--------------------------------\n")

# --- Chart 2: Max Glucose comparison ---
plt.figure()
max_vals = [pop_glucose_max, sample_glucose_max]
plt.bar(labels, max_vals)
plt.ylabel("Glucose")
plt.title("Max Glucose: Population vs Sample (n=25)")
plt.savefig(os.path.join(reports_dir, '../plots/chart_2.png'))

with open(os.path.join(reports_dir, 'report.md'), 'a') as f:
    f.write("--------------------------------\n")
    f.write(f"Population Glucose max: {pop_glucose_max}\n")
    f.write(f"Sample(25) Glucose max: {sample_glucose_max}\n")
    f.write("\n")
    f.write("--------------------------------\n")
    f.write("Chart 2: Max Glucose comparison\n")
    f.write("--------------------------------\n")
    f.write("Here is the chart 2: Max Glucose comparison\n")
    f.write("\n")
    f.write("![Chart 2](../plots/chart_2.png)\n")
    f.write("\n")
    f.write("From this figure, we observe that the maximum Glucose value in the population and in the sample of 25 patients are almost identical. This is unusual because small samples typically fail to capture extreme values that exist in the full population. In this case, however, the random sample happened to include a patient whose Glucose level was nearly as high as the overall maximum recorded across all 768 individuals. This suggests that the sample contains at least one extreme or near-extreme observation. Overall, the figure shows that even a small sample can occasionally approximate population extremes, but this should not be assumed in general since such matches occur mostly by chance rather than representativeness.")
    f.write("\n")
    f.write("--------------------------------\n")



