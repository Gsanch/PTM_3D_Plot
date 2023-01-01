import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches



# prepare some coordinates
x, y, z = np.indices((3, 3, 3))


# draw cuboids in the top left and bottom right corners, and a link between
# them
cube1 = (x == 0) & (y == 0) & (z == 0)
cube2 = (x == 2) & (y == 2) & (z == 2)


# combine the objects into a single boolean array
voxelarray = cube1 | cube2
print(voxelarray)
# set the colors of each object
colors = np.empty(voxelarray.shape, dtype=object)
colors[cube1] = 'blue'
colors[cube2] = 'red'


# and plot everything
ax = plt.figure().add_subplot(projection='3d')
red_patch = mpatches.Patch(color='red', label='Nueva situación')
blue_patch = mpatches.Patch(color='blue', label='Situación anterior')
ax.legend(handles=[red_patch,blue_patch])
labels = [item.get_text() for item in ax.get_xticklabels()]
labels = ["","","","Actual","","Mejora","","Nueva"]
ax.set_xticklabels(labels)
labels = [item.get_text() for item in ax.get_zticklabels()]
labels = ["","","Actual","","Mejora","","Nueva"]
ax.set_zticklabels(labels)
labels = [item.get_text() for item in ax.get_yticklabels()]
labels = ["","","","Actual","","Mejora","","Nueva"]
ax.set_yticklabels(labels)
ax.set_xlabel('Tecnología')
ax.set_ylabel('Mercado')
ax.set_zlabel('Función')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()