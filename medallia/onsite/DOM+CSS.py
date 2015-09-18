# /*
# <div>
#   <span class="title>My title</span>
# </div>

# <style>
#   div { width: 400px; }
#   span {
#     display: block;
#     width: 100%;
#     padding: 15px;
#   }
# </style>
# -------- Problem is that padding pushes span out of the div

# */

# /*

# <div>
#   <!-- comment 1 -->
#   <span>
#     <!-- comment 2 -->
#   </span>
# </div>

# function findComments(div) => [comment1, comment2]


# */

def findComments(node):
    if node is None:
        return []
    commentList = []
    children = node.getChildren()
    for child in children:
        if child.isComment():
            commentList.append(child)
        else:
            commentListFromThisDOMElement = findComments(child)
            commentList += commentListFromThisDOMElement
    return commentList

def findComments(node, functionName):
    if node is None:
        return []
    commentList = []
    children = node.getChildren()
    for child in children:
        if child.functionName():
            commentList.append(child)
        else:
            commentListFromThisDOMElement = findComments(child, functionName)
            commentList += commentListFromThisDOMElement
    return commentList


def findCommentsIt(node):
    if node is None:
        return []
    commentList = []
    queue = []
    queue.append(node)
    while len(queue) > 0:
        currNode = queue.popleft()
        for child in currNode.getChildren():
            if child.isComment():
                commentList.append(child)
            else:
                queue.append(child)
    return commentList
            