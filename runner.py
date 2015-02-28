# Code Concept of running though a maze of any length with each
# step of the maze with variable choices.

# Can be utilised as a method to apply machine learning to solve a problem

# Placeholder maze
maze=[]

# maze_pass produces 1 if the stored solution is a solution to maze
#  and 0 if the stored solution is not a 
def maze_pass(store,maze):
    return "code"

#maze_length calculates the length of the maze
def maze_length(maze):
    return "length"

#pass_value
pass_val = 0

#c_length represents the current length of store
c_length = 0 

#maze_length is the total length of the maze
maze_length = maze_length(maze) 

#attempts is the number of attempted solutions
attempts = 0

#possible is the total number of possible combinations
possible = 0

# assume at each step we are able to order the choices from
# best to worst (0 to k respectively)





# maze_run function solves a maze with any length, any number of choices at any step
#  with or without a solution
# Will return a solution if there is an solution or return "No solution" if there
#  is no solution
# k is the number of choices for current step, and possible is the number of possible
# combinations up to this step choice
def maze_run(k,maze_step):
    
    # Use global variables so that values are kept
    global possible 
    global maze_length
    global pass_val
    global c_length
    global attempt
    
    #will not stop until a solution is found
    while(pass_val == 0): 
        possible += k-1
        # tries the choices from best to worst
        for choice_step in range(0,k+1):
            # Note: We can relate real choices to the value of choice_step
            store[c_length] = choice_step
            
            if maze_step_choice(next_step(maze_step,choice_step))==0:
                # sees if current stored solution is correct
                pass_val = maze_pass(store)
                
                # add one to the number of attempts
                attempt += 1
                
                # change pass_val to 2 once all possibilites are attempted
                if attempt == possible:
                    pass_val = 2
                break
                
            # Increase the current length by 1
            c_length += 1
            maze_run(maze_step_choice(next_step(maze_step,choice_step)),next_step(maze_step,choice_step))
            
        if pass_val == 2:
            return "No Solution"
      
    return store