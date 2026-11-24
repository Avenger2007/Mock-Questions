"""Draw the original data-bearing figures for COMEDK Tests 14 and 15."""
import numpy as np
from matplotlib.patches import Circle, Rectangle

from tests_04_05_figures import INK, chart, diagram, polygon, save


def test_14_figures():
    fig, ax = chart()
    x = np.linspace(0, 3, 401)
    for sign in (1, -1):
        ax.plot(x, sign * .62 * np.sin(np.pi * x), color=INK,
                linestyle="-" if sign > 0 else "--")
    ax.axhline(0, color="#777777", linewidth=.7)
    ax.scatter([0, 1, 2, 3], [0] * 4, color=INK, zorder=3)
    ax.set(xlim=(-.16, 3.26), ylim=(-.94, .94), xlabel="Position on string",
           ylabel="Displacement", yticks=[], xticks=[0, 3], xticklabels=["Fixed end", "Fixed end"])
    save(14, 26, fig)

    fig, ax = diagram((-.45, 3.65), (-.45, 1.8))
    arrow = {"arrowstyle": "->", "color": INK, "lw": 2.3}
    ax.annotate("", (0, 1.45), (0, 0), arrowprops=arrow)
    ax.annotate("", (3.3, 0), (0, 0), arrowprops=arrow)
    ax.text(.13, 1.4, "Electric field", va="center")
    ax.text(1.7, -.25, "Propagation", ha="center")
    save(14, 54, fig)

    fig, ax = chart()
    polygon(ax, [(0, 0), (3, 0), (2, 2), (0, 3)])
    ax.set(xlabel="x", ylabel="y", xlim=(-.23, 3.65), ylim=(-.24, 3.65),
           xticks=range(4), yticks=range(4))
    save(14, 175, fig)

    fig, ax = chart()
    x = np.linspace(-7, 7, 501)
    ax.plot(x, np.arctan(x), color=INK, linewidth=1.9)
    for sign in (1, -1):
        ax.axhline(sign*np.pi/2, color="#587489", linestyle="--", linewidth=1)
    ax.axvline(0, color="#777777", linewidth=.7)
    ax.set(xlabel="x", ylabel="y", xlim=(-7, 7), ylim=(-1.9, 1.9),
           yticks=[-np.pi/2, 0, np.pi/2], yticklabels=["−π/2", "0", "π/2"])
    save(14, 180, fig)


def test_15_figures():
    fig, ax = chart()
    ax.plot([0, 3, 6], [-2, 4, 2], color=INK, marker="o", linewidth=1.8)
    ax.axhline(0, color="#777777", linewidth=.9)
    ax.set(xlabel="Time (s)", ylabel="Velocity (m/s)", xlim=(-.3, 6.4),
           ylim=(-2.5, 4.7), xticks=range(7), yticks=range(-2, 5, 2))
    save(15, 2, fig)

    fig, ax = diagram((-.5, 6.55), (-.4, 2.65))
    lines = [0, .6, 1.65, 3.35, 5.85]
    for i, x in enumerate(lines):
        ax.plot([x, x], [0, 1.9], color=INK, linewidth=1.05)
        ax.text(x, 2.09 + .28*(i % 2), f"{10*i} V", ha="center", fontsize=10)
    for name, x in [("P", .3), ("Q", 2.5), ("R", 4.6)]:
        ax.scatter(x, .88, color=INK, s=18)
        ax.text(x, .55, name, ha="center", weight="bold")
    save(15, 6, fig)

    fig, ax = chart()
    masses = [2, 4, 8, 16, 28, 56, 100, 170, 235]
    binding = [1.1, 7.1, 7.1, 7.9, 8.45, 8.8, 8.6, 8.15, 7.6]
    ax.plot(masses, binding, color=INK, lw=1.8)
    for x, y, label in [(4, 7.1, "A"), (28, 8.45, "B")]:
        ax.scatter(x, y, color=INK)
        ax.annotate(label, (x, y), xytext=(4, 6), textcoords="offset points")
    ax.set(xlabel="Mass number", ylabel="Binding/nucleon (MeV)", xlim=(0, 248), ylim=(0, 10))
    save(15, 22, fig)

    fig, ax = chart()
    t = np.linspace(0, 4, 501)
    wave = np.sin(np.pi*t)
    ax.plot(t, wave, color="#55748a", linestyle="--", label="Input")
    ax.plot(t, np.maximum(0, wave), color=INK, linewidth=1.8, label="Output")
    ax.legend(loc="lower left", ncol=2)
    ax.set(xlabel="Time (arbitrary units)", ylabel="Normalised voltage", ylim=(-1.6, 1.25))
    save(15, 58, fig)

    fig, ax = diagram((-1.65, 1.65), (-1.5, 1.66))
    for base, offset in [(0, 90), (1, 150)]:
        for alpha in np.deg2rad(offset + 120 * np.arange(3)):
            ux, uy = np.cos(alpha), np.sin(alpha)
            inner = .32 if base else 0
            ax.plot([inner*ux, 1.09*ux], [inner*uy, 1.09*uy], color=INK,
                    linestyle="--" if base else "-", lw=1.6)
            ax.text(1.27*ux, 1.27*uy, "H", ha="center", va="center")
    ax.add_patch(Circle((0, 0), .32, edgecolor=INK, facecolor="none"))
    ax.scatter(0, 0, color=INK, s=15)
    save(15, 65, fig)

    fig, ax = diagram((-2.35, 2.35), (-1.55, 1.55))
    ax.add_patch(Rectangle((-2.2, -1.36), 4.4, 2.72, fill=False, edgecolor=INK))
    for x, name in [(-.64, "A"), (.64, "B")]:
        ax.add_patch(Circle((x, 0), .98, fill=False, edgecolor=INK))
        ax.text(x, 1.10, name, ha="center")
    for x, y, value in [(-1, 0, "8"), (0, 0, "5"), (1, 0, "7"), (1.8, -1, "5"),
                        (-1.93, 1.1, "U")]:
        ax.text(x, y, value, ha="center")
    save(15, 134, fig)

    fig, ax = diagram((-2.5, 2.5), (-1.5, 1.74))
    left = [1.03, .36, -.31, -.98]
    right = [.8, .03, -.74]
    for x, values, labels in [(-2, left, "1234"), (2, right, "abc")]:
        for y, label in zip(values, labels):
            ax.add_patch(Circle((x, y), .155, fill=False, edgecolor=INK))
            ax.text(x, y, label, ha="center", va="center")
    for i, j in [(0, 0), (1, 0), (1, 1), (2, 2)]:
        ax.annotate("", (1.82, right[j]), (-1.82, left[i]),
                    arrowprops={"arrowstyle": "->", "color": INK, "lw": 1.1})
    save(15, 137, fig)

    fig, ax = chart()
    ax.axhline(0, color=INK, linewidth=.9)
    ax.axvline(0, color=INK, linewidth=.9)
    ax.plot(-2, 1, "o", color=INK)
    ax.annotate("z", (-2, 1), xytext=(6, 6), textcoords="offset points")
    ax.set(xlabel="Real axis", ylabel="Imaginary axis", xlim=(-3, 3), ylim=(-2, 2),
           xticks=range(-3, 4), yticks=range(-2, 3))
    save(15, 143, fig)


if __name__ == "__main__":
    test_14_figures()
    test_15_figures()
