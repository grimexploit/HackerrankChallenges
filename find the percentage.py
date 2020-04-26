n = int(input())	#garaas utga avna
list = {}			#hooson list zarlana	

for i in range(0,n):
   name, maths, physics, chemistry = input().split(" ")		#4 huvisagchiig zaitai unshina (space tei gesen ug) 
   list[name] = (float(maths) + float(physics) + float(chemistry))/3	#list-nd baigaa name-d hargalzuulah utguudiin average iig tootsov
name = input()	#ug listnees 1 hunii neriig songoj average-iig haruulah uchir neree avna
if name in list:	#avsan ner list-nd baih ym bol 2 ornii nariivchlaltaigaar average utgiig hevlene
    print("%.2f" % list[name])
else:	#za medj baigaa baih 
    print("No")
