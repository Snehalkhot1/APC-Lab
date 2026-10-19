import numpy as np
import pandas as pd

# NumPy array creation
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

# Array operations
print("Addition:", arr + 5)
print("Subtraction:", arr - 5)
print("Multiplication:", arr * 2)
print("Division:", arr / 10)

# Array statistics
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Pandas Series
s = pd.Series([10, 20, 30, 40, 50])
print("\nPandas Series:")
print(s)

# Pandas DataFrame
data = {
    "Name": ["Asha", "Ravi", "Neha", "Amit"],
    "Marks": [78, 85, 92, 67]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

print("\nStudents scoring above 80:")
print(df[df["Marks"] > 80])