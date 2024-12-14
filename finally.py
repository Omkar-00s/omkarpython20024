try:
  file=open("/content/drive/mydrive/omkar/omkar.txt")
except FileNotFoundError:
  print("File not found.")
try:
  file=open("/content/drive/mydrive/omkar/omkar.txt","r")
except FileNotFoundError:
  print("File not found.")
finally:
  print("Execution complete")



