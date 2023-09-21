import math # підключення бібліотеки

def task_integer1():
  """A distance L is given in centimeters.
  Find the amount of full meters of this distance
  (1 m = 1000 cm)"""
  try: # перевірка на помилки
    l = int(input( "L (sm) = "))
  except: # якщо помилка
    print( "L must be an INTEGER !!!")
    input( "Press enter for exit ...")
  else: # якщо немає помилки
    res = l // 100
    print( "L = ", res, "m")


def task2_0():
  """Calculate mathematical expression"""
  print( " sin px - x ^ 3")
  print( "y = _________________")
  print( " ________________")
  print( " V x + e ^ (x / 2)")
  try:
    x = float(input("(Enter x> 0) x = "))
  except:
    print("L must be a NUMBER !!!")
    input( "Press enter for exit ...")
  else:
    try:
      y = (math.sin(math.pi * x) - x ** 3) / \
      math.sqrt(x + math.exp(0.5 * x))
    except:
      print( "x MUST be positive !!!")
      input( "Press enter for exit ...")
    else:
      print( "y = ", y)


def task_boolean1():
  """Given integer A,
  verify the following proposition:
  The number A is positive"""
  try:
    A = int (input( "A = "))
  except:
    print("A MUST be integer !!!")
    input("Press enter for exit ...")
  else:
    res = A> 0
    print( "A is positive: ", res)