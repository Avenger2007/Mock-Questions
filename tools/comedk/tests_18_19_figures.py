"""Draw the original data-bearing figures for COMEDK Tests 18 and 19."""
import numpy as np
from matplotlib.patches import Arc, Circle

from tests_04_05_figures import INK, chart, diagram, polygon, save


def mark(ax, x, y, label, offset=(5, 6)):
    ax.scatter(x, y, color=INK, s=20, zorder=3)
    ax.annotate(label, (x, y), xytext=offset, textcoords="offset points")


def draw_test_18():
    fig, ax = chart()
    t = np.linspace(0, 4, 160)
    ax.plot(t, 3 - .42*(t-2)**2, color=INK, label="X")
    ax.plot(t, 1.8 + .6*t, '--', color="#587489", label="Y")
    mark(ax, 2, 3, "P")
    ax.legend(loc="lower right")
    ax.set(xlabel="Time", ylabel="Position", xlim=(0, 4), ylim=(1.1, 4.5), xticks=[], yticks=[])
    save(18, 11, fig)

    fig, ax = chart()
    angle = np.linspace(0, 180, 200)
    ax.plot(angle, np.sin(np.deg2rad(angle)), color=INK, lw=1.8)
    ax.axvline(90, color="#587489", linestyle="--", lw=.9)
    mark(ax, 90, 1, "Peak")
    ax.set(xlabel="Angle between moment and field (°)", ylabel="Torque magnitude",
           xticks=[0, 45, 90, 135, 180], yticks=[], ylim=(0, 1.24))
    save(18, 37, fig)

    fig, ax = chart()
    ax.plot([0, 2, 5], [1, 5, 2], color=INK, lw=1.7, marker="o")
    ax.axvline(2, color="#587489", linestyle="--", lw=.8)
    ax.text(1, .35, "First interval", ha="center")
    ax.text(3.5, .35, "Second interval", ha="center")
    ax.set(xlabel="Time (s)", ylabel="Velocity (m/s)", ylim=(0, 5.65), xticks=[0, 2, 5])
    save(18, 50, fig)

    fig, ax = chart()
    ax.plot([0, .75], [150, 92], color=INK, lw=1.7)
    ax.scatter([.17,.34,.62], [150-58*x/.75 for x in [.17,.34,.62]], color=INK)
    ax.set(xlabel="Square root of concentration", ylabel="Molar conductivity",
           xlim=(0, .8), ylim=(80, 163), xticks=[], yticks=[])
    save(18, 63, fig)

    fig, ax = diagram((-2.1, 2.1), (-1.8, 1.8))
    ends = [(0, 1.32, "X", False), (1.38, 0, "X", False), (.81, -.86, "X", False),
            (0, -1.32, "Y", True), (-1.38, 0, "Y", True), (-.81, .86, "Y", True)]
    for x, y, label, rear in ends:
        ax.plot([0, x], [0, y], '--' if rear else '-', color=INK, lw=1.3, zorder=1)
        ax.add_patch(Circle((x, y), .17, facecolor="white", edgecolor=INK, zorder=3))
        ax.text(x, y, label, ha="center", va="center", zorder=4)
    ax.add_patch(Circle((0, 0), .17, facecolor="white", edgecolor=INK, zorder=3))
    ax.text(0, 0, "M", ha="center", va="center", zorder=4)
    save(18, 82, fig)

    fig, ax = chart()
    x = np.linspace(0, 1.45, 160)
    ax.plot([-2, 0], [-2, 0], color=INK, lw=1.7)
    ax.plot(x, x+x*x, color=INK, lw=1.7)
    ax.plot([-.65,.65], [-.65,.65], '--', color="#6d8390", lw=1)
    mark(ax, 0, 0, "Join", (5, -13))
    ax.set(xlabel="x", ylabel="y", ylim=(-2.2, 4))
    save(18, 133, fig)

    fig, ax = diagram((-2.55, 2.55), (-1.5, 1.56))
    heights = [.9, 0, -.9]
    for x, labels in [(-2, "123"), (2, "abc")]:
        for y, label in zip(heights, labels):
            ax.add_patch(Circle((x, y), .16, fill=False, edgecolor=INK))
            ax.text(x, y, label, ha="center", va="center")
    for i,j in [(0,0), (1,1), (2,1)]:
        ax.annotate("", (1.80, heights[j]), (-1.80, heights[i]),
                    arrowprops={"arrowstyle":"->", "color":INK})
    save(18, 149, fig)

    fig, ax = chart()
    ax.axhline(0, color=INK, lw=.8)
    ax.axvline(0, color=INK, lw=.8)
    mark(ax, 0, -3, "z")
    ax.set(xlabel="Real axis", ylabel="Imaginary axis", xlim=(-3.5,3.5), ylim=(-3.6,2),
           xticks=range(-3,4), yticks=[-3,-2,-1,0,1,2])
    save(18, 155, fig)

    fig, ax = chart()
    polygon(ax, [(0, 1), (3, 0), (4, 3), (0, 4)])
    ax.set(xlabel="x", ylabel="y", xlim=(-.18,4.65), ylim=(-.2,4.65), xticks=range(5), yticks=range(5))
    save(18, 163, fig)

    fig, ax = chart()
    x = np.linspace(-1,1,300)
    ax.plot(x, np.arccos(x), color=INK, lw=1.7)
    ax.axvline(0, color="#607989", lw=.8)
    ax.scatter([-1,0,1], [np.pi,np.pi/2,0], color=INK, s=18)
    ax.set(xlabel="x", ylabel="y", xlim=(-1.16,1.19), ylim=(-.2,3.35),
           xticks=[-1,0,1], yticks=[0,np.pi/2,np.pi], yticklabels=["0","π/2","π"])
    save(18, 168, fig)


