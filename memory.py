# implementation of card game - Memory

import simplegui
import random

CARD_SIZE = [50, 100]
deck = []
exposed = []
state = 0
turns = 0
index1 = 0
index2 = 0

# helper function to initialize globals
def new_game():
    global deck
    global exposed
    global state
    global turns
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    list1 = range(8)
    list2 = range(8)
    deck = list1 + list2
    random.shuffle(deck)
    
    exposed = [False]*16
                
    print deck
             
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    global index1
    global index2
    global turns
       
    card_index = pos[0] // 50
    
    if exposed[card_index] == True:
        return
    if exposed[card_index] == False: 
        if state == 0:
            state = 1
            exposed[card_index] = True
            index1 = card_index
                                    
        elif state == 1:
            state = 2
            exposed[card_index] = True 
            index2 = card_index 
            
        elif state == 2: 
            if deck[index1] != deck[index2]:
                exposed[index1] = False
                exposed[index2] = False
                state = 1   
                exposed[card_index] = True
                index1 = card_index
            
            if deck[index1] == deck[index2]:
                state = 1   
                index1 = card_index
                exposed[card_index] = True
                index2 = 0
            turns += 1
            label.set_text("Turns = " + str(turns))
                     
       
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
        
    column = 0
    for index in range(len(deck)):
        if exposed[index]== True:
            canvas.draw_text(str(deck[index]),[column*50 + CARD_SIZE[0]/2, 
                                        CARD_SIZE[1]/2 + 10], 40, "White") 
            column +=1   
        elif exposed[index]== False:
            canvas.draw_line ([50*column + 25, 0], [50*column + 25, 100], 50, "Green")
            canvas.draw_line ([50*column, 0], [50*column, 100], 2, "Black")
            column +=1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric