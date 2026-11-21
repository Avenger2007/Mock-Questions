"""Draw the original COMEDK Tests 6 and 7 figures."""
import numpy as np
import matplotlib.pyplot as plt

from tests_04_05_figures import chart, diagram, polygon, save, INK


def main():
    fig, ax = chart()
    x = np.linspace(0, 4.2, 60)
    ax.plot(x, x*x/4, color=INK)
    for label, v, i in (("P", 2, 1), ("Q", 4, 4)):
        ax.scatter(v, i, color=INK)
        ax.annotate(label, (v, i), xytext=(-12, 5), textcoords="offset points")
    ax.set(xlabel="Voltage (V)", ylabel="Current (A)", xticks=range(5), yticks=range(5),
           xlim=(0, 4.45), ylim=(0, 4.65))
    save(6, 13, fig)

    fig, ax = chart()
    ax.plot([0, 3], [12, 0], marker="o", color=INK)
    ax.set(xlabel="Position (m)", ylabel="Force (N)", xticks=range(4), yticks=range(0, 13, 4),
           xlim=(-.15, 3.2), ylim=(-.7, 13))
    save(6, 14, fig)

    fig, ax = chart()
    x = np.linspace(0, .12, 300)
    ax.plot(x, 105-170*x, color=INK, linewidth=2)
    ax.plot(x, 140/(1+90*x), color=INK, linewidth=2, linestyle="--")
    ax.text(.105, 91, "X")
    ax.text(.023, 36, "Y")
    ax.set(xlabel="Square root of concentration (mol/L)¹ᐟ²",
           ylabel="Molar conductivity\n(S cm²/mol)", xlim=(0, .12), ylim=(0, 145))
    save(6, 63, fig)

    fig, ax = chart()
    polygon(ax, [(0, 0), (5, 0), (3, 2), (0, 4)])
    ax.set(xlabel="x", ylabel="y", xticks=range(6), yticks=range(5),
           xlim=(-.2, 5.6), ylim=(-.25, 4.6))
    save(6, 136, fig)

    fig, axes = plt.subplots(3, 1, figsize=(6.1, 2.85))
    t = np.linspace(0, 4*np.pi, 300)
    for ax, name, y in zip(axes, "PQR", (np.sin(t), np.maximum(np.sin(t),0), np.abs(np.sin(t)))):
        ax.plot(t, y, color=INK, linewidth=1.7)
        ax.axhline(0, color="gray", linewidth=.7)
        ax.set(ylim=(-1.15,1.15), xlim=(0,4*np.pi), xticks=[], yticks=[],
               ylabel=name)
    axes[-1].set_xlabel("Time →")
    fig.tight_layout(pad=.55)
    save(7, 4, fig)

    fig, ax = chart()
    ax.plot([0, .10, .20], [0, 6, 0], marker="o", color=INK)
    ax.set(xlabel="Time (s)", ylabel="Force (N)", xticks=[0,.10,.20],
           yticks=[0,2,4,6], xlim=(-.015,.215), ylim=(-.3,6.6))
    save(7, 35, fig)

    fig, ax = diagram((-2.1, 2.5), (0, 2.6))
    for x in (-.60,.60):
        ax.plot([x-.29,x+.29],[1.98,1.98], color=INK, lw=1.8)
    for x in (-1,0,1):
        ax.plot([x-.29,x+.29],[.67,.67], color=INK, lw=1.8)
        ax.text(x,.77,"↑↓", ha="center",fontsize=19)
    ax.annotate("", xy=(1.64,1.98), xytext=(1.64,.67),
                arrowprops=dict(arrowstyle="<->", color=INK))
    ax.text(1.77,1.34,"Gap",va="center")
    save(7, 82, fig)

    fig, ax = chart()
    polygon(ax, [(0, 0), (4, 0), (3, 3), (0, 3)])
    ax.set(xlabel="x", ylabel="y", xticks=range(5), yticks=range(4),
           xlim=(-.2, 4.6), ylim=(-.2, 3.5))
    save(7, 139, fig)


if __name__ == "__main__":
    main()
