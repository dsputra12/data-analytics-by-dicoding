import numpy as np
import pandas as pd
import scipy
import matplotlib
import seaborn as sns

array1 = np.array([2,3,6,5])
print(array1[2], array1[3])

data = {
    'nama' : ['Putra', 'Putri', 'Putro'],
    'age': [10,23,244]
}

df = pd.DataFrame(data)
print(df)

print(scipy.__version__)
print(matplotlib.__version__)
print(sns.__version__)