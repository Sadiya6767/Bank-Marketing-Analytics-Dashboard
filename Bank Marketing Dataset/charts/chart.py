import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/bank.csv")

# Age Distribution
plt.figure(figsize=(8,5))
plt.hist(df['age'], bins=20)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

plt.savefig("charts/age_distribution.png")
plt.show()

# Job Analysis
job_counts = df['job'].value_counts()

plt.figure(figsize=(10,5))
job_counts.plot(kind='bar')

plt.title("Customers by Job")
plt.xlabel("Job")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("charts/job_analysis.png")
plt.show()

# Deposit Analysis
deposit_counts = df['deposit'].value_counts()

plt.figure(figsize=(6,6))
deposit_counts.plot(kind='pie', autopct='%1.1f%%')

plt.ylabel("")
plt.title("Deposit Subscription")

plt.savefig("charts/deposit_analysis.png")
plt.show()