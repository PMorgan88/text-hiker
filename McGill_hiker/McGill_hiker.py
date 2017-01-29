import turtle
import time
from stack import Stack

def mountain(mtnText):
    """Creates and returns a matrix from a properly formatted text file"""
    mountainArray = []
    lineCount = 0
    
    for line in mtnText.readlines():
         temp = []
         for char in line:
             temp.append(char)
         lineCount += 1
         mountainArray.append(temp)
    print(''.join(mountainArray[0]))
    return mountainArray
    
def draw(mtn,turt):
    """Draws each individual tree for the graphical representation based upon the matrix from mountain""" 
    turtle.speed(0)
    turtle.delay(0)
    turt.penup()
    nrows = len(mtn[0])-1
    ncols = len(mtn)
    for i in range(ncols):
        for j in range(nrows):
            if mtn[i][j] == '^':
                turt.setposition(j*40-500,-i*40+150)
                turt.shape("classictree.gif")
                turt.stamp()
            
            
def travel(mtn,turt,rock):
    """2 turtle objects follow the path created by pushing empty spaces onto the stack and pulling them out for a x,y position.
    Hiker walks the path until finding the objective of t. Rock object leaves rocks behind the hiker to mark the paths taken already."""
    stack = Stack()
    turt.shape("lockwalk.gif")
    rock.shape('rock.gif')
    rock.speed(0)
    rock.hideturtle()
    rock.penup()
    tX,tY = 0,0
    walk = 0
    nrows = len(mtn[0])-1
    ncols = len(mtn)
    c = 0
    
    """Finds starting point"""
    for i in range(ncols):
        for j in range(nrows):
            if mtn[i][j] == 'p':
                tX,tY = i,j
                
    turt.setposition(tY*40-500,-tX*40+150)
    turtle.delay(10)
    turt.speed(1)
    time.sleep(3)
 
    while c < 1:
            mtn[tX][tY] = 'a'
            try:
                if mtn[tX][tY+1] == ' ' or mtn[tX][tY+1] == 't':
                    stack.push(tX)
                    stack.push(tY+1)
                if mtn[tX][tY-1] == ' ' or mtn[tX][tY-1] == 't':
                    stack.push(tX)
                    stack.push(tY-1)
                if mtn[tX+1][tY] == ' ' or mtn[tX+1][tY] == 't':
                    stack.push(tX+1)
                    stack.push(tY)
                if mtn[tX-1][tY] == ' ' or mtn[tX-1][tY] == 't':
                    stack.push(tX-1)
                    stack.push(tY)
            except:
                pass
                
            tY = stack.pop()
            tX = stack.pop()
            rock.setposition(tY*40-500,-tX*40+150)
            turt.setposition(tY*40-500,-tX*40+150)
            rock.stamp()
            
            if walk == 0:
                turt.shape("lockwalk2.gif")
                walk += 1
            else:
                turt.shape("lockwalk.gif")
                walk -= 1
            if mtn[tX][tY] == 't':
                rock.clearstamps(-1)
            while mtn[tX][tY] == 't':
                turt.shape('lockarmsup.gif')
                time.sleep(.5)
                turt.shape('lockarmsdown.gif')
                time.sleep(.5)
                    
def McGill_hiker(f):
    """Turtle and canvas creation as well as shapes added"""

    f = open(f)
    canvas.setup(1200,700)
    mountainBack = mountain(f)
    turtle.screensize(len(mountainBack)*200,len(mountainBack[0])*100)
    turtle.addshape("lockwalk.gif", shape=None)
    turtle.addshape("rock.gif", shape=None)
    turtle.addshape("lockwalk2.gif", shape=None)
    turtle.addshape("classictree.gif", shape=None)
    turtle.addshape("lockarmsdown.gif", shape=None)
    turtle.addshape("lockarmsup.gif", shape=None)
    draw(mountainBack,hiker)
    travel(mountainBack,hiker,rock)
canvas = turtle.Screen()
canvas.setup(10,10)
hiker = turtle.Turtle()
rock = turtle.Turtle()

