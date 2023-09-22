import math  # підключення бібліотеки


def task_integer1():
  """A distance L is given in centimeters.
  Find the amount of full meters of this distance
  (1 m = 100 cm)"""
  try:  # перевірка на помилки
    length = int(input("L (sm) = "))
  except ValueError:  # якщо помилка
    print("L must be an INTEGER !!!")
    input("Press enter for exit ...")
  else:  # якщо немає помилки
    res = length // 100
    print("L = ", res, "m")


def task2_0():
  """Calculate mathematical expression"""
  try:
    x = float(input("\n(Enter x> 0) x = "))
  except ValueError:
    print("L must be a NUMBER !!!")
    input("Press enter for exit ...")
  else:
    try:
      denum = math.sin(math.pi * x) - x ** 3
      num = math.sqrt(x + math.exp(0.5 * x))
      y = denum / num
    except ZeroDivisionError:
      print("x MUST be positive !!!")
      input("Press enter for exit ...")
    else:
      print("y = ", y)


def task_boolean1():
  """Given integer A,
  verify the following proposition:
  The number A is positive"""
  try:
    A = int(input("A = "))
  except ValueError:
    print("A MUST be integer !!!")
    input("Press enter for exit ...")
  else:
    res = A > 0
    print("A is positive: ", res)


def main():
  """Основна функція для виклику одного із завдань за варіантом"""
  task_num = int(input("Enter task num: "))
  if task_num == 1:
    task_integer1()
  elif task_num == 2:
    task2_0()
  elif task_num == 3:
    task_boolean1()
  else:
    print("Wrong task num")

main()