import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

nilai_ujian = np.array([5, 1, 3, 4, 2, 2, 2])

# Calculate the mean
rataan = nilai_ujian.mean()

# Calculate the median
median = np.median(nilai_ujian)

# Calculate the mode (returns an array, hence [0] to get the value)
modus = stats.mode(nilai_ujian)[0]

# Calculate the range (max - min)
range = nilai_ujian.max() - nilai_ujian.min()

# Calculate the IQR
iqr = np.percentile(nilai_ujian, 75) - np.percentile(nilai_ujian, 25)

# Sort the array
sorted = np.sort(nilai_ujian)

#Variance using Pandas
nilai_ujian_series = pd.Series(nilai_ujian)
variance = nilai_ujian_series.var()

#Stdev
stdev = nilai_ujian_series.std()

# # Print the results
# print(sorted)
# print(rataan)
# print(median)
# print(modus)
# print(range)
# print(iqr)
# print(nilai_ujian_series)
# print(variance)
# print(stdev)

# #Histogram
# plt.hist(nilai_ujian, bins = 5)
# plt.show()

# #Skewedness
# skewedness = nilai_ujian_series.skew()
# print(skewedness)

sample_data = {
    'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],  
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}
 
df = pd.DataFrame(sample_data)
 
korelasi = df.corr(numeric_only=True)
kovarian = df.cov(numeric_only=True)
print(korelasi)
print(kovarian)
