# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global List,exposed,exposed_,exposed_1,exposed_2,state,click
    List = range(0,8) + range(0,8)
    random.shuffle(List)
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,]
    card_index = 0
    state = 0
    exposed_1 = None
    exposed_2 = None
    exposed_0 = None
    click = 0
# define event handlers
def mouseclick(pos):
    global card_index,exposed,state,List,exposed_1,exposed_2,exposed_0,click
    card_index= pos[0]/50 
    click+=1
    if state == 0:
        exposed[card_index] = True
        state = 1
        exposed_1 = card_index
    elif state ==1:
        exposed[card_index] = True
        state = 2
        exposed_2 = card_index
    elif state == 2:
        if List[exposed_1] == List[exposed_2]:
                exposed[exposed_1] = True
                exposed[exposed_2] = True
        else:
                exposed[exposed_1] = False
                exposed[exposed_2] = False
        exposed[card_index] = True
        exposed_1 = card_index
        state = 1



        
    
# cards are logically 50x100 pixels in size    
def draw_cover(canvas):
    for i in range(0,len(List)):
        #canvas.draw_text(str(List[i]),(i*50,30),30,"Red")
        if exposed[i] == False:
            canvas.draw_polygon([(i*50,30),((i+1)*50,30),((i+1)*50,80),(i*50,80)],1,"Green")
        else:
            canvas.draw_text(str(List[i]),(i*50,30),30,"Red")
        label.set_text(str(click))
            

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw_cover)

# get things rolling
new_game()
frame.start()

