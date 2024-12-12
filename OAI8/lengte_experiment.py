import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

lengtes = [
    180, 191, 182, 170, 182, 180, 186, 159.5,
    182, 193, 175, 197, 200, 175]

"""
15  9.5
16  -
17  0   5   5
18  0   2   2   0   6   2 
19  1   3   7   
20  0
"""

sns.histplot(lengtes)
plt.show()

print(f"Het gemiddelde is {np.mean(lengtes)}")
print(f"De mediaan is {np.median(lengtes)}")