try:
  num = int(input(" Enter number "))
  print(10/num)
except ZeroDivisionError:
  print("You can't divide by zero.")
except ValueError:
  print("Invalid input! Please enter a number.")try