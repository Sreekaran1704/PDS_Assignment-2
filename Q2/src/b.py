import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from a import sample_25, df, reports_dir, log_dir
import os

# ----- Part (b) -----

# Population 98th percentile for BMI
pop_bmi_p98 = np.percentile(df['BMI'], 98)

# Sample 98th percentile for BMI (same sample_25)
sample_bmi_p98 = np.percentile(sample_25['BMI'], 98)

with open(os.path.join(reports_dir, 'report.md'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Part (b)\n")
    f.write("--------------------------------\n")
    f.write(f"Population BMI 98th percentile: {pop_bmi_p98}\n")
    f.write(f"Sample(25) BMI 98th percentile: {sample_bmi_p98}\n")
    f.write("--------------------------------\n")

# Chart: BMI 98th percentile comparison
plt.figure()
labels = ['Population', 'Sample (n=25)']
p98_vals = [pop_bmi_p98, sample_bmi_p98]
plt.bar(labels, p98_vals)
plt.ylabel("BMI")
plt.title("98th Percentile of BMI: Population vs Sample (n=25)")
plt.savefig(os.path.join(reports_dir, '../plots/chart_3.png'))

with open(os.path.join(reports_dir, 'report.md'), 'a') as f:
    f.write("--------------------------------\n")
    f.write("Chart 3: BMI 98th percentile comparison\n")
    f.write("--------------------------------\n")
    f.write("Here is the chart 3: BMI 98th percentile comparison\n")
    f.write("\n")
    f.write("![Chart 3](../plots/chart_3.png)\n")
    f.write("\n")
    f.write("--------------------------------\n")
    f.write("This figure compares the 98th percentile of BMI for the full population with the 98th percentile from the sample of 25 observations. We observe that the two values are close but not identical. This difference is expected: the 98th percentile is a high-end, tail statistic, and tail values are extremely sensitive to sample size. Because the sample contains only 25 individuals, its upper-percentile estimate is based on very few data points, so even small changes in the selected observations can shift the percentile noticeably. The population’s 98th percentile is more stable because it uses all 768 observations. The chart shows that while the sample gives a rough approximation, small samples are less reliable for estimating extreme percentiles compared to central measures like the mean.")
    f.write("\n")
    f.write("--------------------------------\n")