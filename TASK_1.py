n=int(input("Enter a number: "))
def factorial(n):
  if n<2:
    return 1
  else :
    return n*(factorial(n-1))

R=factorial(n)
print (R)
  
