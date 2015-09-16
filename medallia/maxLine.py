/* Given a screen with randomly scattered pixels/points on it, find the line that has the max. no. of pixels/points on it. 

   A line is something that joins any two given points/pixels.
*/

def getEquation(a, b):
    x1, y1 = a
    x2, y2 = b
    if x1 == x2:
        return float("infinity"), x1
    slope = (y2 - y1)/(x2 - x1)
    yint = y1 - slope*x1
    return slope, yint

def calcMaxLine(pointList):
    hash = {}
    for i in range(0, len(pointList) - 1):
        for j in range(i+1, len(pointList)):
            pointA = pointList[i]
            pointB = pointList[j]
            slope, yint = getEquation(pointA, pointB)
            equationTuple = (slope, yint)
            if equationTuple not in hash:
                hash[equationTuple] = []
                hash[equationTuple].append(tuple(pointA, pointB))
            else:
                hash[equationTuple].append(tuple(pointA, pointB))
    maxNumPoints = 0
    for equation in hash:
        curNumPoints  = len(hash[equations])
        if curNumPoints > maxNumPoints: maxNumPoints = curNumPoints
    return maxNumPoints 
    
    
"""
   Create an API service that provides the following three APIs -
   
   Register a handler,
   Execute all registered handlers for an id,
   Delete a registered handler
     
   Register
   id=10, callback
   
   Execute
   id = 10
   
   Delete a registered handler
   delete all handlers at id
   
   
   id -> H1, H2, H3
   
   id ->
       userId -> H1, H2, H3
       kevinfu ->
           handlerId : H4
           handlerId : H5
       bob -> H7, H8, H9
   
"""    

handlerDataStructure = {}

def register(id, handlerId, userId, actualHandler):
    if id in handlerDataStructure:
        if userId in handlerDataStructure[id]:
            if handlerId in handlerDataStructure[id][userId]:
                return False
            else:
                handlerDataStructure[id][userId][handlerId] = actualHandler
        else:
    else:

def execute(id):
    for userId in handlerDataStructure[id]:
        for handler in handlerDataStructure[id][userId]:
            EXE(handlerDataStructure[id][userId][handler])