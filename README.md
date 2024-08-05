# Bubble Sort with Early Termination and Detailed Analysis

This repository contains a Python implementation of the bubble sort algorithm modified to meet specific requirements for an assignment. The goal is to sort an array into ascending order with early termination if no swaps occur during an iteration, along with detailed analysis of each iteration.

# Features
  1.  Iteration Analysis: On each iteration through the outer loop, count the number of comparisons and swaps. Reinitialize these counters to zero at the beginning of each iteration.
  2.  Detailed Output: After each iteration through the outer loop, print the partially sorted array, the number of comparisons, and the number of swaps for that iteration.
  3.  Early Termination: If no swaps occur on an iteration through the outer loop, the array is considered sorted, and the algorithm terminates early.
  4.  Final Statistics: When the algorithm concludes (either after all iterations or early termination), display the total number of comparisons and swaps required to sort the array.

# Problem Instances
The modified bubble sort algorithm is tested on the following arrays:

  -  A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
  -  A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
  -  A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

# Code
The main script bubble_sort.py contains the implementation of the bubble sort algorithm with the required modifications.
