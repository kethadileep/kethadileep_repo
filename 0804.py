# How to swap first element with seventh element in a python list

mylist = [1,2,3,5,6,7,8,9,10,11]

for i in range(len(mylist)):
    for j in range(len(mylist)):
        if i == 0 and j==7:
            mylist[j], mylist[i] = mylist[i], mylist[j]

print(mylist)


# write a function that will check if any character are repeating itself in the given string,that will return True if matches and return False if not matches.

mystr = 'helo'
# print(mystr.count('e'))

# print({i: 'true' if mystr.count(i)> 1 else 'false' for i in mystr})

def myfunc(myarg):
    for i in myarg:
        if myarg.count(i) >1:
            return 'true'

    else:
        return 'false'
        
print(myfunc(mystr))

# Find out pairs of those numbers from the given list whose sum will be equal to target sum?
list1=[1,2,3,4,5,6,7,8,9]
target_sum=9
output = []
for i in list1:
    for j in list1:
        if i+j == target_sum:
            mytup = (i,j)
            if not (j,i) in output:
                output.append(mytup)
# print(output)

# write a python program that will convert lower to upper case without using any inbuilt function?

mydict = {'a':'A', 'b':'B','c':'C'}

mystr = ['a','b','c']

for i in mystr:
    mystr[mystr.index(i)] = mydict[i]
print(mystr)


import {useState} from 'react';

# export mycompo =() => {

    const [count, setCount] = usestate();

    onClickHandler = () => {
        setCount
    }
#     submitHander = () => {
#     }

# return {
#     <form onSubmit= {submitHander}> 
#     <lable>'myname'</lable>
#     <input type='text' onClick= {onClickHandler}>  </input>
#     <button></button>
#     </form>

# }


import Component from react

class Myclass extends react.Component {
    constructor (name, age) {
        this.name = name;
        this.age = age;

    }
    render {
        <>
        <p> {this.name} </p>
        <p> {this.age} </p>
        </>
    }

}


mycompo =() => {

    const [count, setCount] = usestate();
  
    return {
      <p> ${count}</p>
      <button onClick={() => setCount('new')}> click me</button>
    }
}

mouting, updating, unmouting


setState,


SELECT SALARY FROM MYTABLE ODER BY SALARY DESC WHERE ID ==3;



















