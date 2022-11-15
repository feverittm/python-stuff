import pygame

import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.button import ButtonArray
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

activeLeg = 1

def setLeg(leg):
    activeLeg = leg
    lbltxt = "Active Leg: " + str(leg)
    label4.setText(lbltxt)
    print("Setting ",leg)

pygame.init()
win = pygame.display.set_mode((600, 600))

button1 = Button(win, 80, 10, 50, 50, fontsize=50, text='Femur', inactiveColor=(200,0,0), disable=True) # Femur is hip joint
button2 = Button(win, 180, 10, 50, 50, fontsize=50, text='Coxa',  inactiveColor=(200,0,0), disable=True) # Coxa is the mid-leg joint
button3 = Button(win, 280, 10, 50, 50, fontsize=50, text='Tibia', inactiveColor=(200,0,0), disable=True) # Tibia is the leg tip

label4 = TextBox(win, 150, 430, 0, 0, fontsize=50, disable=True)

# Creates an array of buttons
buttonArray = ButtonArray(win, 60, 450, 300, 100, (4, 1), border=20, texts=('Leg 1', 'Leg 2', 'Leg 3', 'Leg 4'), 
                          onClicks=(lambda: setLeg(1), lambda: setLeg(2), lambda: setLeg(3), lambda: setLeg(4))
)

ControlsArray = ButtonArray(win, 370, 20, 200, 400, (1, 5), border=20, texts=('1', '2', '3', '4', '5'))

slider1 = Slider(win, 100, 70, 10, 300, vertical=True, min=0, max=99, steps=1)
slider2 = Slider(win, 200, 70, 10, 300, vertical=True, min=0, max=99, steps=1)
slider3 = Slider(win, 300, 70, 10, 300, vertical=True, min=0, max=99, steps=1)

output1 = TextBox(win, 100, 400, 0, 0, fontsize=30)
output2 = TextBox(win, 200, 400, 0, 0, fontsize=30)
output3 = TextBox(win, 300, 400, 0, 0, fontsize=30)

output1.disable()
output2.disable()
output3.disable()

run = True

# Current Leg Position (Femur, Coxa, Tibia)
leg1Position=(0,0,0)
leg2Position=(0,0,0)
leg3Position=(0,0,0)
leg4Position=(0,0,0)

setLeg(1)
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
            
    win.fill((255, 255, 255))
    
    output1.setText(slider1.getValue())
    output2.setText(slider2.getValue())
    output3.setText(slider3.getValue())
    
    pygame_widgets.update(events)    
    pygame.display.update()