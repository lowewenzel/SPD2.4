Code out 2 solutions for each of the 3 problems. Use your pseudocode to guide your comments. 
Problem 1
Given an array a of n numbers and a target value t, find two numbers whose sum is t.
Example: a=[5, 3, 6, 8, 2, 4, 7], t=10 ⇒ [3, 7] or [6, 4] or [8, 2]

Set hash to {}
For each value k in the array
	If the sum t - k is in the hash, return k and t - k
 

Problem 2
Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3 ⇒ [6, 8, 7]

If k is larger than length of a, return an error
Sort the array
Return a slice of the last k elements

Problem 3
Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
Example: a=[9, 13, 1, 8, 12, 4, 0, 5], b=[3, 17, 4, 14, 6], t=20 ⇒ [13, 6] or [4, 17] or [5, 14]

TIPS:
Remember your simplification strategies to help you strategize, simplify, and break apart your code into smaller chunks.
Pseudocode before you code! Use resources from class to write good pseudocode and use that as comments as you code.
Test your code! Write test cases to debug your code. Think of edge cases.

