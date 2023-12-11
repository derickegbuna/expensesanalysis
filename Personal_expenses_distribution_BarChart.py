import matplotlib.pyplot as plt

# Read and convert file data to python data
file = open("expenses.txt", "r").read()
expenses = eval(file)

# Colors
colors = ['#ff9999', '#ffb3e6', '#ffcc99', "#c2c2f0", '#66b3ff', '#99ff99']

# Split Dictionary keys and value into separate python list
label = expenses.keys()
amount = expenses.values()

# Plotting Bar Chart
fig, ax = plt.subplots()
bars = ax.bar(label, amount, color=colors)

# Add Data Labels
for bar, amount in zip(bars, amount):
    yAxis = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yAxis, round(amount, 2), ha='center', va='bottom')

# Add Labels and Title
plt.xlabel('Expenses Categories')
plt.ylabel('Average Monthly Expenses (CAD)')
plt.title('Average Monthly Expenses')

# Slant labels, change font size
plt.xticks(rotation=25, ha='right', fontsize=7)

plt.show()
