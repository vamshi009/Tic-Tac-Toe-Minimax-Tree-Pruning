import os, random
import numpy as np
from show_2d import show_2d_plot
import copy

game_size = 3
def initialize():
    x = [0]*game_size
    H = [x]*game_size
    a = random.choice([0,1,2])
    y = random.choice([0,1,2])
    print("chose ",a, y)
    print(H)
    H = np.array(H)

    H[a][y] = 1
    print(H)
    #show_2d_plot(H)
    return H


def check_max_has_won(initial_state):
    
    index = 2
    for i in range(game_size):
        check = 1
        for j in range(game_size):
            if(initial_state[i][j]!=index):
                check = 0
                break
        if(check==1):
            return 10

    for i in range(game_size):
        check = 1
        for j in range(game_size):
            if(initial_state[j][i]!=index):
                check = 0
                break
        if(check==1):
            return 10
        

    for i in range(game_size):
        check = 1
        if(initial_state[i][i]!=index):
            check = 0
            break

    if(check==1):
        return 10
        
    for i in range(game_size):
        check = 1
        if(initial_state[2-i][i]!=index):
            check = 0
            break

    if(check==1):
        return 10

    return 0

def check_min_has_won(initial_state):
    #print("checking mini for ", initial_state)
    index = 1
    for i in range(game_size):
        check = 1
        for j in range(game_size):
            if(initial_state[i][j]!=index):
                check = 0
                break
        if(check==1):
            print("check from 1")
            return 10

    for i in range(game_size):
        check = 1
        for j in range(game_size):
            if(initial_state[j][i]!=index):
                check = 0
                break
        if(check==1):
            print("check from 2")
            return 10
        

    for i in range(game_size):
        check = 1
        if(initial_state[i][i]!=index):
            check = 0
            break

    if(check==1):
        print("check from 3")
        return 10
        
    for i in range(game_size):
        check = 1
        if(initial_state[2-i][i]!=index):
            check = 0
            break

    if(check==1):
        print("check from 4")
        return 10
        
    return 0

def play_turn_of_mac_maximizer(initial_state):

    min_score = 0
    curr_status = 'progress'
    current_selected_state = initial_state
    for i in range(game_size):
        for j in range(game_size):
            if(initial_state[i][j]==0):
                local_state = copy.deepcopy(initial_state)
                local_state[i][j] = 2
                score = check_max_has_won(local_state)
                if(score==10):
                    return local_state, "GameOver", 10

                sample_local_state = copy.deepcopy(local_state)
                min_state, status, score = play_turn_of_opponent_minimizer(sample_local_state)
                #print("min retuns inside mac maximizer")
                if(min_score==0):
                    min_score=score
                    current_selected_state = local_state
                else:
                    if(score<min_score):
                        min_score = score
                        current_selected_state = local_state

          
    return current_selected_state, curr_status, min_score


def play_turn_of_opponent_minimizer(initial_state):
    min_score = 0
    current_selected_state = initial_state
    curr_status = 'progress'

    for i in range(game_size):
        for j in range(game_size):
            if(initial_state[i][j]==0):
                local_state = copy.deepcopy(initial_state)
                local_state[i][j] = 1
                score = check_min_has_won(local_state)
                if(score==10):
                    #print("returning from mini edgecase ", i, j)
                    #print(local_state)
                    #print("score ", score)     
                    return local_state, "GameOver", 10
                sample_local_state = copy.deepcopy(local_state)

                min_state, status, score = play_turn_of_mac_maximizer(sample_local_state)
                #print("mac retuns inside minimizer")
                #print(min_state)
                #print(score)
                if(min_score==0):
                    min_score=score
                    current_selected_state = local_state
                else:
                    if(score<min_score):
                        min_score = score
                        current_selected_state = local_state

    print("returning from mini ")
    print(current_selected_state)
    print("score ", min_score)     
    return current_selected_state, curr_status, min_score


def get_remaining(initial_state):
    zero_count = 0
    for i in range(game_size):
        for j in range(game_size):
            if(initial_state[i][j]==0):
                zero_count = zero_count + 1
    
    return zero_count



def check_human_input(x, y):
    
    if((x>=0 and x<game_size) and (y>=0 and y<game_size)):
        return True
    else:
        return False
    

def start_game_with_human():
    initial_state = initialize()

    status = 'progress'
    current_state = initial_state
    count = 1
    show_2d_plot(current_state)
    print("Initalize with \n")
    print(current_state)
    while(status!='GameOver'):
        max_move_state, max_status, score = play_turn_of_mac_maximizer(current_state)
        print("max move")
        print(max_move_state)
        show_2d_plot(max_move_state, "max")
        if(max_status=="GameOver"):
            print("Max WON"*8)
            break

        x = int(input("Entered x co-ordinate\n"))
        y = int(input("Enter y-co-ordinate\n"))

#        min_move_state, min_status, score = play_turn_of_opponent_minimizer(max_move_state)
        if(check_human_input(x,y)):
            min_move_state = copy.deepcopy(max_move_state)
            min_move_state[x][y] = 1
        
        min_score = check_min_has_won(min_move_state)
        
        min_status ='progress'
        if(min_score==10):
            min_status="GameOver"

        print("min move state")
        print(min_move_state)

        current_state = min_move_state
        print("Move no ", count)
        print("currentstate  after  move")
        print(current_state)
        show_2d_plot(current_state, "mini")
        print("status ", status)
        count = count + 1
        if(min_status=="GameOver"):
            print("Min WON"*8)
            break

        zero_c = get_remaining(current_state)
        if(zero_c==0):
            print("GAME DRAW*"*8)
            break
    
        status = min_status

def start_game():
    initial_state = initialize()

    status = 'progress'
    current_state = initial_state
    count = 1
    show_2d_plot(current_state)
    print("Initalize with \n")
    print(current_state)
    while(status!='GameOver'):
        max_move_state, max_status, score = play_turn_of_mac_maximizer(current_state)
        print("max move")
        print(max_move_state)
        show_2d_plot(max_move_state, "max")
        if(max_status=="GameOver"):
            print("Max WON"*8)
            break

        min_move_state, min_status, score = play_turn_of_opponent_minimizer(max_move_state)
        print("min move state")
        print(min_move_state)

        current_state = min_move_state
        print("Move no ", count)
        print("currentstate  after  move")
        print(current_state)
        show_2d_plot(current_state, "mini")
        print("status ", status)
        count = count + 1
        if(min_status=="GameOver"):
            print("Max WON"*8)
            break

        zero_c = get_remaining(current_state)
        if(zero_c==0):
            print("GAME DRAW*"*8)
            break
    
        status = min_status

    




if(__name__=="__main__"):
    #initialize()
    start_game()
    #start_game_with_human()
    