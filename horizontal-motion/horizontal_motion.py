import numpy as np
import matplotlib.pyplot as plt

def calcY_HM(g, t):
    v = g*t
    h = ((g*(t**2))/(g))
    return h

def calcX_HM(v,t):
    S = v*t
    return S

def plotGraph(time, XY):
    t = np.arange(0.0, time, 0.125)
    fig, ax = plt.subplots()
    ax.plot(XY[0], XY[1])
    ax.set(xlabel='X', ylabel='Y', title='horizontal movement')
    ax.grid()

    fig.savefig("test.png")
    plt.show()


def main():
    time = 1 #input("time: ")   
    velocity = 10 #input("velocity: ")
    running = True
    Y = []
    X = []
    allPoints = []
    g = 9.8
    
    for i in np.arange(0, time, 0.125):
        X.append(calcX_HM(velocity,i))
    allPoints.append(X)

    for i in np.arange (0, time, 0.125):
        Y.append(-(calcY_HM(g, i)))
    allPoints.append(Y)
 
    print(allPoints)

    while running:
        plotGraph(time, allPoints)

if __name__ == "__main__":
    main()
