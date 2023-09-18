import math
i = 0
while i == 0:
   print("Выберите действие:")
   print("Сложение (+)")
   print("Вычитание (-)")
   print("Умножение (*)")
   print("Деление (/)")
   print("Возведение в степень (**)")
   print("Извлечение корня (v)")
   print("Факториал числа (!)")
   print("Синус числа (sin)")
   print("Косинус числа (cos)")
   print("Тангенс числа (tan)")
   print("Закончить программу (///)")
   act = str(input("Действие: "))
   if (act == "+") or (act == "-") or (act == "*") or (act == "/") or (act == "**") or (act == "v") or (act == "!") or (act == "sin") or (act == "cos") or (act == "tan")  or (act == "///"):
           match act:
               case "+":
                   a = (input("Введите первое число: "))
                   b = (input("Введите второе число: "))
                   try:
                       A1 = float(a)
                       B1 = float(b)
                       ans = (A1 + B1)
                       print(ans)
                       print(" ")
                   except ValueError:
                       print("Введено некорректное значение")
                       print(" ")
               case "-":
                   a = (input("Введите первое число: "))
                   b = (input("Введите второе число: "))
                   try:
                       A1 = float(a)
                       B1 = float(b)
                       ans = (A1 - B1)
                       print(ans)
                       print(" ")
                   except ValueError:
                       print("Введено некорректное значение")
                       print(" ")
               case "*":
                   a = (input("Введите первое число: "))
                   b = (input("Введите второе число: "))
                   try:
                       A1 = float(a)
                       B1 = float(b)
                       ans = (A1 * B1)
                       print(ans)
                       print(" ")
                   except ValueError:
                       print("Введено некорректное значение")
                       print(" ")
               case "/":
                   a = (input("Введите первое число: "))
                   b = (input("Введите второе число: "))
                   try:
                       A1 = float(a)
                       B1 = float(b)
                       if b != 0:
                           ans = (A1 / B1)
                           print(ans)
                           print(" ")
                       else:
                           print("Введено некорректное значение")
                           print(" ")
                   except ValueError:
                       print("Введено некорректное значение")
                       print(" ")
               case "**":
                   a = (input("Введите число: "))
                   b = (input("Введите степень: "))
                   try:
                       A1 = float(a)
                       B1 = float(b)
                       ans = (A1 ** B1)
                       print(ans)
                       print(" ")
                   except ValueError:
                       print("Введено некорректное значение")
                       print(" ")
               case "v":
                   a = (input("Введите число: "))
                   try:
                       A1 = float(a)
                       if A1 >= 0:
                           ans = math.sqrt(A1)
                           print(ans)
                           print(" ")
                       else:
                           print("Введено некорректное значение")
                           print(" ")
                   except ValueError:
                       print("Введено некорректное значение")
                       print(" ")
               case "!":
                   a = (input("Введите число: "))
                   try:
                       A1 = int(a)
                       if A1 >= 0:
                           ans = math.factorial(A1)
                           print(ans)
                           print(" ")
                       else:
                           print("Введено некорректное значение")
                           print(" ")
                   except ValueError:
                       print("Введено некорректное значение")
                       print(" ")
               case "sin":
                   a = (input("Введите число: "))
                   try:
                       A1 = float(a)
                       ans = math.asin(A1)
                       print(ans)
                       print(" ")
                   except ValueError:
                       print("Введено некорректное значение")
                       print(" ")
               case "cos":
                   a = (input("Введите число: "))
                   try:
                       A1 = float(a)
                       ans = math.acos(A1)
                       print(ans)
                       print(" ")
                   except ValueError:
                       print("Введено некорректное значение")
                       print(" ")
               case "tan":
                   a = (input("Введите число: "))
                   try:
                       A1 = float(a)
                       ans = math.tan(A1)
                       print(ans)
                       print(" ")
                   except ValueError:
                       print("Введено некорректное значение")
                       print(" ")
               case "///":
                   break
   else:
       print("Введено некорректное действие")
       print(" ")
