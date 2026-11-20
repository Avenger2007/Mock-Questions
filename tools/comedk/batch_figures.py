"""Draw the original figures for COMEDK Tests 2 and 3."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

OUTPUT = Path(__file__).resolve().parents[2] / "COMEDK" / "images"
INK = "#153049"
ACCENT = "#176568"
plt.rcParams.update({"font.size": 13, "axes.labelcolor": INK, "text.color": INK})


def save(test, question, fig):
    fig.savefig(OUTPUT / f"COMEDK_T{test:02}_Q{question:03}.png", dpi=190,
                bbox_inches="tight", pad_inches=0.13, facecolor="white")
    plt.close(fig)


def plot():
    fig, ax = plt.subplots(figsize=(5.3, 2.65))
    ax.grid(color="#d7e2e5", alpha=0.7)
    ax.set_axisbelow(True)
    return fig, ax


def diagram(x, y):
    fig, ax = plt.subplots(figsize=(5.0, 2.6))
    ax.set(xlim=x, ylim=y, aspect="equal")
    ax.axis("off")
    return fig, ax


fig, ax = plot()
t = np.linspace(0, 1, 300)
ax.plot(t, np.cos(2 * np.pi * t), lw=2.8, color=ACCENT)
ax.axhline(0, color=INK, lw=1)
ax.set(xlabel="Time", ylabel="Displacement", xlim=(0, 1), ylim=(-1.18, 1.18),
       xticks=[0, .25, .5, .75, 1], xticklabels=["0", "T/4", "T/2", "3T/4", "T"],
       yticks=[-1, 0, 1], yticklabels=["−A", "0", "+A"])
save(2, 20, fig)

fig, ax = diagram((-1, 5), (-0.1, 3.25))
for x, start, end, label in [(1, .8, 2.6, "3 A"), (3, 2.6, .8, "6 A")]:
    ax.plot([x, x], [.65, 2.8], lw=3, color=INK, alpha=.45)
    ax.annotate("", xy=(x, end), xytext=(x, start),
                arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=2.5))
    ax.text(x + .2, 1.9, label)
ax.annotate("", xy=(1, .44), xytext=(3, .44),
            arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
ax.text(2, .13, "d", ha="center")
save(2, 54, fig)

fig, ax = diagram((-2.4, 2.4), (-1.65, 1.65))
for x, y, label in [(0, 1.16, "Cl"), (0, -1.16, "Cl"), (1.6, .55, "A"),
                    (-1.6, -.55, "A"), (1.6, -.55, "A"), (-1.6, .55, "A")]:
    ax.plot([0, x], [0, y], color=INK, lw=2,
            ls="--" if x and y > 0 else "-")
    ax.text(x, y, label, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=.2", fc="white", ec="none"))
ax.text(0, 0, "M", ha="center", va="center",
        bbox=dict(boxstyle="circle,pad=.25", fc="#e3f0f0", ec=ACCENT))
save(2, 82, fig)

fig, ax = diagram((-2.35, 2.35), (-1.31, 1.31))
for x, label, color in [(-.68, "A", ACCENT), (.68, "B", INK)]:
    ax.add_patch(Circle((x, 0), 1.04, fc="none", ec=color, lw=2))
    ax.text(x, 1.08, label, ha="center")
for x, label in [(-1.13, "13"), (0, "12"), (1.13, "18")]:
    ax.text(x, 0, label, ha="center", va="center")
save(2, 146, fig)

fig, ax = plot()
ax.plot([2, 5], [8, 2], color=ACCENT, lw=2.6, marker="o")
ax.set(xlabel="Time (s)", ylabel="Position (m)", xlim=(1.6, 5.4), ylim=(0, 9),
       xticks=[2, 3, 4, 5], yticks=[0, 2, 4, 6, 8])
save(3, 11, fig)

fig, ax = plot()
ax.plot([0, 3], [-2, 4], color=ACCENT, lw=2.6, marker="o")
ax.axhline(0, color=INK, lw=1)
ax.set(xlabel="Time (s)", ylabel="Velocity (m/s)", xlim=(-.15, 3.15), ylim=(-2.5, 4.55),
       xticks=[0, 1, 2, 3], yticks=[-2, 0, 2, 4])
save(3, 50, fig)

fig, ax = diagram((-2.25, 2.25), (-1.65, 1.65))
for x, y in [(0, 1.18), (0, -1.18), (1.5, .55), (1.5, -.55)]:
    ax.plot([0, x], [0, y], color=INK, lw=2, ls="--" if x and y > 0 else "-")
    ax.add_patch(Circle((x, y), .13, ec=INK, fc="white", lw=2, zorder=3))
ax.plot([0, -1.35], [0, 0], color=INK, lw=1.5, ls=":")
ax.scatter([-1.51, -1.51], [-.09, .09], color=ACCENT, s=25)
ax.add_patch(Circle((0, 0), .17, fc=ACCENT, ec=INK, zorder=3))
save(3, 104, fig)

fig, ax = plot()
x, y = [0, 5, 3, 0, 0], [0, 0, 4, 5, 0]
ax.fill(x, y, color="#dbeceb")
ax.plot(x, y, color=ACCENT, lw=2, marker="o")
for vx, vy, label, offset in zip(x, y, "ABCD", [(6, 4), (0, 7), (10, 0), (8, 2)]):
    ax.annotate(label, (vx, vy), xytext=offset, textcoords="offset points")
ax.set(xlabel="x", ylabel="y", xlim=(-.25, 5.65), ylim=(-.25, 5.7),
       xticks=range(6), yticks=range(6))
save(3, 151, fig)
