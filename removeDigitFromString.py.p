import re
txt="the 3 third of July"
x=re.sub("\s","",txt)
x=re.findall("\D",x)
print(x,end=" ")
