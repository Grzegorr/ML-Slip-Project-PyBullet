import numpy as np
import matplotlib.pyplot as plt

x = np.load("x.npy")
y = np.load("y.npy")

print("X shape:")
print(x.shape)



fig = plt.figure()

for i in range(9):
    ax = fig.add_subplot(3, 3, i+1, projection='3d')
    zline = x[i,:,29]
    yline = x[i,:,28]
    xline = x[i,:,27]

        #print(x[i,0:j,0])
        #print(xline[j])
    ax.plot3D(xline, yline, zline, 'red')

plt.savefig("trajectoriesPlot.png")
plt.show()
