import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Sample Stock Data-AAPL.csv')
print(df.head())

null = df.isna().sum()/len(df)
print(null)

# %% plot inline figure
df.hist(figsize=(10,5))
plt.tight_layout()
plt.show()
