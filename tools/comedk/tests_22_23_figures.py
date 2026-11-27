"""Draw the original figures used by COMEDK Tests 22 and 23."""
import numpy as np
from matplotlib.patches import Circle

from tests_04_05_figures import INK, chart, diagram, polygon, save
from tests_18_19_figures import mark

SECONDARY = "#5c798c"


def test_22():
    fig, ax = chart()
    ax.plot([2, 4, 12, 25, 56, 86, 130, 184, 230],
            [1.1, 7.1, 7.5, 8.25, 8.8, 8.6, 8.37, 7.99, 7.6],
            color=INK, lw=1.6)
    mark(ax, 56, 8.8, "B", (-5, 10))
    mark(ax, 230, 7.6, "C", (-8, -17))
    ax.axhline(8.8, color=SECONDARY, ls=":", lw=.9)
    ax.axhline(7.6, color=SECONDARY, ls=":", lw=.9)
    ax.set(xlabel="Mass number", ylabel="Binding/nucleon (MeV)",
           xlim=(0, 250), ylim=(0, 10.2), yticks=[0, 2, 4, 6, 7.6, 8.8, 10])
    save(22, 3, fig)

    fig, ax = chart()
    ax.axhline(0, color=INK, lw=.8)
    ax.plot([0, 2, 3, 5], [0, 8, 8, -4], color=INK, lw=1.7, marker="o")
    ax.set(xlabel="Time (s)", ylabel="Force (N)", xlim=(-.25, 5.3),
           ylim=(-4.8, 9.1), xticks=range(6), yticks=[-4, 0, 4, 8])
    save(22, 35, fig)

    fig, ax = diagram((-1.95, 1.95), (-1.95, 2.08))
    sites = [(0, 1.46), (0, -1.46), (1.48, 0), (-1.48, 0), (.78, .77), (-.78, -.77)]
    for x, y in sites:
        ax.plot([0, x], [0, y], '--' if x > 0 and y > 0 else '-', color=INK, lw=1.4)
        ax.scatter(x, y, s=145, facecolor="white", edgecolor=INK, zorder=3)
    ax.text(0, 0, "M", ha="center", va="center",
            bbox={"fc": "white", "ec": "none", "pad": 2})
    ax.set_title("I", color=INK, pad=0)
    for (x, y), label in zip(sites, "XYXYXY"):
        ax.text(x, y, label, ha="center", va="center", zorder=4, fontsize=10)
    ax.set_position([.04, .08, .42, .79])
    ax2 = fig.add_axes([.54, .08, .42, .79], xlim=(-1.95, 1.95), ylim=(-1.95, 2.08), aspect="equal")
    ax2.axis("off")
    ax2.set_title("II", color=INK, pad=0)
    for (x, y), label in zip(sites, "XXYXYY"):
        ax2.plot([0, x], [0, y], '--' if x > 0 and y > 0 else '-', color=INK, lw=1.4)
        ax2.scatter(x, y, s=145, facecolor="white", edgecolor=INK, zorder=3)
        ax2.text(x, y, label, ha="center", va="center", zorder=4, fontsize=10)
    ax2.text(0, 0, "M", ha="center", va="center",
             bbox={"fc": "white", "ec": "none", "pad": 2})
    save(22, 82, fig)

    fig, ax = diagram((-3.1, 3.1), (-1.45, 1.7))
    points = [{1: .68, 2: -.68}, {"p": .80, "q": 0, "r": -.80}, {4: .63, 7: -.63}]
    centres = [-2.55, 0, 2.55]
    for x, coords, label in zip(centres, points, "ABC"):
        ax.text(x, 1.47, label, ha="center", va="center", weight="bold")
        for item, yy in coords.items():
            ax.add_patch(Circle((x, yy), .20, fill=False, edgecolor=INK))
            ax.text(x, yy, str(item), ha="center", va="center")
    for j, pairs in enumerate([[(1, "p"), (2, "r")], [("p", 4), ("q", 7), ("r", 4)]]):
        for source, target in pairs:
            ax.annotate("", (centres[j+1]-.22, points[j+1][target]),
                        (centres[j]+.22, points[j][source]),
                        arrowprops={"arrowstyle": "->", "color": INK})
        ax.text((centres[j]+centres[j+1])/2, 1.25, "fg"[j], ha="center")
    save(22, 137, fig)

    fig, ax = chart()
    polygon(ax, [(0, 0), (4, 0), (4, 3), (0, 2)])
    ax.set(xlabel="x", ylabel="y", xlim=(-.2, 4.7), ylim=(-.24, 3.62), xticks=range(5), yticks=range(4))
    save(22, 151, fig)

    fig, ax = chart()
    x = np.linspace(-9, 9, 350)
    ax.plot(x, np.arctan(x), color=INK, lw=1.7, label="X")
    ax.plot(x, np.arctan(x)+np.pi/2, "--", color=SECONDARY, lw=1.7, label="Y")
    for h in [-np.pi/2, 0, np.pi/2, np.pi]:
        ax.axhline(h, color="#a6b5bd", linestyle=":", lw=.75, zorder=0)
    ax.set(xlabel="x", ylabel="y", xlim=(-9, 9), ylim=(-1.82, 3.43),
           yticks=[-np.pi/2, 0, np.pi/2, np.pi], yticklabels=["−π/2", "0", "π/2", "π"])
    ax.legend(loc="upper left", ncol=2)
    save(22, 156, fig)


