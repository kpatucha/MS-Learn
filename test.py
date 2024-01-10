import matplotlib.pyplot as plt

fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.plot([1,3,4])

def show_new_figure(evt=None):
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1, 1, 1)
    ax2.plot([1,2,5])
    fig2.show()

# Upon pressing any key in fig1, show fig2.
fig1.canvas.mpl_connect("key_press_event", show_new_figure)

plt.show()