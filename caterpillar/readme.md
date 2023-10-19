Caterpillar Coding Questions (Consolidated)

-----------------------------------------------------------

Question : 01
--------------
Given a String S, find the number of characters resides in the same position after reversing a String S.

Test Case : 01		Test Case : 02

Input :			Input :
S = 'encyclopedia'	S = 'abcdecba'

Output :		Output : 
0			6

-----------------------------------------------------------

Question : 02
--------------
In a given array A of size n, club the values of size k (from start to end in a sequence) and find out the first negative number in each pair of size k. (If no negative value is present in a clubbed pair consider it as 0).

Test Case : 01

Input :
n = 8
A = [-10, -5, 4, 0, -3, 2, 1, 4]
k = 3

Output :
[-10, -5, -3, -3, 0]

-----------------------------------------------------------

Question : 03
--------------
In a given array A of size n, find out the position at which that particular index value is present in a original array A. 

Test Case : 01

Input :
n = 6
A = [1, 4, 5, 2, 0, 3]

Output :
[4, 0, 3, 5, 1, 2]

-----------------------------------------------------------

Question : 04
--------------
From a given array of Strings S find out the Longest common prefix among all n string.

Test Case : 01

Input :
n = 3
S = ['Ram', 'Ramanathan', 'Ramesh']

Output :
'Ram'

-----------------------------------------------------------

Question : 05
--------------
Given a String S, return the number of special characters present in the String (space is a not a Special Character).

Test Case : 01

Input :
S = 'mca@2022 #23.89'

Output :
3

-----------------------------------------------------------

Question : 06
--------------
Given a array A of numbers of size n, return an array containing the alternate numbers after sorting the given array A.

Test Case : 01

Input :
n = 7
A = [6, 5, 4, 2, 1, 3, 7]

Output :
[1, 3, 5, 7]

-----------------------------------------------------------

Question : 07
--------------
Given a array A of numbers of size n, return a sum of alternative numbers after sorting the given array A.

Test Case : 01

Input :
n = 7
A = [6, 5, 4, 2, 1, 3, 7]

Output :
16

-----------------------------------------------------------

Question : 08
--------------
Sender sends a number S and receiver receives a number R. During the intermdiate transfer of number, that may be interrupted and modified. Find the error occurrence between sender and receiver.

Test Case : 01			Test Case : 02

Input :				Input :
S = 5				S = 5
R = 9				R = 8

Output :			Output :
2				3

-----------------------------------------------------------

Question : 09
--------------
Return a string by removing all the vowel characters present in the Input String S.

Test Case : 01

Input :
S = 'Encyclopedia'

Output :
'ncyclpd'

-----------------------------------------------------------

Question : 10
--------------
In a given array A of size n, with the start and end value, find out the numbers which resides inbetween start and end value. (Inclusive of start and end)

Test Case : 01

Input :
n = 9
A = [10, 15, 12, 11, 5, 3, 2, 4, 7]
start = 2
end = 10

Output :
[10, 5, 3, 2]

-----------------------------------------------------------

Question : 11
--------------
In a given array A of size n and a value k, arrange first k elements in the Ascending order and remaining elements in the Descending order.

Test Case : 01

Input :
n = 10
A = [9, 5, 2, 1, 4, 3, 0, 7, 6, 8]
k = 5

Output :
[1, 2, 4, 5, 9, 8, 7, 6, 3, 0]

-----------------------------------------------------------

Question : 12
--------------hr
Scenario based Question :
Distance of Parent from Home : 3 M	Distance of Child from Home : 2 M
Velocity of Parent : 2 M/Step
Number of steps walked by Parent : 20 Steps

Find out the Velocity of Child and the number of common steps that Parent and Child meet together.
(Not clear with the Question)

Reference Link : https://brainly.in/question/43383542

-----------------------------------------------------------

Question : 13
--------------
Given a number n (long data type), return a smallest possible number by interchanging the digits among the number (all digits should present in the final number).

Test Case : 01

Input :
n = 310

Output :
103

-----------------------------------------------------------

Question : 14
--------------
Given a string S, return a count of unique characters present in a string S.

Test Case : 01

Input :
S = 'encyclopedia'

Output :
8

-----------------------------------------------------------

Question : 15
--------------
Find out the Area of intersection of Two Circles.

Input : 
Circle 1 : Co-Ordinate (x1,y1), radius r1
Circle 2 : Co-Ordinate (x2,y2), radius r2

Output :
Area

-----------------------------------------------------------

Question : 16
--------------
Given a number n (long data type), and a value k, Find the number of occurrences a value k in number n.

Test Case : 01

Input :
n = 123345534
k = 3

Output :
3

-----------------------------------------------------------

Question : 17
--------------
In a given array A of size n, make the resultant array containging all the even numbers comes first followed by the odd number. (Relative position of the numbers to be considered).

Test Case : 01

Input :
n = 6
A = [5, 4, 1, 6, 3, 2]

Output :
[4, 6, 2, 5, 1, 3]

-----------------------------------------------------------

Question : 18
--------------
Employees in a compaany are put into work in projects with N nnumber of modules.
Employee do not work on the same project more than a week.
1 module of a project must be completed in one week.
Find out the maximum number of consecutive weeks that the employee can work on these projects satisfing above conditions.

Test Case : 01			Test Case : 02

Input :				Input :
3				4
7 2 3				2 2 2 2

Output : 			Output :
11				8

-----------------------------------------------------------

Question : 19
--------------
In a given array A of size n, return number of negative elements present in a array A.

Test Case : 01

Input :
n = 7
A = [-3, 7, 0, -8, -2, 1, -4]

Output :
4

-----------------------------------------------------------

Question : 20
--------------
Given a array A of size n, return same array of size n that containing the values as sum of digits inside each value in a original array (at each Index).
(Should not use any external array).

Test Case : 01

Input :
n = 4
A = [64, 123, 45, 10, 5]

Output :
[10, 6, 9, 1, 5]

-----------------------------------------------------------

Question : 21
--------------
Given a array A of size n, contains only 0's and 1's. Check with its previous and next value of each index (If those values are same then consider it as 0, if they are different then consider it as 1). Assume previous and next value of first and last index to be 0 respectively.

Test Case : 01

Input :
n = 7
A = [1, 0, 1, 0, 0, 0, 1]

Output :
[0, 0, 0, 1, 0, 1, 0]

-----------------------------------------------------------

Question : 22
--------------
A company has a sales record of N products for M days. The company wishes to know the maximum revenue received from a given product of the N products each day. Write an algorithm to find the highest revenue received each day.

Input

The first line of the input consists of two space-separated integers- days and products, representing the days (M) and the products in the sales record (N), respectively.

The next M lines consist of N space- separated integers - salesRecord, representing the grid of sales revenue (can be positive or negative) received from each product each day.


Output

Print M space-separated integers representing the maximum revenue received each day.

Example

Input:

3 4

100 198 333 323

122 232 221 111

223 565 245 764

Output:

333 232 764

Explanation:

The maximum revenue received on the first day is 333, followed by a maximum revenue of 232 on the second day and a maximum revenue of 764 on the third day.
