import graphMaker
import pathFind
import imageProcess
import tracePath
import math

maxinput = 10
starter = 75

totalNodes = 500
sensitivityC = 0.2
friendGap = 20
friendD = 30
angleTolerance = math.pi/8
calLength = 4


nodes = imageProcess.imgProc(totalNodes, sensitivityC, friendGap)
graph = graphMaker.makeGraph(nodes, friendD, angleTolerance, calLength)
path1 = pathFind.pathfinder(starter, maxinput*1000/(1375/697), graph)
tracePath.trace(nodes, path1)
