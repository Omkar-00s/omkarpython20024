def is_even(num):
  if num <=1:
    return False

  for i in range(2,int(num**0.5+1)):
    if num % i==0:
      return False
  return True

number = int(input("Enter a number:"))
if is_even(number):
  print(number, "the number is prime number")
else:
  print(number, "the number is not a prime number")