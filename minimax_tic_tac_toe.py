

empty_cells=[]
def emptyCells(state):
    empty_cells.clear()
    for x in range(0,3):
        for y in range(0,3):
            if state[x][y]==0:
                empty_cells.append([x,y])
    return empty_cells
def check(state):
    for x in range(0,3):
            for player in range(-1,2,2):
                if ((state[x][0]==player and state[x][1]==player and state[x][2]==player) or
                    (state[0][x] ==player and state[1][x] == player and state[2][x] == player) or
                    (state[0][0] == player and state[1][1] == player and state[2][2] == player) or
                    (state[0][2] == player and state[1][1] == player and state[2][0] == player)):
                        # print("player ",player, " won", x)
                        if player==1:
                            return 10
                        elif player==-1:
                            return -10
    return False

def minimax(state,depth,player):
    empty_states=emptyCells(state)
    result_from_check=check(state)
    # print(state)
    if len(empty_states)==0 and result_from_check==False:
        return 0
    elif result_from_check==10:
        return 10
    elif result_from_check==-10:
        return -10
    else:
        if player==1:
            best=-1000
            for aa in range(0,3):
                for bb in range(0,3):
                    if state[aa][bb]==0:
                        state[aa][bb]=player
                        best=max(best,minimax(state,depth+1,-player))
                        state[aa][bb]=0
            return best
        elif player==-1:
            best=1000
            for aa in range(0,3):
                for bb in range(0,3):
                    if state[aa][bb]==0:
                        state[aa][bb]=player
                        best=min(best,minimax(state,depth+1,-player))
                        state[aa][bb]=0
            return best
def best_move(state,player):
    best=-1000
    if len(emptyCells(state))!=0 and check(state)==False:
        for aa in range(0, 3):
            for bb in range(0, 3):
                if state[aa][bb]==0:
                    state[aa][bb] = player
                    mov_val=minimax(state,0,-player)
                    state[aa][bb] = 0
                    if best<mov_val:
                        best=mov_val
                        best_cell=[aa,bb]

        return best_cell,best
    elif check(state)==10:
        return True
    else:
        return False
if __name__ == '__main__':
    print("Enter 1-9..")
    # state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    status=True
    while(status==True):
        inp=input()
        dict1={'1':[0,0],'2':[0,1],'3':[0,2],'4':[1,0],'5':[1,1],'6':[1,2],'7':[2,0],'8':[2,1],'9':[2,2]}

        x=dict1.get(inp)[0]
        y=dict1.get(inp)[1]
        x=int(x)
        y=int(y)
        if state[x][y]!=0:
            print("cell occupied")
        else:
            state[x][y]=-1
            if best_move(state,1)==False:
                for aa in range(0, 3):
                    print(state[aa][0], " ", state[aa][1], " ", state[aa][2])
                print("It's a draw")
                status=False
            elif best_move(state,1)==True:
                for aa in range(0, 3):
                    print(state[aa][0], " ", state[aa][1], " ", state[aa][2])
                print("Computer won")
                status=False
            else:
                best_cell,best=(best_move(state,1))
                state[best_cell[0]][best_cell[1]]=1
                for aa in range(0, 3):
                    print(state[aa][0]," ",state[aa][1]," ",state[aa][2])
