ages =[10, 20, 35, 50, 28, 40, 55, 18, 16, 55, 30, 25, 43, 18, 30, 28, 14, 24, 16, 17, 32, 35, 26, 27, 65, 18, 43, 23, 21, 19, 70]
import numpy as np
ages_mean = np.mean(ages)
#print(ages_mean)
sample_size = 10
age_sample = np.random.choice(ages, sample_size)
#print(age_sample)
from scipy.stats import ttest_1samp
#print(ttest_1samp(age_sample, 30))
import pandas as pd
