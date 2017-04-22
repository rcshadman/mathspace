Question
-----------------------------------
B. Write a program that calculates the probability for an n-sided die labelled with integers from 1 to n, to roll all the numbers {1, ..., n}, in any order if the die is thrown n times

e.g. A tetrahedral die can be made from four equilateral triangles. If the sides are labelled 1, 2, 3 and 4, what is the probability of throwing the die four times and getting {1, 2, 3, 4} in any order?

Investigate how your program scales for moderately large numbers, such as n=1000.


Solution
-----------------------------------

Instead of googling  probability's formulas,lets derive our equation using a crude method of mathematical induction.

So let's start with the 2 sided die,

side = 2 ie {1,2}

number of rolls = 2 

all possibilities or samples = 2^2 =4 ie {11,12,21,22}

number of ways dinstinct face can appear = in 2 ways = 2! = 2 ie {12,21}

Probability = 2!/2^2










side = 3 
---------

ie {1,2,3}

number of rolls = 3 

all possibilities or samples = 3^3 =27 

ie [ 111,112,113, 121,122,123, 131,132,133, 211,212,213, 221,222,223, 231,232,233, 311,312,313, 321,322,323, 331,332,333 ] 

fnumber of ways dinstinct face can appear 3! = 6 ie [ 123,132,213,231,312,321 ] 

probability = 3!/3^3










side = 4 
----------

number of rolls = 4

all possibilities or samples = 4^4 = 16 

number of ways dinstinct face can appear = 4! = 24 

ie [ 1234,1243,1324,1342,1423,1432, 2134,2143,2314,2341,2413,2431, 3124,3142,3214,3241,3412,3421 ..... ] 


probability = 4!/4^4








side = 5 
---------

number of rolls = 5 

sample = 5^5 = 25 

number of ways dinstinct face can appear = 5! 

probability = 5!/5^5










Therefore , for side n and roll n:

sides = n 
----------


number of rolls = n 

sample = n^n 

number of ways dinstinct face can appear = n! 

probability = n!/n^n

P(e) = n!/n^n = n(n-1)!/n(n^n-1) = (n-1)!/(n^n-1)








Formulae
----------

P(E) = (n-1)! / n^n-1


The Real Problems
-----------------------------------

Implementing the equation will result into memory overflow, or buffer overflow because primitive datatypes of the language often has limitation (max range). More over floating points operations are extremely exahustive.

Solution
-----------------------------------

Lets approach the problem from a layman's perspective.

Do we really need to divide the such huge numbers?

FACT 1
-------
1/1000 is same as 523/523000  and 523000/523000000

FACT 2
--------
625/7869900768687 = ~ = 62 / 786990076868 = ~ =  6 / 78699007686 
These are approximately equal.



Using this analogy, when n = 15 in p(E) = (n-1)! / n^(n-1)

numerator = (n-1)! = 14! = 87178291200 
---------------------------------------

denominator = n^(n-1) = 15^14 = 29192926025390625
--------------------------------------------------

p(E) 
-----
0.0000029862813725549966110419351783544783529578126035630702972412109375


So do we need such high precision? if we just consider first 100 decimal places, we have fairly correct answer.
To verify our approach, lets truncate just 5 digits of decimal digits from the numnerator and denominator and check it makes a signification difference to the result. we will call this 'normalizing_factor'

numerator = (n-1)! = 14! = 871782 
-----------------------------------

denominator = n^(n-1) = 15^14 = 291929260253 
---------------------------------------------

P(E)
-----
0.000002986278248519766919354123668739475760958157479763031005859375 


we still get exactly correct value uptil 10 decimal positions, ie ( 0.0000029862 ) 
If we round off the both values at 11th position, we will have exact same answer.
we escape the memory limitation at the cost of precision.

I have considered 8 digit precision.
First 8 digits of numerator are kept and removed the remaining. ie (no of digits in numerator - 8)digits =>normalizing_factor. In denominator we have removed (no of digits in numerator - 8)digits from right.
As the value of n grows bigger, our denominator grows exponentially and our normalizing factor isnt sufficient to deal with buffer-overflow problem. There we introduce the an adjustment number to furthur increase normalizing digits.


This method might not be mathematically absolutely accurate to max precision but will give us a rough estimate of
significant digits in the answer


#Conclusion
-----------

So is this approach correct ? I am not sure, but if a small hack can save time and effort,
I would use till it cracks.


#Comment
---------

I have chosen second question mainly because, 1st and 3rd are too frequently asked problems. 
1st problem can solved using Dynamic programming (although doesnt cover corner cases) or recursive DFS method (lenghty).
2nd problem , I couldnt figure out the function being used to generate the values for string.









