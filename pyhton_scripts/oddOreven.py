#Python program to check if the input number is odd or even
# if numberr is even - square input number
# if number is odd - cube input number

num = int(input("Enter a number: "))
if (num % 2) == 0:
  print(num**2)
else:
  print(num**3)