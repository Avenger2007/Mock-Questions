"""Draw the data-bearing figures for COMEDK Tests 4 and 5."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse

OUT = Path(__file__).resolve().parents[2] / "COMEDK" / "images"
INK = "#122d40"
plt.rcParams.update({"font.size": 12, "text.color": INK, "axes.labelcolor": INK})


def save(test, question, fig):
    fig.savefig(OUT / f"COMEDK_T{test:02}_Q{question:03}.png",
                dpi=200, bbox_inches="tight", pad_inches=.19, facecolor="white")
    plt.close(fig)


def chart():
    fig, ax = plt.subplots(figsize=(5.3, 2.55))
    ax.grid(color="#dddddd")
    ax.set_axisbelow(True)
    return fig, ax


def diagram(xlim, ylim):
    fig, ax = plt.subplots(figsize=(4.7, 2.5))
    ax.set(xlim=xlim, ylim=ylim, aspect="equal")
    ax.axis("off")
    return fig, ax


def polygon(ax, vertices):
    xs, ys = zip(*vertices)
    ax.fill(xs, ys, facecolor="white", edgecolor=INK, hatch="...", linewidth=1.4)
    ax.scatter(xs, ys, color=INK, s=24, zorder=3)
    for label, (x, y) in zip("ABCD", vertices):
        ax.annotate(label, (x, y), xytext=(7, 3), textcoords="offset points")


def main():
    fig, ax = chart()
    v = np.array([-.6, -.4, -.2, 0, .25, .4, .48, .54, .6, .66, .7])
    i = [-.04, -.04, -.03, 0, .03, .10, .22, .48, 1.2, 2.65, 4.5]
    ax.plot(v, i, color=INK, lw=2)
    ax.axhline(0, color="black", lw=.8)
    ax.axvline(0, color="black", lw=.8)
    for label, x, y in [("P", -.4, -.04), ("Q", .4, .10), ("R", .66, 2.65)]:
        ax.scatter(x, y, color=INK, zorder=3)
        ax.annotate(label, (x, y), xytext=(6, 7), textcoords="offset points")
    ax.set(xlabel="Diode voltage (V)", ylabel="Current (mA)", xlim=(-.65, .76), ylim=(-.6, 4.9))
    save(4, 36, fig)

    fig, ax = chart()
    ax.plot([1, 3], [10, 6], color=INK, lw=2, marker="o")
    ax.annotate("P", (1, 10), xytext=(6, 3), textcoords="offset points")
    ax.annotate("Q", (3, 6), xytext=(6, 3), textcoords="offset points")
    ax.set(xlabel="Current (A)", ylabel="Terminal voltage (V)", xticks=[1, 2, 3],
           yticks=[6, 7, 8, 9, 10], xlim=(.72, 3.35), ylim=(5.35, 10.55))
    save(4, 55, fig)

    fig, ax = diagram((-1.85, 1.85), (-1.55, 1.55))
    for dx, dy, angle in [(.63, .60, 45), (-.63, -.60, 45),
                          (.63, -.60, -45), (-.63, .60, -45)]:
        ax.add_patch(Ellipse((dx, dy), 1.40, .56, angle=angle, fill=False,
                            edgecolor=INK, linewidth=2, linestyle="-" if dx*dy>0 else "--"))
    ax.annotate("", (1.65, 0), (-1.51, 0), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", (0, 1.40), (0, -1.40), arrowprops=dict(arrowstyle="->"))
    ax.text(1.70, -.07, "x")
    ax.text(.07, 1.40, "y")
    save(4, 80, fig)

    fig, ax = chart()
    polygon(ax, [(0,0), (4,0), (3,2), (0,3)])
    ax.set(xlabel="x", ylabel="y", xlim=(-.25, 4.8), ylim=(-.25, 3.55),
           xticks=range(5), yticks=range(4))
    save(4, 142, fig)

    fig, ax = chart()
    ax.axhline(0,color="black",lw=.8)
    ax.plot([0, 6], [-4, 8], color=INK, lw=2, marker="o")
    ax.set(xlabel="Time (s)", ylabel="Velocity (m/s)", xlim=(-.25,6.3), ylim=(-5,9),
           xticks=range(7), yticks=range(-4,9,2))
    save(5, 2, fig)

    fig, ax = diagram((-1.6, 2.4), (-1.35, 1.35))
    for radius, style in [(.55,'-'), (.85,'--'), (1.18,'-')]:
        ax.add_patch(Circle((0, 0), radius, fill=False, edgecolor=INK, lw=1.7, ls=style))
    ax.plot(0,0,'.',color=INK)
    ax.annotate("+Q", xy=(-.53,.15), xytext=(-1.47,.64),
                arrowprops=dict(arrowstyle="-", color=INK))
    ax.annotate("−2Q", xy=(.92,.74), xytext=(1.28,1.03),
                arrowprops=dict(arrowstyle="-", color=INK))
    ax.annotate("Gaussian surface", xy=(.54,-.66), xytext=(1.2,-.83),
                arrowprops=dict(arrowstyle="-", color=INK))
    save(5, 19, fig)

    fig, ax = diagram((-2.22,2.62), (-1.42,1.55))
    for x, y, symbol in [(0,0,"C"),(0,1,"O"),(-1.35,-.64,"O"),(1.35,-.64,"O")]:
        ax.text(x,y,symbol,ha="center",va="center",fontsize=19)
    ax.plot([-.064,-.064],[.2,.80],color=INK,lw=1.5)
    ax.plot([.064,.064],[.2,.80],color=INK,lw=1.5)
    for direction in [-1,1]:
        ax.plot([direction*.23,direction*1.14],[-.12,-.54],color=INK,lw=1.5)
        ax.scatter([direction*1.3,direction*1.40,direction*1.3,direction*1.40,
                    direction*1.63,direction*1.63],[-.28,-.28,-1.0,-1.0,-.59,-.70],s=10,color=INK)
        ax.scatter([direction*.27,direction*.27],[.95,1.06],s=10,color=INK)
    ax.annotate("Marked",xy=(1.54,-.43),xytext=(1.76,.34),arrowprops=dict(arrowstyle="->"))
    save(5, 86, fig)

    fig, ax = chart()
    polygon(ax, [(5,0), (2,3), (5,3)])
    xs = np.array([.4, 5.7])
    ax.plot(xs, 5-xs, ls="--", color=INK, lw=1.4)
    ax.text(.20, 4.88, "x+y=5")
    ax.set(xlabel="x", ylabel="y", xlim=(-.2,6), ylim=(-.4,5.4),
           xticks=range(6), yticks=range(6))
    save(5, 145, fig)


if __name__ == "__main__":
    main()
