mystr = 'dileep'

mydict_chars = {x: mystr.count(x) for x in mystr}

print(mydict_chars)


def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

 

print(myfunc1())

 



def myfunc1():
  x = "John"
  def myfunc2():
    x = "hello"
  myfunc2() 
  return x

 

print(myfunc1())



lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 
50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 
97, 98, 99]




Input: x = 123
Output: 321

x = 123



# Output: 321
 

# Input: x = -123
# Output: -321

 

# Input: x = 120
# Output: 21