I would like to attempt the second question mainly because, 1st and 3rd are too frequently asked problems. 
1st problem can solved using Dynamic programming (although doesnt cover corner cases) or recursive DFS method (lenghty).
2nd problem , i couldnt figure out the function being used to generate the values for string.

B. Write a program that calculates the probability for an n-sided die labelled with integers from 1 to n, to roll all the numbers 
{1, ..., n}, in any order if the die is thrown n times.

e.g. A tetrahedral die can be made from four equilateral triangles. If the sides are labelled 1, 2, 3 and 4, what is the probability of throwing the die four times and getting {1, 2, 3, 4} in any order?

Investigate how your program scales for moderately large numbers, such as n=1000.
-----------------------------------
ANSWER
-----------------------------------

I definetiely dont remember all the probability formalaes 
Instead of googling it,lets derive equation using a crude method of  mathematical induction.

So lets start with the 2 sided die,

side = 2 ie {1,2}
number of rolls = 2
all possibilities or samples = 2^2 =4 ie {11,12,21,22} 
face can appear in 2 ways = 2! = 2 ie  {12,21}
Probablity = 2!/2^2

side = 3 ie {1,2,3}
number of rolls = 3 
all possibilities or samples = 3^3 =27 ie [
											111,112,113, 121,122,123, 131,132,133, 
											211,212,213, 221,222,223, 231,232,233,
											311,312,313, 321,322,323, 331,332,333
											]
faces can appear 3! = 6 ie [ 123,132,213,231,312,321 ] 
probability = 3!/3^3

side = 4
number of rolls = 4
all possibilities or samples =  4^4 = 16 
faces can appear = 4! = 24 ie [ 1234,1243,1324,1342,1423,1432, 2134,2143,2314,2341,2413,2431, 3124,3142,3214,3241,3412,3421 ..... ]
probabilty = 4!/4^4

side = 5
number of rolls = 5
sample = 5^5 = 25
face can appear = 5!
probability = 5!/5^5

Therefore , for side n and roll n:
side = n
number of rolls = n
sample = n^n
face can appear = n!
probability = n!/n^n

P(e) = n!/n^n = n(n-1)!/n(n^n-1) = (n-1)!/(n^n-1)

P(E) = (n-1)! / n^n-1





