# Simple Data Structures and Algorithms
These are exercises done as part of the Udacity Data Structures and Algorithms in Python course

## Queues (queue.py)
* A queue is a first in first out (FIFO) data structure
* One can enqueue (push) to the end of the queue
* One can dequeue (pop) from the front of the queue
* Push and Pop in O(1)
* Can implement a Queue object using a Python list
* Could also use a Python deque, which allows enqueueing and dequeueing from both ends - `from collections import deque`

## Hashing (hashing.py)
* Create HashTable object using Python list
* Hashing strings, particularly the first two letters of string
* Bucket size 10,000
* Load factor is % of table filled
* Hash value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
* O(1) Lookup

## Binary Search (binary_search.py)
* Iterative binary search on Python list
* Assumes data is sorted
* O(log n) search

## Trees (A type of graph)
* Connected graphs, acyclic, directed
* Root (top node, first node)
* Parent and child
* Leaf is a bottom node
* If node doesn't point to other node, usually points to Null (None)
* Traversing is done recursively

## Binary Tree (binarytree.py)
* Each parent has at most 2 children
* Height is log n
* Implement preorder (LRN) search and print
* Comprised of Node objects that contain the value and left, right child pointers

## Binary Search Tree (bst.py)
* Left child < parent
* Right child > parent
* Search is O(log n), the height of the tree
* In-order traversal is sorted order
* Can degrade to looking like linked list => O(n) search in worst case
* Enter self-balancing trees (AVL, Red-black)

## Graph (graph.py)
* Node class contains value and list of edges connected to that node
* Edge class contains value, references to node from and node to
* Graph class contains list of nodes and list of edges
* Insert node is simple
* Insert edge is a little more complicated.
* Get representation of edge list, adjacency list, and adjacency matrix

## Graph (graph2.py)
* Here I implemented DFS (recursive) and BFS (iterative)
* The rest of the code was written by Udacity
