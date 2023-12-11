import matplotlib.pyplot as plt

# Read and convert file to Python data
file = open("expenses.txt", "r").read()
expenses = eval(file)

# colors for each category
colors = ['#FF0000', '#1D3366', '#046FC6', "#94D1E0", '#82AEC0', '#2F7889']

# Plotting Pie Chart
fig, ax = plt.subplots()
ax.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%', startangle=90, colors=colors)
ax.axis('equal')

plt.show()

