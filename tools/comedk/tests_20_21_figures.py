"""Draw the original graphs and diagrams for COMEDK Tests 20 and 21."""
import numpy as np

from tests_04_05_figures import INK, chart, diagram, save
from tests_18_19_figures import mark

SECONDARY = "#59778b"


def draw_test_20():
    fig, ax = chart()
    ax.plot([0, 2, 7], [0, 6, 0], color=INK)
    for x, y, label in [(0, 0, "O"), (2, 6, "A"), (7, 0, "B")]:
        mark(ax, x, y, label, (-12, 7) if label == "B" else (5, 5))
    ax.set(xlabel="Time (s)", ylabel="Velocity (m/s)", xlim=(-.25, 7.4),
           ylim=(-.35, 7), xticks=[0, 2, 7], yticks=[0, 2, 4, 6])
    save(20, 2, fig)

    fig, ax = diagram((-2.1, 2.1), (-1.85, 1.85))
    sites = [(0, 1.48, "B"), (0, -1.48, "B"), (-1.57, 0, "A"),
             (1.57, 0, "A"), (-.85, -.64, "A"), (.85, .64, "A")]
    for x, y, label in sites:
        ax.plot([0, x], [0, y], '--' if x > 0 and y > 0 else '-', color=INK)
        ax.text(x, y, label, ha="center", va="center", bbox={"fc": "white", "ec": "none", "pad": 2})
    ax.text(0, 0, "M", ha="center", va="center", bbox={"fc": "white", "ec": "none", "pad": 2})
    save(20, 82, fig)

    fig, ax = chart()
    ax.plot([0, 1], [1, 2], color=INK, lw=1.6)
    ax.plot([1, 3.1], [2, 3.05], color=INK, lw=1.6)
    ax.scatter([1], [2], s=50, facecolor="white", edgecolor=INK, linewidth=1.4, zorder=4)
    ax.scatter([1], [4], s=38, color=INK, zorder=4)
    ax.set(xlabel="x", ylabel="f(x)", xlim=(-.2, 3.3), ylim=(.65, 4.55),
           xticks=range(4), yticks=range(1, 5))
    save(20, 127, fig)

    fig, ax = chart()
    xs = [0, 4, 4, 2, 0]
    ys = [0, 0, 2, 4, 3]
    ax.fill(xs, ys, fc="#e2ebf0", ec=INK, lw=1.5)
    ax.scatter(xs, ys, color=INK, zorder=3)
    ax.set(xlabel="x", ylabel="y", xlim=(-.25, 4.55), ylim=(-.25, 4.55),
           xticks=range(5), yticks=range(5))
    save(20, 157, fig)

    fig, ax = chart()
    x = np.linspace(-1, 1, 300)
    ax.plot(x, np.arcsin(x), color=INK, lw=1.7)
    ax.scatter([-1, 1], [-np.pi/2, np.pi/2], s=25, color=INK)
    ax.set(xlabel="x", ylabel="y", xlim=(-1.28, 1.28), ylim=(-1.94, 1.94),
           xticks=[-1, 0, 1], yticks=[-np.pi/2, 0, np.pi/2], yticklabels=["−π/2", "0", "π/2"])
    save(20, 162, fig)


