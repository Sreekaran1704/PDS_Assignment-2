import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from b import pop_bmi_p98, sample_bmi_p98, reports_dir, log_dir, df
import os

# ----- Part (c) -----

bp = df['BloodPressure']

# True population statistics
pop_bp_mean = bp.mean()
pop_bp_std = bp.std(ddof=1)   # sample std on full population
pop_bp_p98 = np.percentile(bp, 98)

with open(os.path.join(reports_dir, 'report.md'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Part (c)\n")
    f.write("--------------------------------\n")
    f.write(f"Population BloodPressure mean: {pop_bp_mean}\n")
    f.write(f"Population BloodPressure std : {pop_bp_std}\n")
    f.write(f"Population BloodPressure 98th percentile: {pop_bp_p98}\n")
    f.write("--------------------------------\n")

# Bootstrap settings
n_boot = 500
sample_size = 150

boot_means = []
boot_stds = []
boot_p98s = []

np.random.seed(123)  # reproducible bootstrap

for i in range(n_boot):
    boot_sample = bp.sample(n=sample_size, replace=True)
    boot_means.append(boot_sample.mean())
    boot_stds.append(boot_sample.std(ddof=1))
    boot_p98s.append(np.percentile(boot_sample, 98))

boot_means = np.array(boot_means)
boot_stds = np.array(boot_stds)
boot_p98s = np.array(boot_p98s)

# Average bootstrap estimates
boot_mean_avg = boot_means.mean()
boot_std_avg = boot_stds.mean()
boot_p98_avg = boot_p98s.mean()

with open(os.path.join(reports_dir, 'report.md'), 'a') as f:
    f.write("\n")
    f.write("--------------------------------\n")
    f.write("Part (c)\n")
    f.write("--------------------------------\n")
    f.write(f"Bootstrap average mean: {boot_mean_avg}\n")
    f.write(f"Bootstrap average std : {boot_std_avg}\n")
    f.write(f"Bootstrap average 98th percentile: {boot_p98_avg}\n")
    f.write("--------------------------------\n")

