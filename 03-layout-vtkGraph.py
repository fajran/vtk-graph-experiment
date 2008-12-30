
from vtk import *

source = vtkRandomGraphSource()
source.SetNumberOfVertices(50)
source.SetNumberOfEdges(200)

graph = source.GetOutput()

layout = vtkGraphLayout()
layout.SetInput(graph)

strategy = vtkCircularLayoutStrategy()

layout.SetLayoutStrategy(strategy)
layout.Update()

view = vtkGraphLayoutView()
view.AddRepresentationFromInputConnection(layout.GetOutputPort())
view.SetLayoutStrategyToPassThrough()

window = vtkRenderWindow()
window.SetSize(600, 600)
view.SetupRenderWindow(window)
view.GetRenderer().ResetCamera()
window.GetInteractor().Start()

