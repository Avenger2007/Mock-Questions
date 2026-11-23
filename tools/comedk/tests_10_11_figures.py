"""Draw the original data-bearing COMEDK Tests 10 and 11 figures."""
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch

from tests_04_05_figures import chart, diagram, polygon, save, INK


def main():
    fig, ax = chart()
    ax.plot([1, 5], [1, 13], marker="o", color=INK, lw=2)
    ax.annotate("A", (1, 1), xytext=(7, 5), textcoords="offset points")
    ax.annotate("B", (5, 13), xytext=(7, 5), textcoords="offset points")
    ax.set(xlabel="Time (s)", ylabel="Velocity (m/s)", xlim=(0, 5.8), ylim=(0,14.5),
           xticks=range(6), yticks=[0,1,4,7,10,13])
    save(10, 2, fig)

    fig, ax = chart()
    i = np.linspace(0, 4, 100)
    ax.plot(i, 1.2*i, color=INK)
    ax.plot(i, .65*i*i, color=INK, linestyle="--")
    ax.text(3.58, 4.63, "X")
    ax.text(3.56, 9.18, "Y")
    ax.set(xlabel="Current (A)", ylabel="Voltage (V)", xlim=(0,4.4), ylim=(0,11))
    save(10, 40, fig)

    fig, ax = diagram((-2.7,2.7), (-1.45,1.40))
    for x, colour, label, stage in [(-1.6,"#f7d85b","Yellow","Before"),
                                    (1.6,"#ee9338","Orange","After")]:
        ax.add_patch(FancyBboxPatch((x-.4,-.88),.8,1.2,
                                  boxstyle="round,pad=.02,rounding_size=.25",
                                  facecolor=colour,edgecolor="none"))
        ax.plot([x-.42,x-.42,x-.26,x+.26,x+.42,x+.42],
                [.73,-.7,-.92,-.92,-.7,.73],color=INK,lw=1.7)
        ax.text(x,.99,stage,ha="center")
        ax.text(x,-1.22,label,ha="center")
    ax.annotate("",xy=(.65,.18),xytext=(-.65,.18),arrowprops=dict(arrowstyle="->",color=INK))
    save(10, 81, fig)

    fig, ax = chart()
    polygon(ax, [(0,2),(2,0),(5,0),(0,5)])
    ax.set(xlabel="x",ylabel="y",xlim=(-.25,5.7),ylim=(-.25,5.7),
           xticks=range(6),yticks=range(6))
    save(10, 124, fig)

    fig, ax = chart()
    x = np.linspace(-3,3,280)
    y = np.sqrt(np.maximum(0,9-x*x))
    ax.plot(x,y,color=INK,lw=1.9)
    ax.fill_between(x,y,where=x>=0,color="#c9dce6")
    ax.axhline(0,color=INK,lw=.7)
    ax.axvline(0,color=INK,lw=.7)
    ax.set(xlabel="x",ylabel="y",xlim=(-3.4,3.4),ylim=(-.25,3.45),
           xticks=range(-3,4),yticks=range(4))
    save(10, 145, fig)

    fig, ax = chart()
    ax.plot([0,.001,.002],[0,200,400],color=INK,marker="o")
    ax.set(xlabel="Strain",ylabel="Stress (MPa)",xlim=(0,.00225),ylim=(0,442),
           xticks=[0,.001,.002],yticks=[0,100,200,300,400])
    save(11, 23, fig)

    fig, ax = diagram((-5.8,5.8),(-3.05,3.05))
    for x, label, seq in [(-3.85,"P","RLRR"),(0,"Q","LRLL"),(3.85,"R","RRRR")]:
        ax.text(x,2.73,label,ha="center",fontweight="bold")
        ax.text(x,2.18,"CHO",ha="center")
        ax.text(x,-2.45,"CH₂OH",ha="center")
        ax.plot([x,x],[-2.17,1.92],color=INK,lw=1.2)
        for y, side in zip([1.32,.42,-.48,-1.38],seq):
            ax.plot([x-.58,x+.58],[y,y],color=INK,lw=1.2)
            ax.text(x-.69,y,"OH" if side=="L" else "H",ha="right",va="center")
            ax.text(x+.69,y,"OH" if side=="R" else "H",ha="left",va="center")
    save(11, 90, fig)

    fig, ax = chart()
    polygon(ax,[(0,0),(4,0),(3,4),(0,5)])
    x = np.linspace(1.35,4.12,70)
    ax.plot(x,8-2*x,color=INK,ls="--",lw=1.2)
    ax.text(1.22,5.42,"2x+y=8",fontsize=10)
    ax.set(xlabel="x",ylabel="y",xlim=(-.25,4.7),ylim=(-.25,5.95),
           xticks=range(5),yticks=range(6))
    save(11, 127, fig)

    fig, ax = chart()
    ax.axhline(0,color=INK,lw=.8)
    ax.plot([.5,3.5],[-1.5,1.5],color=INK,lw=2)
    ax.scatter(2,0,color=INK,zorder=5)
    ax.set(xlabel="x",ylabel="f′(x)",xlim=(.4,3.6),ylim=(-1.65,1.65),
           xticks=[1,2,3],yticks=[-1,0,1])
    save(11, 138, fig)


if __name__ == "__main__":
    main()
