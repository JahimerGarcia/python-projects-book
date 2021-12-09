import matplotlib.pyplot as plt

input_values = range(1, 5001)
squares = [x ** 3 for x in input_values]


plt.style.use("seaborn")

fig, ax = plt.subplots()

# line
# ax.plot(input_values, squares, linewidth=3)

# point
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", labelsize=14)

# Set the range for each axis.
# ax.axis([0, 1100, 0, 1100000])

plt.savefig("squares_plot.png")
# bbox_inches="tight" trims extra whitespace from the plot

plt.show()
