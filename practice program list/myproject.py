#print("hello mom")
#a="hello world!" #--Q1
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
#Q4 WAP TO FILL IN A LETTER TEMPLATE GIVEN BELOW WITH NAME AND DATE.
#letter='''Dear <|Name|>, 
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
#a=[11,2,3,4,55,96,7,8,89]
#print the lists using print() function
#print(a)
#print(a[5])
#Access using index using a[0],a[1],a[2]--Q9
#print(a[1])
#print(a[5])
#cg
# change the value of lists using--Q10
#a[0]=44
#print(a)

#we can create a lists with items of different types--Q11
#c=[45,"boy",False,6.9]
#print(c)

#list slicing--Q12
#friends=["haka","brocode","raka","pablo","loki",11]
#print(friends[0:5])

#list method--Q13
#l=[1,8,7,2,21,15]
#l.sort()
#l.reverse()
#l.append(99)#--add the item  at the end of the list
#l.insert(3,9)--insert a number 9 at 3rd position
#l.remove(15)--remove the number from the list
#l.pop(2)---delete the number from index 2
#print(l)

#TUPLES using ()--Q14
#t=(1,2,4,5)
#t1=() #empty tuple
#t2=(1,) #tuple with single element
#print(t[0])
#print(t[3])
#print(t1)
#print(t2)
#cannot update the values of tuple
#t[0]=34------ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#TUPLES METHODS--Q15

#t=(1,2,1,1,1,4,5)
#print(t.count(1))

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
#b=[2,34,43,5]

#print(b[0]+b[1]+b[2]+b[3])
#print(sum(b))

#WAP TO COUNT THE NUMBER OF ZEROS IN THE FOLLOWING TUPLE ---a=(7,0,8,0,0,9)--QUES19
#a=(7,0,8,0,0,9)
#print(a.count(0))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CHAPTER NUMBER -5 # DICTIONARY AND SETS ---Q20
#--DICTIONARY IS A COLLECTION OF KEY VALUES PAIRS
#myDict={
   # "Fast":"In a Quick Manner",
   #"Mrityunjay":"A coder",
   # "Marks":[1,2,3,45,6],
   #"AnotherDict":{'Mrityunjay':'A Hacker'}
    #}
#DICTIONARY METHODS----Q21
#print(myDict['Fast'])
#print(myDict['Mrityunjay'])
#print(myDict['Marks'])
#print(myDict['AnotherDict']['Mrityunjay'])
#print(list(myDict.keys()))--print the keys of the Dictionary
#print(list(myDict.values()))--print the keys of the Dictionary
#print(list(myDict.items()))--print the (keys,values) for all contents of the dictionary
#print(myDict)
#updateDict={
#    "Love For Ever":"Friendship",
#    "Mrityunjay":"A Dancer"
#}
#myDict.update(updateDict)#--update the dictionary by a key-value pairs from updateDict
#print(myDict)
#print(myDict.get("Mrityunjay"))--prints value associated with key "Mrityunjay"
#print(myDict["Mrityunjay"])--prints value associated with key "Mrityunjay"

#The difference between .get and [] syntax in Dictionary
#print(myDict.get("Mrityunjay2"))--returns None as Mrityunjay2 is not present in the dictionary
#print(myDict["Mrityunjay2"])--throws an error as Mrityunjay2 is not present in the dictionary
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#SETS IN PYTHON ----Q22
#a={1,23,4,5}
#print(type(a)) 
#print(a)

#Important: This syntax will create an empty dictionary and not an empty set.
#a={}
#print(type((a)))

#AN EMPTY SET CAN CREATED USING THE BELOW SYNTAX:
#a=set()
#print(type(a))
#adding values to aN EMPTY SET
#a.add(4)
#a.add(5)
#a.add(3)
#a.add(6)
#a.add(9)
#a.add(10)
#print(type(a))

#adding values to aN EMPTY SET-->

#a.add([3,6,7])#you can't add list cuz it can't be changed
#a.add((3,6,7))#you can add tuple cuz it can be changed
#print(a)
#print(len(a))#print the length of the set.
#a.remove(5) #remove 5 from set a
#a.remove(15)#throw an error while trying to remove 15 from set a(which is not present in the set)
#print(a)

#print(a.pop())
#print(a)
#print(a.clear())#clear the element from the set
#print(a.union({8,11}))
#print(a.intersection({8,11}))
#print(a)
#--------------------------------------------------------------------------------------------------------------------
#PRACTICE SET CHAPTER-5
#Q1-WAP TO CREATE A DICTIONARY OF HINDI WORDS VALUES AS THEIR ENGLISH TRANSLATION .PROVIDE USER WITH AN OPTION TO LOOK IT UP!

#myDict={
 #   "laal":"red",
  #  "kala":"black",
   # "hara":"green",
    #"neela":"blue"
