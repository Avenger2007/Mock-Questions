"""Draw the original practice figures for COMEDK Tests 8 and 9."""
import numpy as np
from matplotlib.patches import Circle, Rectangle

from tests_04_05_figures import chart, diagram, polygon, save, INK


def main():
    fig, ax = chart()
    x = [0, 1, 1.8, 3, 4]
    y = [0, 2, 3.6, 2, 1]
    ax.plot(x, y, color=INK, linewidth=2)
    for label, i in zip("ABCD", [0, 1, 3, 4]):
        ax.scatter(x[i], y[i], color=INK)
        ax.annotate(label, (x[i], y[i]), xytext=(7, 5), textcoords="offset points")
    ax.set(xlabel="Time (s)", ylabel="Position (m)", xticks=range(5), yticks=range(5),
           xlim=(-.2,4.5), ylim=(-.2,4.2))
    save(8, 11, fig)

    fig, ax = diagram((-1.9, 1.9), (-1.6, 1.6))
    sites = [(0, 1.23, "A"), (0,-1.23,"A"), (-1.45,.48,"A"),
             (1.45,-.48,"B"), (1.45,.48,"B"), (-1.45,-.48,"B")]
    for x, y, label in sites:
        ax.plot([0,x],[0,y],color=INK,linewidth=1.7,linestyle="--" if x*y>0 else "-")
        ax.text(x,y,label,ha="center",va="center",bbox=dict(facecolor="white",edgecolor="none"))
    ax.text(0,0,"M",ha="center",va="center",bbox=dict(facecolor="white",edgecolor="none"))
    save(8, 82, fig)

    fig, ax = chart()
    polygon(ax, [(0,0),(4,0),(3,3),(0,5)])
    ax.scatter(1,2,color=INK)
    ax.annotate("E",(1,2),xytext=(6,4),textcoords="offset points")
    ax.set(xlabel="x",ylabel="y",xticks=range(5),yticks=range(6),
           xlim=(-.2, 4.65),ylim=(-.25,5.55))
    save(8, 130, fig)

    fig, ax = diagram((-2.3,2.3),(-1.38,1.38))
    ax.add_patch(Rectangle((-2.16,-1.23),4.32,2.46,fill=False,edgecolor=INK,lw=1.4))
    for x, label in [(-.68,"A"),(.68,"B")]:
        ax.add_patch(Circle((x,0),.94,fill=False,edgecolor=INK,lw=1.6))
        ax.text(x,1.05,label,ha="center")
    for x,y,label in [(-1.10,0,"9"),(0,0,"?"),(1.10,0,"6"),(1.76,.94,"4")]:
        ax.text(x,y,label,ha="center",va="center")
    save(8, 170, fig)

    fig, ax = chart()
    v = np.linspace(0,.75,280)
    f = lambda x: .15*(np.exp(5*x)-1)
    ax.plot(v,f(v),color=INK,lw=2)
    for label, x in [("P",.25),("Q",.65)]:
        ax.scatter(x,f(x),color=INK)
        ax.annotate(label,(x,f(x)),xytext=(-13,6),textcoords="offset points")
    ax.set(xlabel="Forward voltage (V)",ylabel="Diode current (mA)",xlim=(0,.78),ylim=(0,7))
    save(9, 3, fig)

    fig, ax = diagram((-2.75,2.75),(-1.2,1.35))
    x = [-2.65,-.72,.72,2.65]
    y = [.73,.73,.365,.365]
    ax.plot(x,y,color=INK,lw=2)
    ax.plot(x,[-r for r in y],color=INK,lw=2)
    ax.annotate("",xy=(-1.33,0),xytext=(-2.21,0),arrowprops=dict(arrowstyle="->",color=INK))
    ax.text(-1.9,.99,"Area 4A",ha="center")
    ax.text(1.62,.68,"Area A",ha="center")
    save(9, 47, fig)

    fig, ax = chart()
    x = np.linspace(0,4,150)
    c = lambda u: .80*np.exp(-.47*u)
    ax.plot(x,c(x),color=INK,lw=2)
    ax.plot([0,1.15],[.8,.8-.8*.47*1.15],ls="--",color=INK)
    ax.plot([0,4],[.8,c(4)],ls=":",color=INK)
    ax.annotate("Tangent",(1.0,.424), xytext=(1.35,.62),
                arrowprops=dict(arrowstyle="-",color=INK))
    ax.annotate("Secant",(2.44,.39),xytext=(2.30,.66),
                arrowprops=dict(arrowstyle="-",color=INK))
    ax.set(xlabel="Time (s)",ylabel="[A] (mol/L)",xticks=range(5),xlim=(-.1,4.2),ylim=(0,.9))
    save(9, 64, fig)

    fig, ax = chart()
    polygon(ax, [(0,0),(5,0),(4,2),(0,3)])
    ax.set(xlabel="x",ylabel="y",xticks=range(6),yticks=range(4),
           xlim=(-.2,5.55),ylim=(-.25,3.55))
    save(9, 133, fig)


if __name__ == "__main__":
    main()
