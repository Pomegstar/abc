from stack import stack
 
def infixTopost(inTopost):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    s1 = stack()
    pofixlist = []
    tokenList = inTopost.split()

    for token in tokenList:
        if token not in "*/+-()":
            pofixlist.append(token)
        elif token == "(":
            s1.push(token)
        elif token == ")":
            toptok = s1.pop()
            while toptok != "(":
                pofixlist.append(toptok)
                toptok = s1.pop()
        else:
            while not (s1.isEmpty()) and (prec[s1.peek()] >= prec[token]):
                pofixlist.append(s1.pop())
            s1.push(token)   
    while not s1.isEmpty():
        pofixlist.append(s1.pop())
    return " ".join(pofixlist)

def postfixeval(postfixex):
    s = stack()
    tokenlist = postfixex.split()

    for token in tokenlist:
        if token not in ("+-*/"):
          s.push(int(token))
        else:
           operand2 = s.pop()
           operand1 = s.pop()
           result = domath(token, operand1, operand2)
           s.push(result)
    return s.pop()
def domath(token, operand1, operand2):
   if token == "*":
    return operand1 * operand2
   elif token == "/":
      return operand1 / operand2
   elif token == "+":
      return operand1 + operand2
   else:
      return operand1 - operand2
   
expr = input("enter your expressioin with space between items or numbers: ")
postfix = infixTopost(expr)
result = postfixeval(postfix)
print(result)
