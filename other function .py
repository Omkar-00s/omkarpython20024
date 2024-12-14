with open("/content/omkar.txt","w") as file:
  file.write("hello world!")

with open("/content/omkar.txt","r") as file:
  content=file.read()
  print(content)

with open("/content/omkar.txt","a") as file:
  file.write("Welcome to python programming!")

with open("/content/omkar.txt","r") as file:
  line_count = 0
  for line in file:
    line_count += 1
print("Number of lines:", line_count)

with open("/content/omkar.txt","r") as file:
  content = file.read()
  word  = content.split()
with open("/content/omkar.txt","r") as file:
  content = file.read()
  word  = content.split()
  word_count = len(word)

print(f"The file has {word_count} words.")

with open("/content/omkar.txt","r") as  source_file, open("/content/omkar.txt","w") as destination_file:
    destination_file.write(source_file.read())

import os

file_path ="/content/preeth.txt"

if os.path.exists(file_path):
    print("The file exists.")
else:
      print("The file does not exisyts.")

if os.path.exists(file_path):
    print("The file exists.")
else:
      print("The file does not exisyts.")


with open("/content/omkar.txt","r") as file:
     for line in file:
         if "python" in line:
             print(line, end="")
             break

import random
random_number = random.randint(1,6)
print("the random number is:", random_number)

import os
import random

print(f"Current working directory: {os.getcwd()}")

numbers = [1, 2, 3, 4, 5]
with open("numbers.txt", "w") as file:
    file.write("\n".join(map(str, numbers)))
