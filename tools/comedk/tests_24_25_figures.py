"""Draw the original figures for COMEDK Tests 24 and 25."""
import numpy as np
from matplotlib.patches import Circle

from tests_04_05_figures import INK, chart, diagram, polygon, save
from tests_18_19_figures import mark

SECONDARY = "#597b91"
ARROW = {"arrowstyle": "->", "color": INK, "lw": 1.2}


def plotted_polygon(test, question, vertices):
    fig, ax = chart()
    polygon(ax, vertices)
    ax.set(xlabel="x", ylabel="y", xlim=(-.25, max(x for x, y in vertices)+.7),
           ylim=(-.25, 4.65), xticks=range(max(x for x, y in vertices)+1), yticks=range(5))
    save(test, question, fig)


def arrow_diagram(test, question, left, right, pairs):
    fig, ax = diagram((-2.55, 2.55), (-1.73, 1.94))
    left_height = np.linspace(.95, -.95, len(left))
    right_height = np.linspace(1.1, -1.1, len(right))
    for x, symbols, heights, name in [(-1.9, left, left_height, "A"),
                                    (1.9, right, right_height, "B")]:
        ax.text(x, 1.62, name, ha="center", weight="bold")
        for symbol, y in zip(symbols, heights):
            ax.add_patch(Circle((x, y), .18, ec=INK, fc="white", zorder=3))
            ax.text(x, y, symbol, ha="center", va="center", zorder=4)
    for source, target in pairs:
        ax.annotate("", (1.69, right_height[target]), (-1.69, left_height[source]), arrowprops=ARROW)
    save(test, question, fig)


def draw_test_24():
    fig, ax = chart()
    x = np.linspace(0, 3.5, 200)
    ax.plot(x, x, color=INK, label="P")
    ax.plot([0, 1, 2, 3, 3.5], [0, .2, 1, 3, 4.4], "--", color=SECONDARY, label="Q")
    ax.set(xlabel="Voltage (V)", ylabel="Current (A)", xlim=(-.09, 3.65),
           ylim=(-.15, 4.65), xticks=[0,1,2,3], yticks=range(5))
    ax.legend()
    save(24, 1, fig)

    fig, ax = chart()
    xs, ys = [2, 4, 12, 32, 56, 110, 156, 225], [1.1, 7.1, 7.5, 8.35, 8.8, 8.5, 8.18, 7.65]
    ax.plot(xs, ys, color=INK, lw=1.6)
    mark(ax, 12, 7.5, "L", (7, -14))
    mark(ax, 110, 8.5, "R", (6, 8))
    ax.hlines([7.5, 8.5], [0, 0], [12, 110], colors=SECONDARY, linestyles=":")
    ax.set(xlabel="Mass number", ylabel="Binding/nucleon (MeV)", xlim=(0, 240),
           ylim=(0, 9.9), yticks=[0, 2, 4, 6, 7.5, 8.5])
    save(24, 16, fig)

    fig, ax = diagram((-3.8, 3.8), (-1.65, 1.97))
    for centre, name, labels in [(-1.85, "A", "XXYY"), (1.85, "B", "XYXY")]:
        ax.text(centre, 1.65, name, weight="bold", ha="center")
        for (dx, dy), ligand in zip([(0,1.1),(1.1,0),(0,-1.1),(-1.1,0)], labels):
            ax.plot([centre, centre+dx], [0,dy], color=INK, lw=1.4)
            ax.add_patch(Circle((centre+dx, dy), .17, ec=INK, fc="white", zorder=3))
            ax.text(centre+dx,dy,ligand,ha="center",va="center",zorder=4)
        ax.text(centre, 0, "M", ha="center", va="center",
                bbox={"fc": "white", "ec": "none", "pad": 2})
    save(24, 82, fig)

    fig, ax = diagram((-4.8, 4.4), (-.7, .65))
    ax.annotate("", (4.17,0), (-4.6,0), arrowprops=ARROW)
    ax.plot([-3, 2], [0, 0], color=INK, lw=3)
    for pos, label, filled in [(-3, "−3", False), (2, "2", True)]:
        ax.scatter([pos], [0], s=54, ec=INK, fc=INK if filled else "white", zorder=3)
        ax.text(pos, -.28, label, ha="center", va="top")
    ax.plot([0,0],[-.08,.08],color=SECONDARY)
    ax.text(0,-.28,"0",ha="center",va="top")
    save(24, 140, fig)
    plotted_polygon(24, 145, [(0,0),(5,0),(4,2),(1,4)])

    fig, ax = chart()
    x = np.linspace(-1,1,250)
    ax.plot(x,np.arccos(x),color=INK,lw=1.7)
    ax.scatter([-1,1],[np.pi,0], color=INK, s=20)
    ax.axhline(2*np.pi/3, ls=":", color=SECONDARY)
    ax.set(xlabel="x", ylabel="y", xlim=(-1.17,1.17), ylim=(-.2,3.39),
           xticks=[-1,0,1], yticks=[0,np.pi/2,2*np.pi/3,np.pi],
           yticklabels=["0","π/2","2π/3","π"])
    save(24, 150, fig)
    arrow_diagram(24,173,"123","pqr",[(0,1),(1,0),(1,1),(2,2)])
    fig, ax = chart()
    ax.axhline(0,color=INK,lw=.9)
    ax.axvline(0,color=INK,lw=.9)
    mark(ax,-2,3,"P")
    ax.set(xlabel="Real axis", ylabel="Imaginary axis", xlim=(-3.75,3.75), ylim=(-3.6,3.8),
           xticks=range(-3,4), yticks=range(-3,4))
    save(24,179,fig)


