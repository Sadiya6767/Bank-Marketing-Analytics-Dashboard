import pandas as pd

df = pd.read_csv("data/bank.csv")
print(df.head())
print(df.info())

print("Missing Values:")
print(df.isnull().sum())

print("Duplicate Values:")
print(df.duplicated().sum())

print("Extra Space")
df.columns = df.columns.str.strip()

print("Text Column to lowercase")
for col in df.select_dtypes(include=['object','string']).columns:    df[col] = df[col].str.strip().str.lower()

print("Save Cleaned Data")
df.to_csv("data/cleaned.csv", index=False)

print("Data Cleaned")
print("File Saved Successfully")


summary = df.describe(include = 'all')
summary.to_excel("data/summary.xlsx")
print("Report Generated Successfully")