#}
#print("Options are ",myDict.keys())
#a=input("Enter the Hindi Word\n")
#print("The Meaning of your word is:",myDict[a])
#print("The Meaning of your word is:",myDict.get(a))- don't throw errors(show NONE)
#---------------------------------------------------------------------------------------------------------------------------------
#Q2-WAP TO INPUT EIGHT NUMBERS FROM THE USER AND DISPLAY ALL THE UNIQUE NUMBERS (ONCE)
#num1=input("Enter number 1\n")
#num2=input("Enter number 2\n")
#num3=input("Enter number 3\n")
#num4=input("Enter number 4\n")
#num5=input("Enter number 5\n")
#num6=input("Enter number 6\n")
#num7=input("Enter number 7\n")
#num8=input("Enter number 8\n")
#s={num1,num2,num3,num4,num5,num6,num7,num8}
#print(s)
#----------------------------------------------------------------------------------------------------------------------------------
#Q3-CAN WE HAVE A SET WITH 18(INT) AND "18"(STR) AS A VALUES IN IT?
#s={18,"18",18.1}
#print(s)
#print(len(s))
#---------------------------------------------------------------------------------------------------------------------------------

#WHAT WILL BE THE LENGTH OF FOLLOWING SET S:--Q
#S=S()
#S.ADD=(20)
#S.ADD=(20.0)
#S.ADD=("20")

#s={20,20.0,"20"}
#print(len(s))
#-------------------------------------------------------------------------------------------------------------------------------------
#S={}--empty dictionary--Q
#WHAT IS THE TYPE OF 5?

#--------------------------------------------------------------------------------------------------------------------------------------
#CREATE AN EMPTY DICTIONARY .ALLOW 4 FRIENDS TO ENTER THEIR FAVOURITE LANGUAGE AS VALUES ANS USE KEYS AS THEIR NAME .ASSUME THAT THE NAMES ARE UNIQUE

#favLang={}
#a=input("Enter your favourite language Mrityunjay\n")
#b=input("Enter your favourite language Saurab\n")
#c=input("Enter your favourite language Ankit\n")
#d=input("Enter your favourite language Manas\n")
#
#favLang['Mrityunjay']=a
#favLang['Saurab']=b
#favLang['Ankit']=c
#favLang['Manas']=d
#print(favLang)
#--------------------------------------------------------------------------------------------------------------------------------------------------

#IF NAMES OF 2 FRIENDS ARE SAME ; WHAT WILL HAPPEN TO THE PROGRAM IN PROBLEM 6?--Q

#favLang={}
#a=input("Enter your favourite language Mrityunjay\n")
#b=input("Enter your favourite language Saurab\n")
#c=input("Enter your favourite language Ankit\n")
#d=input("Enter your favourite language Manas\n")
#
#favLang['Mrityunjay']=a
#favLang['Saurab']=b
#favLang['Mrityunjay']=c
#favLang['Manas']=d
#print(favLang)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#IF LANGUAGE OF 2 FRIENDS ARE SAME ; WHAT WILL HAPPEN TO THE PROGRAM IN PROBLEM 6?

#favLang={}
#a=input("Enter your favourite language Mrityunjay\n")
#b=input("Enter your favourite language Saurab\n")
#c=input("Enter your favourite language Ankit\n")
#d=input("Enter your favourite language Manas\n")
#
#favLang['Mrityunjay']=a
#favLang['Saurab']=b
#favLang['Ankit']=c
#favLang['Manas']=d
#print(favLang)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#CAN YOU CHANGE THE VALUE INSIDE A LIST WHICH IS CONTAINED IN SET S
# S={8,7,12,"HARRY",[1,2]}

#exit() no result can be found b/c their is tuple inside which can't be changed
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#CONDITIONAL EXPRESSIONS-CHAPTER-6
# If else and elif in python

#a=45------@1
#if(a>3):
#    print("The value of a is greater than 3")
#elif(a>7):
#    print("The value of a is greater than 7")   
#else:
#    print("The value is not greater than 3 or 7")
    #The value of a is greater than 3-OUTPUT
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#a=45--If-elif-else-ladder in python
#if(a<3):
#    print("The value of a is greater than 3")
#elif(a>13):
#    print("The value of a is greater than 13")
#elif(a>7):  
#    print("The value of a is greater than 7")  
#elif(a>17):
#    print("The value of a is greater than 17")
#else:
#    print("The value is not greater than 3 or 7")

#print("Done")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#2.MULYIPLE IF STATEMENTS
#a=45
#if(a<3):
#    print("The value of a is greater than 3")
#elif(a>13):
#    print("The value of a is greater than 13")
#elif(a>7):  
#    print("The value of a is greater than 7")  
#elif(a>17):
#    print("The value of a is greater than 17")
#else:
#    print("The value is not greater than 3 or 7")
#print("Done")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#QUIZ--
#Q1-WAP TO PRINT YES WHEN THE AGE ENTERED BY THE USER IS GREATER THAN OR EQUAL TO 18.

#age=int(input("Enter your Age"))
#if age>18:
#    print("YES")
#else:
#    print("NO")    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#RELATIONAL OPERATORS (==;>=;<=)

#age=int(input("Enter your Age:"))
#if (age>18 and age<59):
#    print("You can work with us")
#else:
#    print("You cannot work with us")    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#LOGICAL OPERATORS(and ;or ;not)

#a=None------(is)
#if(a is None):
#    print("YES")
#else:
#    print("NO")    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
#a = [45, 56, 6]
#print(453 in a)      
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ELSE OPTIONAL
#a=45
#if(a==7):
#    print("YES")
#elif(a>34):
#    print("NO and YES")
#else:
#    print("I am Optional")# else is optional
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------