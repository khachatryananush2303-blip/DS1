import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv('kidney_disease.csv')

# Replace '?' or other non-numeric strings with np.nan
df.replace('?', np.nan, inplace=True)

# ------------------------------
# Fill missing values
# ------------------------------

# Categorical columns: fill missing with mode
categorical_cols = ['rbc','pc','pcc','ba','htn','dm','cad','appet','pe','ane','classification']
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Numerical columns: convert to numeric and fill missing with mean
numerical_cols = ['age','bp','sg','al','su','bgr','bu','sc','sod','pot','hemo','pcv','wc','rc']
for col in numerical_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # converts non-numeric to NaN
    df[col] = df[col].fillna(df[col].mean())

print(df.info())

# ------------------------------
# Scatter Plot: Age vs Sugar (sg)
# ------------------------------
plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['sg'], color='b', alpha=0.7)
plt.title("Scatter Plot of Age vs Sugar (sg)")
plt.xlabel("Age")
plt.ylabel("Sugar (sg)")
plt.grid(True)
plt.show()

# Pie Charts for Categorical Columns
# ------------------------------
plt.figure(figsize=(20, 10))

for i, col in enumerate(categorical_cols[:8], 1):  # Plot first 8 categorical columns
    plt.subplot(2, 4, i)
    counts = df[col].value_counts()
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
    plt.title(col)

plt.tight_layout()
plt.show()