def draw_test_25():
    fig, ax = chart()
    ax.plot([0,3],[2,8],color=INK,lw=1.7,label="P")
    ax.plot([0,3],[2,4],"--",color=SECONDARY,lw=1.7,label="Q")
    ax.set(xlabel="Time (s)",ylabel="Velocity (m/s)",xlim=(-.12,3.16),ylim=(0,8.6),
           xticks=[0,1,2,3],yticks=range(0,9,2))
    ax.legend(loc="upper left")
    save(25,2,fig)

    fig, ax = chart()
    points = [(1,100),(1,200),(3,200),(3,100)]
    for start, end in zip(points, points[1:]+points[:1]):
        ax.plot([start[0],end[0]],[start[1],end[1]], color=INK, lw=1.5)
        middle = tuple(.55*a+.45*b for a,b in zip(start,end))
        forward = tuple(.40*a+.60*b for a,b in zip(start,end))
        ax.annotate("", forward, middle, arrowprops=ARROW)
    ax.set(xlabel="Volume (L)",ylabel="Pressure (kPa)",xlim=(.67,3.33),ylim=(72,225),
           xticks=[1,2,3],yticks=[100,150,200])
    save(25,26,fig)

    fig, ax = chart()
    ax.plot([-4,-1,1,3],[0,0,1,1],color=INK,label="X",lw=1.7)
    ax.plot([-4,-3,1,3],[0,0,.65,.65],"--",color=SECONDARY,label="Y",lw=1.8)
    ax.set(xlabel="Collector voltage (V)",ylabel="Photocurrent",ylim=(-.08,1.15),
           xticks=range(-4,4),yticks=[0])
    ax.legend(loc="upper left",ncol=2)
    save(25,45,fig)

    fig, ax = diagram((-3.8,3.8),(-1.54,1.83))
    orbitals = [
        (-1.89, "I", [(-.69,-.65,1),(0,-.65,1),(.69,-.65,1),(-.41,.35,0),(.41,.35,0)]),
        (1.89, "II", [(-.35,-1.02,2),(.35,-1.02,2),(0,-.54,2),(0,-.06,2),(0,.56,0)]),
    ]
    for centre, name, entries in orbitals:
        ax.text(centre,1.51,name,ha="center",weight="bold")
        for dx, y, occupation in entries:
            x = centre + dx
            ax.plot([x-.27,x+.27],[y,y],color=INK,lw=1.4)
            arrows = [] if occupation == 0 else [(0,False)] if occupation == 1 else [(-.10,False),(.10,True)]
            for offset, reverse in arrows:
                a,b=y+.04,y+.31
                ax.annotate("",(x+offset,a if reverse else b),(x+offset,b if reverse else a),
                            arrowprops={**ARROW,"shrinkA":0,"shrinkB":0})
    save(25,82,fig)
    plotted_polygon(25,136,[(0,0),(6,0),(6,2),(2,4)])

    fig, ax = chart()
    for offset, colour, marker, label in [(0,INK,"o","X"),(4,SECONDARY,"s","Y")]:
        x=np.array([0,1,2])+offset
        y=[1,3,2]
        ax.vlines(x,0,y,color=colour,lw=1.6)
        ax.scatter(x,y,color=colour,marker=marker,label=label)
    ax.set(xlabel="Observed value",ylabel="Frequency",xlim=(-.35,6.35),ylim=(0,3.7),
           xticks=range(7),yticks=range(4))
    ax.legend(ncol=2)
    save(25,140,fig)
    arrow_diagram(25,149,"123","pqrs",[(0,0),(1,1),(1,2),(2,2)])


if __name__ == "__main__":
    draw_test_24()
    draw_test_25()
