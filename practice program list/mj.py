#print("hello mom")
#a="hello world!"--Q1
#print(a[0:5])
#print(len(a))
#print(a.endswith("!"))
#print(a.count("l"))
#print(a.capitalize())
#print(a.find("world"))
#print(a.replace("hello","hy"))

#a="Hello World.\n How \t is your Day!"--Q2
#print(a)

#name=input("Enter Your Name\n")--Q3
#print("Good Afternoon,"+name)

#letter='''Dear <|Name|>,--Q4 WAP TO FILL IN A LETTER TEMPLATE GIVEN BELOW WITH NAME AND DATE.
#You are selected!

#Date:<|Date|>
#'''
#name=input("enter your name\n")
#date=input("enter date\n")
#letter=letter.replace("<|Name|>",name)
#letter=letter.replace("<|Date|>",date)
#print(letter)

#WAP TO DETECT DOUBLE SPACE B/W THE STRINGS--Q5
#st="this is a string with double   spaces"

#doublespace=st.find("  ")
#print(doublespace)

#wap REPLACE THE DOUBLE SPACES FROM Q5 WITH SINGLE SPACES.--Q6
#st="THIS IS A STRING WITH DOUBLE   SPACES"

#st=st.replace("  "," ")
#print(st)

#WAP TO FORMAT THE FOLLOWING LETTER USING ESCAPE SEQUENCE CHARACTERS.--Q7
#letter="Dear Man, this code is nice! Thanks!"
#print(letter)

#formatted_letter="Dear Man, \n\t This code is nice!\nThanks!"
#print(formatted_letter)

#LIST AND TUPLES--CHAPTER-4--Q8
#CREATE LISTS USING []
a=[11,2,3,4,55,96,7,8,89]
#print the lists using print() function
#print(a)
#print(a[5])
#Access using index using a[0],a[1],a[2]--Q9
print(a[1])
print(a[5])
#cg
# change the value of lists using--Q10
a[0]=44
print(a)

#we can create a lists with items of different types--Q11
c=[45,"boy",False,6.9]
print(c)

#list slicing--Q12
friends=["haka","brocode","raka","pablo","loki",11]
print(friends[0:5])

#list method--Q13
l=[1,8,7,2,21,15]
#l.sort()
#l.reverse()
#l.append(99)#--add the item  at the end of the list
#l.insert(3,9)--insert a number 9 at 3rd position
#l.remove(15)--remove the number from the list
#l.pop(2)---delete the number from index 2
#print(l)

#TUPLES using ()--Q14
t=(1,2,4,5)
t1=() #empty tuple
t2=(1,) #tuple with single element
print(t[0])
print(t[3])
print(t1)
print(t2)
#cannot update the values of tuple
#t[0]=34------ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#TUPLES METHODS--Q15

#t=(1,2,1,1,1,4,5)
print(t.count(1))

#t=(1,2,4,5)
#print(t.index(5))

#WAP TO STORE SEVEN FRUITS IN ALIST ENTERED BY USER.--QUES16
#l1=input("enter fruit number 1:")
#l2=input("enter fruit number 2:")
#l3=input("enter fruit number 3:")
#l4=input("enter fruit number 4:")
#l5=input("enter fruit number 5:")
#l6=input("enter fruit number 6:")
#l7=input("enter fruit number 7:")
#l8=input("enter fruit number 8:")
#l9=input("enter fruit number 9:")
#myFruitList=[l1,l2,l3,l4,l5,l6,l7,l8,l9]
#print(myFruitList)

#WAP TO EXCEPT MARKS OF 6 STUDENTS AND DISPLAY THEM IN A SORTED MANNER.--QUES17

#m1 = int(input("enter marks for Student number 1:"))
#m2 = int(input("enter marks for Student number 2:"))
#m3 = int(input("enter marks for Student number 3:"))
#m4 = int(input("enter marks for Student number 4:"))
#m5 = int(input("enter marks for Student number 5:"))
#m6 = int(input("enter marks for Student number 6:"))

#myList = [m1,m2,m3,m4,m5,m6]
#myList.sort()
#print(myList)

#CHECK THAT A TUPLE CANNOT BE CHANGED IN PYTHON
#a=(2,3,4,5,1,0)
#a[0]=34
#TypeError: 'tuple' object does not support item assignment

#wap to sum a list with 4 numbers .--QUES18
b=[2,34,43,5]

print(b[0]+b[1]+b[2]+b[3])
print(sum(b))

#WAP TO COUNT THE NUMBER OF ZEROS IN THE FOLLOWING TUPLE ---a=(7,0,8,0,0,9)--QUES19
a=(7,0,8,0,0,9)
print(a.count(0))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
CHAPTER NUMBER -5 # DICTIONARY AND SETS 
#--DICTIONARY IS A COLLECTION OF KEY VALUES PAIRS




