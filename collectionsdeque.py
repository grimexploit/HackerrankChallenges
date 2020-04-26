from collections import deque	#deque gedeg ni 2 talaas ni yavdag queue gesen ug.
n = int(input())
d = deque()	#hervee husvel tusad ni list uusgeed urd ni deque(blablabla) geed yavj bolno

for i in range(0,n):	#for davtalt guilgej muruu unshij baina
    command = input().split(" ")	
    if command[0] == "append":	#hervee hamgiin ehnii string ni iim baih ym bol ternii ard baigaa integer iig nemne
        d.append(command[1])	#append ashiglaval list-iin baruun tald element nemne
    elif command[0] == "appendleft":	#end esregeeree zuun tald ni nemne	
        d.appendleft(command[1])	#suuld nemsen elementee ustgana
    elif command[0] == "pop":	#hervee listee tseverlehiig husvel d.clear() 
        d.pop()
    else:
        d.popleft()		#hamgiin zuun gariin elementiig ustgana
print(' '.join(d))