from vtk import *

graph = vtkMutableDirectedGraph()
a = graph.AddVertex()
b = graph.AddChild(a)
c = graph.AddChild(a)
d = graph.AddChild(b)
e = graph.AddChild(c)
f = graph.AddChild(c)

view = vtkGraphLayoutView()
view.AddRepresentationFromInput(graph)

window = vtkRenderWindow()
window.SetSize(600, 600)
view.SetupRenderWindow(window)
view.GetRenderer().ResetCamera()
window.GetInteractor().Start()



