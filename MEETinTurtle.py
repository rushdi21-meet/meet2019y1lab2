import turtle 
turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)
turtle.penup()
#Draw the E:
turtle.goto(-80,100)
turtle.pendown()
turtle.goto(0,100)
turtle.penup()
turtle.goto(-80,33.3)
turtle.goto(-80,0)
turtle.pendown()
turtle.goto(0,0)
turtle.penup()
turtle.goto(-80,-100)
turtle.pendown()
turtle.goto(0,-100)
turtle.penup()
turtle.goto(-80,100)
turtle.pendown()
turtle.goto(-80,-100)
turtle.penup()
#again E:
turtle.goto(80,100)
turtle.pendown()
turtle.goto(160,100)
turtle.penup()
turtle.goto(80,33.3)
turtle.goto(80,0)
turtle.pendown()
turtle.goto(160,0)
turtle.penup()
turtle.goto(80,-100)
turtle.pendown()
turtle.goto(160,-100)
turtle.penup()
turtle.goto(80,100)
turtle.pendown()
turtle.goto(80,-100)
turtle.penup()
#Drawing T:
turtle.goto(180,100)
turtle.pendown()
turtle.goto(260,100)
turtle.goto(220,100)
turtle.goto(220,-100)
turtle.mainloop()
