import pandas as pd
import matplotlib.pyplot as plt

# Read the two CSV files
df1 = pd.read_csv("Temperature distribution 2D_diff+boundary conditions.csv")
df2 = pd.read_csv("Temperature distribution 2D_diff+sink+boundary conditions.csv")

# Create new table
result = pd.DataFrame({
    "Node": df1["Node"],
    "Temperature NO sink": df1["Numerical solution"],
    "Temperature With sink": df2["Numerical solution"],
})

# Compare the columns
result["Source/Sink +/-"] = result["Temperature With sink"] - result["Temperature NO sink"]

h = 7000
T_inf = 300

result["Source"] = -h * (
    result["Temperature With sink"] - T_inf
)

# Save as a new CSV
result.to_csv("comparison.csv", index=False)

# Plot
plt.figure(figsize=(8, 5))

plt.plot(
    result["Temperature NO sink"],
    result["Source/Sink +/-"],
    marker="o",
    linestyle="-"
)

plt.xlabel("Temperature without sink")
plt.ylabel("Source/Sink effect")
plt.title("Source/Sink Effect vs Temperature without Sink")

plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(
    result["Temperature With sink"],
    result["Source"],
    marker="o",
    linestyle="-"
)
plt.xlabel("Temperature with sink")
plt.ylabel("Source")
plt.grid(True)
plt.tight_layout()
plt.show()