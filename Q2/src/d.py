import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from c import pop_bp_mean, pop_bp_std, pop_bp_p98, boot_mean_avg, boot_std_avg, boot_p98_avg, boot_means, reports_dir, log_dir, df
import os


# --- Chart: Mean comparison ---
plt.figure()
labels = ['Population', 'Bootstrap avg']
values = [pop_bp_mean, boot_mean_avg]
plt.bar(labels, values)
plt.ylabel("BloodPressure")
plt.title("BloodPressure Mean: Population vs Bootstrap Avg (500 samples of n=150)")
plt.savefig(os.path.join(reports_dir, '../plots/D1.png'))

# --- Chart: Std deviation comparison ---
plt.figure()
values = [pop_bp_std, boot_std_avg]
plt.bar(labels, values)
plt.ylabel("BloodPressure")
plt.title("BloodPressure Std Dev: Population vs Bootstrap Avg")
plt.savefig(os.path.join(reports_dir, '../plots/D2.png'))

# --- Chart: 98th percentile comparison ---
plt.figure()
values = [pop_bp_p98, boot_p98_avg]
plt.bar(labels, values)
plt.ylabel("BloodPressure")
plt.title("BloodPressure 98th Percentile: Population vs Bootstrap Avg")
plt.savefig(os.path.join(reports_dir, '../plots/D3.png'))

# Optional: show distribution of bootstrap means (nice for report)
plt.figure()
plt.hist(boot_means, bins=30)
plt.xlabel("Bootstrap mean of BloodPressure")
plt.ylabel("Frequency")
plt.title("Distribution of Bootstrap Means (BloodPressure)")
plt.savefig(os.path.join(reports_dir, '../plots/D4.png'))

with open(os.path.join(reports_dir, 'report.md'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Part (d)\n")
    f.write("--------------------------------\n")
    f.write(f"Population BloodPressure mean: {pop_bp_mean}\n")
    f.write(f"Bootstrap average mean: {boot_mean_avg}\n")
    f.write(f"Bootstrap average std : {boot_std_avg}\n")
    f.write(f"Bootstrap average 98th percentile: {boot_p98_avg}\n")
    f.write("--------------------------------\n")

    f.write("![D1](../plots/D1.png)\n")
    f.write("\n")
    f.write("Here is the chart D1: Mean comparison\n")
    f.write("\n")
    f.write("![D2](../plots/D2.png)\n")
    f.write("\n")
    f.write("Here is the chart D2: Std deviation comparison\n")
    f.write("\n")
    f.write("![D3](../plots/D3.png)\n")
    f.write("\n")
    f.write("Here is the chart D3: 98th percentile comparison\n")
    f.write("\n")
    f.write("![D4](../plots/D4.png)\n")
    f.write("\n")
    f.write("Here is the chart D4: Distribution of Bootstrap Means\n")
    f.write("\n")
    f.write("--------------------------------\n")
