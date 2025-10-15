sam="Pam.Is.Good.Boy"
print(sam.split('.')[1])
#prints "Is" because it is the second part amongst 4 in the string separated by "."
print(sam.replace("Pam","Shyam"))
#prints "Shyam.Is.Good.Boy"
print(sam.upper())
#output "PAM.IS.GOOD.BOY"
#notice how replace did not change the value in the variable
print(sam.center(20,"="))
#==Pam.Is.Good.Boy===
m="MENU"
print(m.center(20,"-"))
print("Coffee".ljust(16,".")+"$1".rjust(4," "))
print("Tea".ljust(16,".")+"$1.5".rjust(4," "))
print("Cake".ljust(16,".")+"$5".rjust(4," "))
print("Ice-Cream".ljust(16,".")+"$3".rjust(4," "))
print("Cream Roll".ljust(16,".")+"$2".rjust(4," "))
#--------MENU--------
#Coffee..........  $1
#Tea.............$1.5
#Cake............  $5
#Ice-Cream.......  $3
#Cream Roll......  $2
sky="       Sky is very blue"
print(sky.strip())
#Sky is very blue
print(sky.rstrip())
#       Sky is very blue
print(sky.lstrip())
#Sky is very blue
print(len(sky))
#23 as it includes spaces as well
#for a multiline
a='''
Hello
Hey
'''
print (a)
#
#Hello
#Hey
#
s="Shashwat"
print(s[1:-1])
#hashwa
print(s[1:8])
#hashwat
#notice it does not include "S" when we start from 1. This is because it never includes starting index.