def draw_test_21():
    fig, ax = chart()
    ax.axhline(0, color=INK, lw=.8)
    ax.plot([0, 1, 3, 4, 5], [0, 4, 0, -3, 0], color=INK, marker="o")
    ax.set(xlabel="Position (m)", ylabel="Force (N)", xlim=(-.25, 5.3), ylim=(-3.6, 4.6),
           xticks=range(6), yticks=[-3, 0, 4])
    save(21, 14, fig)

    fig, ax = chart()
    v = np.linspace(-4, 2, 400)
    for cutoff, color, style, label in [(-3, INK, "-", "X"), (-1, SECONDARY, "--", "Y")]:
        ax.plot(v, np.minimum(1, np.maximum(0, (v-cutoff)/3)), color=color, ls=style, lw=2, label=label)
    ax.axvline(-2, color="#a7b3bd", lw=1.1, linestyle=":")
    ax.legend(loc="upper left", ncol=2)
    ax.set(xlabel="Collector voltage (V)", ylabel="Photocurrent", ylim=(-.10, 1.19),
           xticks=range(-4, 3), yticks=[0])
    save(21, 18, fig)

    fig, ax = chart()
    ax.plot([0, 2.4], [0, 3.2], color=INK, lw=1.8)
    ax.plot([0, 3.4], [0, 2.1], color=SECONDARY, ls="--", lw=1.8)
    ax.text(2.47, 3.18, "X")
    ax.text(3.46, 2.1, "Y")
    ax.set(xlabel="Strain", ylabel="Stress", xlim=(-.07, 3.85), ylim=(-.1, 3.55), xticks=[], yticks=[])
    save(21, 23, fig)

    fig, ax = diagram((-2.6, 2.65), (-1.4, 1.5))
    ax.annotate("", (-1.95, 1.15), (-1.95, -1.05), arrowprops={"arrowstyle": "->", "color": INK})
    ax.text(-2.15, 0, "Energy", rotation=90, ha="right", va="center")
    for y, positions, label in [(0.63, [-.6, .55], r"$e_g$"), (-.63, [-1.13, -.03, 1.07], r"$t_{2g}$")]:
        for x in positions:
            ax.plot([x-.36, x+.36], [y, y], color=INK, lw=1.5)
            if y < 0:
                for dx, direction in [(-.12, 1), (.12, -1)]:
                    a, b = y+.05, y+.43
                    ax.annotate("", (x+dx, b if direction==1 else a), (x+dx, a if direction==1 else b),
                                arrowprops={"arrowstyle": "->", "color": INK, "shrinkA": 0, "shrinkB": 0})
        ax.text(1.73, y+.04, label, ha="left", va="center")
    save(21, 82, fig)

    fig, ax = diagram((-5.35, 6.35), (-.7, .75))
    ax.annotate("", (6.05, 0), (-5.12, 0), arrowprops={"arrowstyle": "->", "color": SECONDARY, "lw": .8})
    for x in [-2, 0, 3]:
        ax.plot([x, x], [-.10, .10], color=INK, lw=.9)
        ax.text(x, -.35, f"{x}".replace("-", "−"), ha="center", va="top")
    for x, edge, filled in [(-2, -5, False), (3, 5.9, True)]:
        ax.annotate("", (edge, 0), (x, 0), arrowprops={"arrowstyle": "->", "color": INK, "lw": 2.1})
        ax.scatter([x], [0], s=38, facecolor=INK if filled else "white", edgecolor=INK, zorder=3)
    save(21, 128, fig)

    fig, ax = diagram((-2.4, 2.4), (-1.65, 1.72))
    positions = [0.86, 0, -0.86]
    for x, symbols, title in [(-1.75, "123", "A"), (1.75, "pqr", "B")]:
        ax.text(x, 1.37, title, ha="center", weight="bold")
        for height, symbol in zip(positions, symbols):
            ax.text(x, height, symbol, ha="center", va="center",
                    bbox={"boxstyle": "circle,pad=.33", "fc": "white", "ec": INK})
    for source, target in [(0, 1), (1, 0), (2, 1)]:
        ax.annotate("", (1.49, positions[target]), (-1.49, positions[source]),
                    arrowprops={"arrowstyle": "->", "color": INK})
    save(21, 161, fig)

    fig, ax = chart()
    ax.axhline(0, color=INK, lw=.8)
    ax.axvline(0, color=INK, lw=.8)
    mark(ax, 2, 1, "z")
    ax.set(xlabel="Real axis", ylabel="Imaginary axis", xlim=(-3.2, 3.2), ylim=(-2.2, 2.2),
           xticks=range(-3, 4), yticks=range(-2, 3))
    save(21, 167, fig)

    fig, ax = diagram((-.55, 2.65), (-.50, 1.9))
    for endpoint, label, offset in [((2.3, 0), "u (+x)", (0, -15)), ((0, 1.55), "v (+y)", (5, 0))]:
        ax.annotate("", endpoint, (0, 0), arrowprops={"arrowstyle": "->", "color": INK, "lw": 1.9})
        ax.annotate(label, endpoint, xytext=offset, textcoords="offset points", ha="right" if offset[0]==0 else "left")
    ax.scatter(0, 0, s=13, color=INK)
    save(21, 171, fig)


if __name__ == "__main__":
    draw_test_20()
    draw_test_21()