def test_23():
    fig, ax = chart()
    coords = [(0, 0), (2, 2), (3, 0), (5, 4)]
    ax.plot(*zip(*coords), color=INK, lw=1.7)
    for (x, y), title in zip(coords, "OABC"):
        mark(ax, x, y, title, (-12, 9) if title == "C" else (5, 6))
    ax.set(xlabel="Time (s)", ylabel="Position (m)", xlim=(-.23, 5.35),
           ylim=(-.29, 4.68), xticks=range(6), yticks=range(5))
    save(23, 11, fig)

    fig, ax = chart()
    ax.plot([-4, -2, 1, 2], [0, 0, 1, 1], color=INK, lw=1.8)
    ax.set(xlabel="Collector voltage (V)", ylabel="Photocurrent", xlim=(-4.25, 2.25),
           ylim=(-.10, 1.15), xticks=range(-4, 3), yticks=[0])
    save(23, 31, fig)

    fig, ax = chart()
    coords = [(0, 0), (1, 3), (3, 0), (4, -2), (6, -1)]
    ax.axhline(0, color=SECONDARY, lw=.9)
    ax.plot(*zip(*coords), color=INK, lw=1.6)
    for (x, y), label in zip(coords, "ABCDE"):
        mark(ax, x, y, label, (-11, 6) if label == "E" else (6, 6))
    ax.set(xlabel="Time (s)", ylabel="Velocity (m/s)", xlim=(-.24, 6.25),
           ylim=(-2.38, 3.6), xticks=range(7), yticks=range(-2, 4))
    save(23, 50, fig)

    fig, ax = diagram((-3.5, 3.65), (-1.37, 1.62))
    for centre, legend, singles in [(-1.85, "I", False), (1.85, "II", True)]:
        ax.text(centre, 1.30, legend, weight="bold", ha="center")
        for y, offsets in [(0.55, [-.51, .51]), (-.62, [-.91, 0, .91])]:
            for j, dx in enumerate(offsets):
                x = centre+dx
                ax.plot([x-.34, x+.34], [y, y], color=INK, lw=1.5)
                arrows = ([(-.11, 1), (.11, -1)] if y < 0 and (not singles or j == 0)
                          else [(0, 1)] if singles else [])
                for dz, sense in arrows:
                    up, low = y+.38, y+.05
                    ax.annotate("", (x+dz, up if sense == 1 else low),
                                (x+dz, low if sense == 1 else up),
                                arrowprops={"arrowstyle": "->", "color": INK, "shrinkA": 0, "shrinkB": 0})
    save(23, 82, fig)

    fig, ax = diagram((-1.95, 3.25), (-1.58, 1.74))
    for theta in np.deg2rad([90, 210, 330]):
        dx, dy = np.cos(theta), np.sin(theta)
        ax.plot([.29*dx, 1.10*dx], [.29*dy, 1.10*dy], color=SECONDARY, ls="--", lw=3.5)
        ax.plot([0, 1.03*dx], [0, 1.03*dy], color=INK, lw=1.35)
        ax.text(1.32*dx, 1.32*dy, "H", ha="center", va="center")
    ax.add_patch(Circle((0, 0), .29, fill=False, edgecolor=SECONDARY, lw=1.2))
    ax.scatter([0], [0], color=INK, s=22)
    ax.plot([1.4, 1.83], [.85, .85], color=INK, lw=1.35)
    ax.text(1.96, .85, "Front bonds", va="center", fontsize=10)
    ax.plot([1.4, 1.83], [.38, .38], color=SECONDARY, ls="--", lw=3)
    ax.text(1.96, .38, "Rear bonds", va="center", fontsize=10)
    save(23, 95, fig)

    fig, ax = chart()
    polygon(ax, [(0, 0), (3, 0), (3, 2), (0, 4)])
    for old, new, xy in zip(ax.texts, "OPQR", [(0, 0), (3, 0), (3, 2), (0, 4)]):
        old.remove()
        ax.annotate(new, xy, xytext=(6, 4), textcoords="offset points")
    ax.set(xlabel="x", ylabel="y", xlim=(-.2, 3.7), ylim=(-.25, 4.62), xticks=range(4), yticks=range(5))
    save(23, 142, fig)


if __name__ == "__main__":
    test_22()
    test_23()
