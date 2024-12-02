import pandas as pd

df = pd.read_json("../steam.json")

df.describe()
df.info()
df.head()