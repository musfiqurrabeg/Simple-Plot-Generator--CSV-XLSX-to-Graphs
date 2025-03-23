import os
import pandas as pd
import matplotlib.pyplot as plt

# File Input
file_path = input("Enter the file path (CSV/XLSX): ").strip()

# Load Data
if file_path.endswith('.csv'):
    df = pd.read_csv(file_path)
elif file_path.endswith('.xlsx'):
    df = pd.read_excel(file_path)
else:
    print("Unsupported file format! Please provide a CSV or XLSX file.")
    exit()

# Display column details
print(f"\nTotal Columns: {len(df.columns)}")
print("Column Names:", list(df.columns))

# Plot Selection Menu
plot_options = {
    1: "Line Plot",
    2: "Bar Chart",
    3: "Histogram",
    4: "Scatter Plot",
    5: "Box Plot",
    6: "Pie Chart",
    7: "Density Plot",
    8: "Hexbin Plot",
    9: "Area Plot"
}

print("\nAvailable Plots:")
for key, value in plot_options.items():
    print(f"{key}. {value}")

# Get user choice
try:
    plot_choice = int(input("\nEnter the number of your desired plot: "))
    if plot_choice not in plot_options:
        raise ValueError
except ValueError:
    print("Invalid choice! Exiting program.")
    exit()

# Get X and Y-axis columns
x_column = input("Enter the X-axis column name: ").strip()
y_column = input("Enter the Y-axis column name: ").strip()

if x_column not in df.columns or y_column not in df.columns:
    print("Invalid column names! Please enter correct column names.")
    exit()

# Plot generation
plt.figure(figsize=(8, 5))
plot_title = input("Enter a Title for plot: ")

if plot_choice == 1:
    df.plot(x=x_column, y=y_column, kind='line', title=plot_title)
elif plot_choice == 2:
    df.plot(x=x_column, y=y_column, kind='bar', title=plot_title)
elif plot_choice == 3:
    df[y_column].plot(kind='hist', title=plot_title)
elif plot_choice == 4:
    df.plot(x=x_column, y=y_column, kind='scatter', title=plot_title)
elif plot_choice == 5:
    df[[x_column, y_column]].plot(kind='box', title=plot_title)
elif plot_choice == 6:
    df[y_column].value_counts().plot(kind='pie', title=plot_title, autopct='%1.1f%%')
elif plot_choice == 7:
    df[y_column].plot(kind='density', title=plot_title)
elif plot_choice == 8:
    df.plot.hexbin(x=x_column, y=y_column, gridsize=25, cmap='Blues', title=plot_title)
elif plot_choice == 9:
    df.plot(x=x_column, y=y_column, kind='area', title=plot_title, alpha=0.5)

plt.xlabel(x_column)
plt.ylabel(y_column)

# Save the plot
plot_filename = f"{plot_options[plot_choice].replace(' ', '_')}.png"
plt.savefig(plot_filename, bbox_inches='tight')
plt.show()

print(f"\nPlot saved successfully as {plot_filename}")
