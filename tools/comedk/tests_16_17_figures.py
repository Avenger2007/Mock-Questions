"""Render original data-bearing diagrams for COMEDK Tests 16 and 17."""
import numpy as np

from tests_04_05_figures import INK, chart, diagram, polygon, save


def draw_test_16():
    fig, ax = chart()
    x = np.array([0, 1, 2, 2.65, 3.1, 3.6, 4])
    y = [0, 1, 2, 2.38, 2.9, 2.77, 2.4]
    ax.plot(x, y, color=INK, linewidth=1.8)
    for label, index in [("O", 0), ("P", 2), ("Q", 4), ("R", 6)]:
        ax.scatter(x[index], y[index], color=INK, zorder=3)
        ax.annotate(label, (x[index], y[index]), xytext=(4, 8), textcoords="offset points")
    ax.set(xlabel="Strain (schematic)", ylabel="Stress (schematic)", xlim=(-.2, 4.42),
           ylim=(-.2, 3.45), xticks=[], yticks=[])
    save(16, 23, fig)

    fig, ax = chart()
    t = np.linspace(0, 4, 101)
    ax.plot(t, .5 + t, color=INK)
    ax.plot(t, .5 + .25*t**2, color="#587489", linestyle="--")
    ax.text(2.65, 2.86, "X")
    ax.text(2.65, 1.93, "Y")
    ax.set(xlabel="Time", ylabel="Position", xlim=(0, 4.2), ylim=(0, 5.1),
           xticks=[], yticks=[])
    save(16, 47, fig)

    fig, ax = chart()
    voltage = np.linspace(-3, 2, 301)
    for stop, style, name, colour in [(-2.45, "-", "G", INK), (-1.25, "--", "F", "#587489")]:
        current = 1 - np.exp(-1.24*np.maximum(voltage-stop, 0))
        ax.plot(voltage, current, style, color=colour, linewidth=1.6)
        ax.scatter(stop, 0, color=colour, zorder=3)
        ax.annotate(name, (stop, 0), xytext=(-4, -15), textcoords="offset points")
    ax.axvline(0, color="#777777", linewidth=.75)
    ax.set(xlabel="Applied voltage (V)", ylabel="Photocurrent (relative units)",
           xlim=(-3, 2), ylim=(-.22, 1.2), yticks=[0, 1])
    save(16, 51, fig)

    fig, ax = chart()
    ax.plot([-2, 0, 1.5], [2, 0, 3], color=INK, linewidth=1.8)
    ax.scatter(0, 0, color=INK, zorder=3)
    ax.axvline(0, color="#777777", linewidth=.65)
    ax.set(xlabel="x", ylabel="y", xlim=(-2.35, 1.85), ylim=(-.35, 3.45))
    save(16, 139, fig)

    fig, ax = chart()
    polygon(ax, [(0, 0), (5, 0), (4, 2), (1, 4)])
    ax.set(xlabel="x", ylabel="y", xlim=(-.22, 5.7), ylim=(-.2, 4.75),
           xticks=range(6), yticks=range(5))
    save(16, 169, fig)


def draw_test_17():
    fig, ax = diagram((-.5, 4.5), (-.4, 2.92))
    for x, voltage in [(0.65, 10), (2.0, 20), (3.35, 30)]:
        ax.plot([x, x], [0, 2.12], color=INK, linewidth=1.05)
        ax.text(x, 2.42, f"{voltage} V", ha="center")
    for name, x, y in [("P", 2.0, 1.77), ("Q", .65, 1.06), ("R", 2.0, .34)]:
        ax.scatter(x, y, color=INK, s=23, zorder=3)
        ax.text(x+.17, y, name, va="center", weight="bold")
    save(17, 19, fig)

    fig, ax = chart()
    i = np.linspace(0, 4, 161)
    ax.plot(i, i, color=INK, label="X")
    ax.plot(i, .55*i**2, color="#587489", linestyle="--", label="Y")
    ax.axvline(3, color="#777777", lw=.9, linestyle=":")
    ax.scatter([3, 3], [3, .55*9], color=INK, zorder=3)
    ax.legend(loc="upper left")
    ax.set(xlabel="Current (A)", ylabel="Voltage (V)", xlim=(0, 4.2), ylim=(0, 9.55))
    save(17, 21, fig)

    fig, ax = diagram((-2.45, 2.45), (-.45, 2.90))
    for y, xs, pairs in [(0.53, [-.85, 0, .85], True), (1.97, [-.42, .42], False)]:
        for x in xs:
            for dx, start, end in [(-.12, y-.25, y+.25)] + ([(.12, y+.25, y-.25)] if pairs else []):
                ax.annotate("", (x+dx, end), (x+dx, start), arrowprops={"arrowstyle":"->", "color":INK})
            ax.plot([x-.29, x+.29], [y-.36, y-.36], color=INK, lw=1.3)
    ax.text(1.44, .53, "Lower set", va="center")
    ax.text(1.44, 1.97, "Upper set", va="center")
    save(17, 82, fig)

    fig, ax = diagram((-4.65, 7.65), (-1.25, 1))
    ax.plot([-4.25, 7.25], [0, 0], color="#777777", lw=.85)
    for point, end, label in [(-1, -4.3, "−1"), (4, 7.3, "4")]:
        ax.annotate("", (end, 0), (point, 0), arrowprops={"arrowstyle":"->", "color":INK, "lw":2.4})
        ax.scatter(point, 0, color=INK, s=27, zorder=3)
        ax.text(point, -.58, label, ha="center", va="top")
    save(17, 176, fig)


if __name__ == "__main__":
    draw_test_16()
    draw_test_17()
