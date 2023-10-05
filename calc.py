print("Jerry's Simple Arithmetic Calculator")
while True:
 first =float(input("First Number"))
 numberone=first
 second =float(input("Second Number"))
 numbertwo =second
 type =input("Add(A), divide(d), multiply(w), or subtract?(s)  ")
 which=type

 if which == 'a':
  answer = int(numberone) + int(numbertwo)
  print(answer)
 elif which == 'd':
  answer = int(numberone) / int(numbertwo)
  print(answer)
 elif which == 'w':
  answer = int(numberone) * int(numbertwo)
  print(answer)
 elif which == 's':
  answer = int(numberone) - int(numbertwo)
  print(answer)