def draw_test_19():
    fig, ax = diagram((-.4, 2.58), (-1.3, 1.35))
    ax.add_patch(Arc((0,0), 4,4, theta1=-38, theta2=38, color=INK, lw=1.7))
    ax.plot([0,2], [0,0], '--', color="#587489", lw=1)
    mark(ax, 0, 0, "S", (0,8))
    mark(ax, 2, 0, "P", (6,5))
    ax.text(1.63, 1.16, "Wavefront", ha="right")
    save(19, 3, fig)

    fig, ax = diagram((-.1, 4.3), (-.45, 2.45))
    for x, label in [(1.0, "12 V"), (3.0, "30 V")]:
        y = np.linspace(0,2,100)
        ax.plot(x+.22*(y-1)**2,y,color=INK,lw=1.3)
        ax.text(x+.22,2.23,label,ha="center")
    for x0, y, label in [(1,.5,"P"),(1,1.5,"Q"),(3,1.25,"R")]:
        mark(ax, x0+.22*(y-1)**2,y,label)
    save(19, 33, fig)

    fig, ax = diagram((-1.66, 2.05), (-1.70, 1.38))
    ax.add_patch(Circle((0,0),1,fill=False,edgecolor=INK,lw=1.5))
    ax.scatter(0,0,color=INK,s=12)
    ax.add_patch(Circle((0,0),.13,fill=False,edgecolor=INK))
    ax.annotate("", (.87,.49),(1,.28),arrowprops={"arrowstyle":"->","color":INK,"lw":1.4})
    ax.text(0,-1.28,"Current out of page",ha="center")
    ax.text(1.38,.79,"Path",ha="left")
    save(19, 36, fig)

    fig, ax = chart()
    mass = [2, 4, 12, 25, 56, 85, 125, 180, 230]
    energy = [1.1, 7.1, 7.5, 8.3, 8.8, 8.65, 8.43, 8.03, 7.6]
    ax.plot(mass,energy,color=INK,lw=1.6)
    for x,y,label in [(12,7.5,"A"),(56,8.8,"B"),(230,7.6,"C")]:
        mark(ax,x,y,label)
    ax.set(xlabel="Mass number", ylabel="Binding/nucleon (MeV)", xlim=(0,251),ylim=(0,10),
           xticks=[0,50,100,150,200,250],yticks=range(0,11,2))
    save(19, 49, fig)

    fig, ax = chart()
    x = np.linspace(-1,3,150)
    ax.plot(x,2+4*((x+1)/4)**1.5,color=INK,lw=1.7)
    for px,py,label,offset in [(-1,2,"(−1, 2)",(6,-13)),(3,6,"(3, 6)",(-39,6))]:
        mark(ax,px,py,label,offset)
    ax.set(xlabel="x",ylabel="f(x)",xlim=(-1.45,3.45),ylim=(1,6.8),
           xticks=range(-1,4),yticks=range(2,7))
    save(19, 128, fig)


if __name__ == "__main__":
    draw_test_18()
    draw_test_19()
