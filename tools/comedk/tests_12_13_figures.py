"""Draw the original data-bearing figures for COMEDK Tests 12 and 13."""
import numpy as np
from matplotlib.patches import Circle

from tests_04_05_figures import INK, chart, diagram, polygon, save


def test_12_figures():
    fig, ax = chart()
    ax.plot([1, 2, 3], [2, 3, 7], marker="o", color=INK)
    for label, x, y in [("P", 1, 2), ("Q", 2, 3), ("R", 3, 7)]:
        ax.annotate(label, (x, y), xytext=(6, 4), textcoords="offset points")
    ax.set(xlabel="Current (A)", ylabel="Voltage (V)", xlim=(.7, 3.35),
           ylim=(1.2, 7.9), xticks=[1, 2, 3], yticks=range(2, 8))
    save(12, 54, fig)

    fig, ax = diagram((-2.35, 2.35), (-1.6, 1.6))
    for x, y, label in [(0, 0, "M"), (-1, 0, "X"), (1, 0, "X"),
                        (0, -1, "Y"), (0, 1, "Y")]:
        if label != "M":
            ax.plot([0, x], [0, y], color=INK, lw=1.5)
        ax.add_patch(Circle((x, y), .22, facecolor="white", edgecolor=INK, zorder=4))
        ax.text(x, y, label, ha="center", va="center", zorder=5)
    save(12, 82, fig)

    fig, ax = diagram((-2.45, 2.45), (-1.55, 1.62))
    ax.plot([-2.2, 2.2, 2.2, -2.2, -2.2], [-1.3, -1.3, 1.4, 1.4, -1.3], color=INK)
    for x, label in [(-.65, "A"), (.65, "B")]:
        ax.add_patch(Circle((x, 0), 1, fill=False, edgecolor=INK))
        ax.text(x, 1.13, label, ha="center")
    for x, y, label in [(-1, 0, "7"), (0, 0, "4"), (1, 0, "8"),
                        (1.8, -1, "6"), (-1.92, 1.12, "U")]:
        ax.text(x, y, label, ha="center", va="center")
    save(12, 122, fig)

    fig, ax = diagram((-2.8, 2.8), (-1.08, 1.08))
    for x, label in [(-2, "1"), (0, "2"), (2, "3")]:
        ax.add_patch(Circle((x, 0), .25, fill=False, edgecolor=INK))
        ax.text(x, 0, label, ha="center", va="center")
    for start, end in [(-1.72, -.28), (.28, 1.72)]:
        ax.annotate("", (end, 0), (start, 0), arrowprops={"arrowstyle": "->", "color": INK})
    save(12, 125, fig)


def test_13_figures():
    fig, ax = chart()
    masses = [2, 4, 12, 28, 56, 92, 132, 200, 236]
    energies = [1.1, 7.1, 7.68, 8.45, 8.79, 8.65, 8.40, 7.90, 7.60]
    ax.plot(masses, energies, color=INK, lw=1.8)
    for x, y, name in [(4, 7.1, "A"), (56, 8.79, "B"), (236, 7.60, "C")]:
        ax.scatter(x, y, color=INK)
        ax.annotate(name, (x, y), xytext=(6, 4), textcoords="offset points")
    ax.set(xlabel="Mass number", ylabel="Binding energy/nucleon (MeV)",
           xlim=(0, 255), ylim=(0, 10), yticks=[0, 2, 4, 6, 8, 10])
    save(13, 9, fig)

    fig, ax = chart()
    time = np.linspace(0, 4, 601)
    wave = np.sin(np.pi * time)
    ax.plot(time, wave, color=INK, linestyle="--", label="Input")
    ax.plot(time, np.abs(wave), color=INK, label="Output")
    ax.axhline(0, lw=.8, color="#666666")
    ax.legend(loc="lower left", ncol=2)
    ax.set(xlabel="Time (arbitrary units)", ylabel="Normalised voltage", ylim=(-1.6, 1.3))
    save(13, 45, fig)

    fig, ax = chart()
    time = np.linspace(0, 6, 301)
    ax.plot(time, .9 * np.exp(-.42 * time), color=INK, lw=1.8)
    for instant, label in [(1, "L"), (4, "M")]:
        point = .9 * np.exp(-.42 * instant)
        dx = np.linspace(-.91, .91, 9)
        ax.plot(instant + dx, point - .42 * point * dx, color="#57758a", linestyle="--")
        ax.scatter(instant, point, color=INK)
        ax.annotate(label, (instant, point), xytext=(7, 9), textcoords="offset points")
    ax.set(xlabel="Time (s)", ylabel="Concentration of A (mol/L)", ylim=(0, 1))
    save(13, 64, fig)

    fig, ax = chart()
    polygon(ax, [(0, 0), (4, 0), (3, 1), (0, 3)])
    ax.set(xlabel="x", ylabel="y", xlim=(-.24, 4.75), ylim=(-.22, 3.6),
           xticks=range(5), yticks=range(4))
    save(13, 121, fig)


if __name__ == "__main__":
    test_12_figures()
    test_13_figures()
