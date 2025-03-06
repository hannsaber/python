print ("#Basic - Print all integers from 0 to 150.")
x =range(0,151)
for n in x:
    print(n)
print("#Multiples of Five - Print all the multiples of 5 from 5 to 1,000")
x = range(5,1001,5)
for n in x:
    print(n)
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".
x=range(1,101)
for n in x:
    if (n % 10 ==0):
        print ("Coding Dojo")
    elif (n % 5 == 0):
        print ("coding")
    else:
        print (n)
#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum
x=range(0,500001)
sum=0
for n in x :
    if (n % 2 != 0):
        sum+=n
print (sum) 

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours
x =range (2018,0,-4)
for n in x:
    print (n)
print ("********************************")
low=2
heigth=9
mult =3

x=range (low,heigth+1)
for n in x:
    if (n % mult == 0):
        print(n)

    









    