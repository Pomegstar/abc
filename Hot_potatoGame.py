from queu import queu
def hotpot(namelist, num):
    q = queu()
    for name in namelist:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.deque())
        q.deque()
    return q.deque()
print(hotpot(["s","d","f","e","r"], 14))