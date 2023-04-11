# pands-problem-sheet

# Problems 2023


<p>This repository is used for the problem sets given during the Programming and scripting module on Higher Diploma in Data Analytics course from GMIT.\</p>
<p>in Visual Studio Code, I have added source files for code, and also added comments to explain work</p>
</p><em>As I was unable to install all software until wk06, pushing my work to Github is non existent for the initial weeks of course.</em></p>
<p>for this markup sheet, I used the following websites.
<p><a href="#">https://www.markdownguide.org/basic-syntax</a></p>
<p><a href="#">https://www.w3schools.io/file/markdown-cheatsheet/</a></p>

# **Table of contents**
* [Weekly tasks](weekly-tasks)
    1. [Hello World](#HelloWorld)
    2. [Bank](#Bank)
    3. [Accounts Masked Number](#accounts)
    4. [Collatz](#collatz)
    5. [Weekday](#Weekday) 
    6. [Square root](#square-root)
    7. [es](#es)
    8. [Plottask](#plottask)


# HelloWorld! #
<h2> Wk 01 Task: Hello World!.py </h2>
<p>Write a program that outputs <em>"Hello World!"</em></p>
<h3> Output Expected </h3>    
<p>This file should contain a python program that displays <em>Hello World!</em> when it is run. </p>
<h3> Assumptions </h3>
<p>N/A</p>
<h3>Instructions to run progrgam </h3>
<ol>
<li>run python helloworld.py</li>
<li>program prints Hello World! in Terminal</li>
</ol>

# Bank #
<h2> Wk 02 Task: Bank.py </h2>
<p>Write a program called bank.py </p>
<p>The program should:</p>
<p>Prompt the user and read in two money amounts (in cent)</p>
<p>Add the two amounts</p>
<p>Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount</p>
<h3> Output Expected </h3>
<p>Enter amount1(in cent): 65</p>
<p>Enter amount2(in cent): 180<p>
<p>The sum of these is €2.45</p>
<h3> Assumptions </h3>
<li> User must enter positive number, otherwise exception</li>
<li> User must not enter symbols, otherwise exception</li>
<h3>Instructions to run progrgam </h3>
<ol>
<li>run python bank.py</li>
<li>enter first number</li>
<li>enter second number</li>
<li>program prints sum of number1 & number 2 in Terminal</li>
</ol>

# accounts #
<h2> Wk 03 Task: Accounts.py </h2>
<p>Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).</p>
<h3>  Output Expected </h3>
<p>Please enter an 10 digit account number: 1234567890
XXXXXX7890</p>
<h3> Extra: </h3>
<p>Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)</p>
<p><em>Program will run as long as more than 4 characters are entered.</em></p>
<h3> Assumptions </h3>
<li> Number entered must be greater than 4 characters otherwise exception called</li>
<li> Any number with > than 4 characters will have last 4 characters masked</li>
<li> User must not enter symbols, otherwise exception</li>
<h3>Instructions to run progrgam </h3>
<ol>
<li>run python accounts.py</li>
<li>enter 10 digit number</li>
<li>program prints masked string in Terminal</li>
</ol>

# collatz #
<h2> Wk 04 Task: collatz.py </h2> 
<p>Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.</p>
<p>At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.<,p>
<p>Have the program end if the current value is one.</p>
<h3>  Output Expected </h3>
<p>Please enter a positive integer: 10</p>
</p>10 5 16 8 4 2 1 </p>  
<h3> Assumptions </h3>
<li> User must enter positive number, otherwise exception
<li> User must not enter symbols, otherwise exception
<h3>Instructions to run progrgam </h3>
<ol>
<li>run python collatz.py</li>
<li>enter positive number</li>
<li>program prints output in Terminal</li>
</ol>

# Weekday #
<h2> Wk 05 Task: weekday.py </h2> 
<p>Write a program that outputs whether or not today is a weekday.</p>
<h3>  Output Expected </h3>
<p>An example of running this program on a Thursday is given below.</p>
<p>Yes, unfortunately today is a weekday.</p>        
<p>An example of running it on a Saturday is as follows:
<p>It is the weekend, yay!</p>
<h3> Assumptions </h3>
<p>N/A</p>
<h3>Instructions to run progrgam </h3>
<ol>
<li>run python weekday.py</li>
<li>program prints output</li>
</ol>

# Square root #
<h2> Wk 06 Task: weekday.py </h2> 
<p>Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.</p>
</p>You should create a function called <tt>sqrt</tt> that does this.</p>
<p>I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).</p>
<h3>  Output Expected </h3>
<p>Please enter a positive number: 14.5</p>
<p>The square root of 14.5 is approx. 3.8.</p> 
<h3> Assumptions </h3>
<li><em>output formatted to 1 decimal place as per screenshot question</em></li>
<li>User must enter positive number, otherwise exception</li>
<li>User must not enter symbols, otherwise exception</li>
<h3>Instructions to run progrgam </h3>
<ol>
<li>run python squareroot.py</li>
<li>enter positive number</li>
<li>program prints output to <em>1 decimal place</em></li>
</ol>
  
# es #
<h2> Wk 07 Task: es.py </h2> 
<p>Write a program that reads in a text file from the command line and outputs the number of e's it contains.</p>
<h3>  Output Expected </h3>
<p>python es.py moby-dick.txt</p>
<p>116960</p>
<h3> Assumptions </h3>
<li>both uppercase and lower case es are counted</li>
<li>User must enter valid filename from command line</li>
<h3>Instructions to run progrgam </h3>
<ol>
<li>run python es.py SampleFile.txt</li>
<li>program prints count of number of <em>e's</em> & <em>E's</em>
</ol>
  
# plottask #
<h2> Wk 08 Task: plottask.py </h2> 
<p>Write a program called plottask.py that displays:</p>
*  a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2,
*  and a plot of the function  h(x)=x3 in the range [0, 10], Write a program that reads in a text file and outputs the number of e's it contains.
<p>on the one set of axes.</p>
<h3>  Output Expected </h3>
<p>display appears when program is run</p>
<h3> Assumptions </h3>
<p>N/A</p>
<h3>Instructions to run progrgam </h3>
<ol>
<li>run python plottask.py</li>
<li>program displays hist/plot</li>
</ol>