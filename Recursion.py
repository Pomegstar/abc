def s(iList): 
        if len(iList) == 1:
           return iList[0]
        else:
           return iList[0] + s(iList[1:]) #s(iLIst[1:]) is a recursive function

print(s([2343,65,5,78,897]))



import turtle
t = turtle.Turtle()
s = turtle.Screen()

def spi(t,linLen):
    if linLen  > 0:
          
     t.forward(linLen)
     t.right(120)
     spi(t,linLen)
spi(t,200)
