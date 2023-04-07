from catplot.grid_components.nodes import Node2D
from catplot.grid_components.edges import Edge2D
from catplot.grid_components.grid_canvas import Grid2DCanvas
from catplot.grid_components.supercell import SuperCell2D
import numpy as np
import matplotlib.pyplot as plt

nodes, edges = [], []

top = Node2D([0.0, 0.0], size=1, color='#5A5A5A')
t1 = Node2D([0.0, 1.0])
t2 = Node2D([1.0, 0.0])
nodes.append(top)

e1 = Edge2D(top, t1, width=1)
e2 = Edge2D(top, t2, width=1)
edges.extend([e1, e2])

canvas = Grid2DCanvas()
supercell = SuperCell2D(nodes, edges)

canvas.add_supercell(supercell)
canvas.draw()
canvas.figure

expanded_supercell = supercell.expand(60, 50)

canvas_big = Grid2DCanvas(figsize=(30, 20), dpi=60)
canvas_big.add_supercell(expanded_supercell)
canvas_big.draw()
canvas_big.figure

path = 'timeStd_Max_within_2Hours_per_SpacePoint.txt'
data = np.genfromtxt(path)
data = np.array(data)
print data.shape

subdata = data[11:12,:]
print subdata.shape

subdata = np.transpose(subdata)

max_sub = max(subdata)
print max_sub

subdata = subdata / max_sub

subdata = subdata * 50
print subdata.shape

delta = 60.0/25000

plt.plot(np.arange(0, delta*23493, delta), subdata, color='orange')

plt.show()
