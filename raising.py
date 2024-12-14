def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or order.")
    return True

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or order.")
    return True

try:
  check_age(16)
except ValueError as e:
    print(e)  
