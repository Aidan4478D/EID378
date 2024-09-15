import pandas as pd
import numpy as np

# create dataframe
t = {
         "Scenario": ['w1', 'w2', 'w3', 'w4', 'w5'],
         "Probability": [0.2, 0.2, 0.3, 0.2, 0.1],
         "R1": [0.03, 0.17, 0.28, 0.05, -0.04],
         "R2": [0.09, 0.16, 0.10, 0.02, 0.15]
    }

df = pd.DataFrame(t)

# expected value & stdev
E1 = 0
E2 = 0
V1 = 0
V2 = 0

for i in range(len(df.index)):
    E1_l = df["R1"][i] * df["Probability"][i]
    E2_l = df["R2"][i] * df["Probability"][i]

    V1 += (df["R1"][i] - E1_l) ** 2 * df["Probability"][i]
    V2 += (df["R2"][i] - E1_l) ** 2 * df["Probability"][i]
    
    E1 += E1_l
    E2 += E2_l

std1 = np.sqrt(V1)
std2 = np.sqrt(V2)

print("E1 is " + str(E1) + " E2 is " + str(E2))
print("std1 is " + str(std1) + " std2 is " + str(std2))

# pearson correlation
