#palindrome example = radar {which can readed from both left and right side}
from deque import deque
st = input("enter a string: ")
d = deque()
for ch in st:
    d.addRear(ch)

isPal = True
while isPal and d.size() > 1:
    xb = d.removeFront()
    xd = d.removeRear()
    if xb != xd:
        isPal = False
if isPal:
    print("your input is a palindrome")
else:
    print("your input is not a palindrome") 
    




