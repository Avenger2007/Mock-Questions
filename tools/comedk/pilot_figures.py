"""Render the four data-bearing figures for Test 1."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parents[2] / "COMEDK" / "images"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 13, "font.family": "DejaVu Sans"})


def save(fig, number):
    fig.savefig(OUT / f"COMEDK_T01_Q{number:03}.png", dpi=180, facecolor="white")
    plt.close(fig)


fig, ax = plt.subplots(figsize=(5.5, 2.55), layout="constrained")
ax.plot([0, 2, 5], [4, 4, 0], color="black", marker="o")
ax.set(xlabel="Position x (m)", ylabel="Force F (N)", xlim=(-0.16, 5.5),
       ylim=(-0.16, 4.9), xticks=[0, 2, 5], yticks=[0, 4])
ax.spines[["top", "right"]].set_visible(False)
ax.grid(True, linestyle=":", color="#777777")
save(fig, 14)

fig, ax = plt.subplots(figsize=(5.5, 2.1), layout="constrained")
ax.axis("off")
table = ax.table(cellText=[["X", "0.85"], ["Y", "0.95"]],
                 colLabels=["Ray", "Sine of incidence angle"], loc="center",
                 cellLoc="center", colWidths=[0.24, 0.56])
table.auto_set_font_size(False)
table.set_fontsize(13)
table.scale(1, 2.0)
save(fig, 55)

fig, ax = plt.subplots(figsize=(5.5, 2.1), layout="constrained")
ax.axis("off")
table = ax.table(cellText=[["1", "c", "d", "r"], ["2", "2c", "d", "2r"],
                           ["3", "2c", "2d", "8r"]],
                 colLabels=["Run", "[A]", "[B]", "Initial rate"],
                 loc="center", cellLoc="center", colWidths=[0.16, 0.21, 0.21, 0.24])
table.auto_set_font_size(False)
table.set_fontsize(13)
table.scale(1, 1.85)
save(fig, 109)

fig, ax = plt.subplots(figsize=(5.5, 2.1), layout="constrained")
ax.axis("off")
table = ax.table(cellText=[[1, 1, 0], [1, 1, 1], [0, 1, 1]], rowLabels=[1, 2, 3],
                 colLabels=[1, 2, 3], loc="center", cellLoc="center",
                 colWidths=[0.16, 0.16, 0.16])
table.auto_set_font_size(False)
table.set_fontsize(13)
table.scale(1, 1.8)
save(fig, 121)
