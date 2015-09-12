class Node:
    def __init__(self):
        self.friends = []
        self.enemies = []
    def addFriend(self, friend):
        self.friends.append(friend)
    def getFriends(self):
        return self.friends
    def addEnemies(self, enemy):
        self.enemies.append(enemy)
    def getEnemies(self):
        return self.enemies

def recursion(starter, relation, result, nodeArray):
    if len(relation) == 0:
        if starter == result: return True
        else: return False
    relationship = relation[0]
    if relationship == 'F':
        for friend in nodeArray[starter].getFriends():
            if recursion(friend, relation[1:], result, nodeArray): return True
        return False
    elif relationship == 'E':
        for enemy in nodeArray[starter].getEnemies():
            if recursion(enemy, relation[1:], result, nodeArray): return True
        return False
    else:
        return None
    
        
def  isFrenemy( n,  frenemy,  x,  y,  relation):
    nodeArray = [Node() for i in range(n)]
    for personA in range(n):
        for personB in range(n):
            if personA == personB: continue
            relationship = frenemy[personA][personB]
            if relationship == 'F':
                nodeArray[personA].addFriend(personB)
                nodeArray[personB].addFriend(personA)
            elif relationship == 'E':
                nodeArray[personA].addEnemies(personB)
                nodeArray[personB].addEnemies(personA)
   
    if recursion(x, relation, y, nodeArray): return 1
    else: return 0