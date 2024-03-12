#python comments- this is a single line comment
"""
this is a sample multiline comment in python
"""

#variables
student_name = "Jonathan" #data type is string
student_age =20 #data type is integer
student_fee = 100.0 #data type is float
student_marks =100 #data type is integer
is_male= True #data type is boolean


#outputting the values in the variables
print(student_name)
print(student_age)
print(is_male)


student_name= "Jonathan"
student_name= "Allan"
print(student_name)

#case sensitivity
STUDENT_NAME = "Ryan"
student_name = "Ben"
print(STUDENT_NAME)


#variable naming in python
book_price= 20.0 #valid variable name
_book_price= 20.0 #valid variable name
#*book_price=10.0  invalid variable naming
#123_book_price=0 invalid variable naming
book_price_123= 40 #valid variable naming


x=y=z=10 #assigning one value to multiple variables
x,y,z=30,40,50 #multiple values being assigned to multiple variables


#casting example 1
price= 10
quantity= 5
total= price*quantity
print("the total is:"+str(total)+ "Kenyan shillings")

#casting example 2
firstname= "Jonathan "
secondname= "Allan"
thirdname= firstname+secondname
print("His thirdname name is:" +thirdname)

#casting example 3
firstname= "Jonathan "
secondname=73734
thirdname=firstname+str(secondname)
print("His thirdname name is:" ,thirdname)

#casting example 4
a= 1
b=2
c= a+b
print("the sum of a and b is:",c)

#ASSIGNMENT OPERTAORS
#division
print(7.5/1.5)
#floor division
print(7.5//1.5)
#modulus
print(3%7)
#exponentiation
print(2**5)

#ASSIGNMENT OPERATORS
x=5
print(x) #output is 5
x+=5 #x=X+5
print(x) #output is 10
x-=4 #x=x-4
print(x) #output is 6
x*=3 #x=x*3
print(x) #output is 18
x/=2 #x=x/2
print(x) #output is 9

#COMPARISON OPERATORS
a=20
b=20
print(a==b) #output is TRUE

a=20
b=28
print(a!=b) #output is TRUE

#LOGICAL OPERATORS
age= 20
nationality= "North America"
if nationality=="North America" and age>=35:
    print("You can be President")
else:
    print("You cannot President")

constituency="Kasarani"
if constituency=="Kasarani" or "Embakasi" or "Westlands":
    print("you can be a governor")
else:
    print("you can't be a governor")