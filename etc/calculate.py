print("Input two numbers:")  #먼저 두개의 숫자를 입력받습니다.
x=int(input(''))  #정수를 x,y에 저장합니다.
y=int(input(''))
op=input('Input operation:') #op라는 변수에 연산자를 받습니다.
def my_plus(x,y):
 return x+y
def my_minus(x,y):
 return x-y
def my_multiply(x,y):
 return x*y
def my_division(x,y):
 return x/y       
def my_calculate(x,y,op):
 if op == '+' :
  return my_plus(x,y)
 if op == '-':
  return my_minus(x,y)
 if op == '*':
  return my_multiply(x,y)
 if op == '/':
  return my_division(x,y) 

 else:
  print("Sorry, check your inputs")
print("Result is", my_calculate(x,y,op) )    