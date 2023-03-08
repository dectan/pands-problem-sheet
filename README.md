# pands-problem-sheet

# Problems 2023


This repository is used for the problem sets given during the Programming and scripting module on Higher Diploma in Data Analytics course from GMIT.\

I have previous completed the higher diploma in software deveolment in GMIT, & so even though Python wasnt taught, the basics were knowledge between different languages


## Table of contents
* [Weekly tasks](#weekly-tasks)
    * [Hello World](#HelloWorld)
    * [Bank](#Bank)
    * [Accounts Masked Number](#AccountsMaskedNumber)
    * [Collatz](#collatz)
    * [Weekday](#weekday)
    * [Square root](#square-root)


Weekly tasks
======
### ***HelloWorld***

    Write a program that outputs "Hello World 
    

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :


  ### ***Bank***


    Write 



###***Accounts Masked Num***



  ### ***Collatz***
    
    Write a program that asks the user to input any positive integer and outputs the successive 
    values of the following calculation. At each step calculate the next value by taking the 
    current value and, if it is even, divide it by two, but if it is odd, multiply it by three 
    and add one. Have the program end if the current value is one.

Even though the task didn't require to have a fix for wrongly inputed negative number, it's added to avoid errors. This is done with *while* loop.

In second *while* loop we are cheching whether a number is odd or even, with the help of conditional statements *if* and *else* and it's doing so until the current value is one.\
The statement *if* checks if the number is even using modulus operation. If the remainder of the operation is zero, the number is even and the program divides the number by 2 and prints it out.\
If the remainder is not zero, program performs operations from statement *else* - multiplying the number by three and adding one, and prints out the result.

The output of the program looks neater if it's written in one line. That is done with the help of *end = " "* parameter, and the reference goes to [Geeksforgeeks.org](https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/).

<details>
           <summary>User point of view</summary>
           <p>
         
User call of the program is :

```
λ python 4-collatz.py
```
User input :
```
Add any positive integer: -20
```
In case of putting in a negative integer the program will respond with a message that a number is negative and ask to input a positive integer until the input is correct:
```
Add any positive integer: -10
-10 isn't a positive integer.
Add any positive integer: -20
-20 isn't a positive integer.
Add any positive integer: 20
```

When user inputs the positive integer the output is :

```
20 10 5 16 8 4 2 1
```
</p>
</details>

----








  ### ***Weekday***

    Write a program that outputs whether or not today is a weekday.

For this program it is neccessary to import *datetime* module so we can manipulete date and time.



<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :


</p>
</details>

----

  ### ***Square root***

    Write a program that takes a positive floating-point number as input and outputs an 
    approximation of its square root.
    You should create a function called sqrt that does this.

Addition to the task: 
    
    The weekly task is trickier than the previous ones but I really suggest you try to crack it.
    You'll find a simple algorithm for the problem if you Google "Newton's method for square roots".
    I really recommend trying to code it up yourself rather than looking at others' implementations.





<details>
           <summary>User point of view</summary>
           <p>


</p>
</details>

- - - -

  