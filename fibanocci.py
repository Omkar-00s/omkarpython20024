def fibonaccin(n):
  sequence =[]
  a,b=0,1
  for _ in range(n):
    sequence.append(a)
    a,b=b,a+b
    return sequence
terms=int(input("Enter the number of terms"))
print("fibonacci sequence:",fibonaccin(terms))
