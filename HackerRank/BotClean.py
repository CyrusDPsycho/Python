class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, dest):
        return abs(dest.x - self.x) + abs(dest.y - self.y)

def next_move(posx, posy, board):
    bot_cell = Node(posy, posx)

    dirty_nodes = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "d":
                dirty_nodes.append(Node(j, i))
    nearest_node = None
    for node in dirty_nodes:
        if nearest_node is None or node.dist(bot_cell) < nearest_node.dist(bot_cell):
            nearest_node = node

    if nearest_node is not None:
        Move(nearest_node.x - bot_cell.x, nearest_node.y - bot_cell.y)
         
def Move(dx, dy):
    if dx < 0 :
        print "LEFT"
    elif dx > 0 :
        print "RIGHT"
    elif dy < 0 :
        print "UP"
    elif dy > 0 :
        print "DOWN"
    else:
        print "CLEAN"
        
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    brd = [[j for j in raw_input().strip()]for i in range(5)]
    next_move(pos[0],pos[1], brd)
