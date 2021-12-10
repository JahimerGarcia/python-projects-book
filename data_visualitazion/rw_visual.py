import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    # make a random walk
    rw = RandomWalk(500)
    rw.fill_walk()

    # plot the points in the walk
    plt.style.use("classic")
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
