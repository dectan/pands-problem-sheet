# pands-problem-sheet

# Problems 2023


This repository is used for the problem sets given during the Programming and scripting module on Higher Diploma in Data Analytics course from GMIT.\

I have previous completed the higher diploma in software deveolment in GMIT, & so even though Python wasnt taught, the basics were knowledge between different languages

As I was unable to install all software until wk06, pushing my work to Github is non existent for the initial weeks of course.
Link to 
https://www.markdownguide.org/basic-syntax






# **Table of contents**
* [Weekly tasks](weekly-tasks)
    1. [Hello World](#HelloWorld)
    2. [Bank](#Bank)
    3. [Accounts Masked Number](#accounts)
    4. [Collatz](#collatz)
    5. [Weekday](#Weekday) 
    6. [Square root](#square-root)
    7. [Square root](#es)
    8. [Plot](#plottask)


Weekly tasks
======
<h1> ***HelloWorld!*** </h>
<h2> Wk 01 Task: Hello World!.py </h2>
<p>Write a program that outputs "Hello World!"</p>
<h3> Output Expected </h3>    
<p>This file should contain a python program that displays **Hello World!** when it is run. </p>
<h3> Assumptions </h3>
<p>N/A</p>

<h1> ***Bank*** <h1>
<h2> Wk 02 Task: Bank.py </h2>
<p>Write a program called bank.py </p>
<p>The program should:
Prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount</p>
<h3> Output Expected </h3>
<p>Enter amount1(in cent): 65
Enter amount2(in cent): 180
The sum of these is €2.45</p>
<h3> Assumptions </h3>
<li> User must enter positive number, otherwise exception</li>
<li> User must not enter symbols, otherwise exception</li>

<h1> ***accounts*** </h1>
<h2> Wk 03 Task: Accounts.py </h2>
<p>Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).</p>
<h3>  Output Expected </h3>
<p>Please enter an 10 digit account number: 1234567890
XXXXXX7890</p>
<h3> Assumptions </h3>
<li> Number entered must be 4 characters otherwise number entered by user will be returned</li>
<li> User must not enter symbols, otherwise exception</li>

<h1> ***collatz*** </h1>
<h2> Wk 03 Task: Accounts.py </h2> 
<p>Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.</p>
<h3>  Output Expected </h3>
<p>Please enter a positive integer: 10</p>

</p>10 5 16 8 4 2 1 </p>
        
<h3> Assumptions </h3>
<li> User must enter positive number, otherwise exception
<li> User must not enter symbols, otherwise exception

  ### ***Weekday***

Write a program that outputs whether or not today is a weekday.


<details>
          
<p>An example of running it on a Saturday is as follows:

It is the weekend, yay!

</p>
</details>



  ### ***Square root***

    Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
<p> code working in excel</p>

<p>
Step	Number	x	y	Difference	Absolute	Tolerance
1	14.300000000	7.150000000	4.575000000	-2.575000000	2.575000000	FALSE
2	14.300000000	4.575000000	3.850341530	-0.724658470	0.724658470	FALSE
3	14.300000000	3.850341530	3.782148891	-0.068192639	0.068192639	FALSE
4	14.300000000	3.782148891	3.781534130	-0.000614761	0.000614761	FALSE
5	14.300000000	3.781534130	3.781534080	-0.000000050	0.000000050	TRUE

</P>


<p>output rounded to 1 decimal place as per screenshot of output in question</p>
<details>
           
           <p>


</p>
</details>

Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

  
   ### ***es***

    Write a program that reads in a text file and outputs the number of e's it contains. 






<details>
           <summary></summary>
           <p>


</p>
</details>

The program should take the filename from an argument on the command line.

  
  ### ***plottask***

    Write a program called plottask.py that displays:

a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range [0, 10], Write a program that reads in a text file and outputs the number of e's it contains. 






<details>
           <summary></summary>
           <p>


</p>
</details>



