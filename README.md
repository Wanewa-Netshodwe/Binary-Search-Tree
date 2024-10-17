# Binary Search Tree (BST) Implementation in Python

A simple implementation of a **Binary Search Tree (BST)** in Python. This project demonstrates the essential operations of a binary search tree, including insertion, searching, finding minimum/maximum values, calculating tree height, and comparing two trees for equality.

## Features

- Insert values into the tree.
- Search for a value in the tree.
- Find the minimum and maximum values in the tree.
- Calculate the height of the tree.
- Compare two trees for structural and value equality.
- Retrieve all nodes at a specific distance from the root.
- Count the total number of edges in the tree.

## Installation

Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/your-username/binary-search-tree.git
cd binary-search-tree
```
## Usage
```bash
# Import the BinarySearchTree and node classes
from bst import BinarySearchTree

# Initialize the tree
tree = BinarySearchTree()

# Insert values into the tree
tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(3)
tree.insert(7)

# Search for values in the tree
print(tree.find(10))  # Output: True
print(tree.find(15))  # Output: False

# Get the height of the tree
print(tree.height())  # Output: 2

# Find the minimum and maximum values
print(tree.min())  # Output: 3
print(tree.max())  # Output: 20

# Get nodes at a specific distance from the root (distance = 1)
print(tree.getNodesAtDistance(1))  # Output: [5, 20]

# Compare two trees for equality
tree2 = BinarySearchTree()
tree2.insert(10)
tree2.insert(5)
tree2.insert(20)
print(tree.equals(tree2))  # Output: True

# Count the number of edges in the tree
print(tree.numEdges())  # Output: 4
```
## Unit Tests 
```bash
import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        """Set up a tree for testing before each test case"""
        self.tree = BinarySearchTree()
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(20)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(15)
        self.tree.insert(30)

    def test_insert_and_find(self):
        """Test inserting values and finding them in the tree"""
        self.assertTrue(self.tree.find(10))
        self.assertTrue(self.tree.find(3))
        self.assertTrue(self.tree.find(30))
        self.assertFalse(self.tree.find(100))  # Value not in the tree

    def test_height(self):
        """Test the height of the tree"""
        # The expected height should be 2 (longest path: 10 -> 20 -> 30)
        self.assertEqual(self.tree.height(), 2)

    def test_min(self):
        """Test finding the minimum value in the tree"""
        self.assertEqual(self.tree.min(), 3)  # Smallest value is 3

    def test_max(self):
        """Test finding the maximum value in the tree"""
        self.assertEqual(self.tree.max(), 30)  # Largest value is 30

    def test_get_nodes_at_distance(self):
        """Test getting nodes at a specific distance from the root"""
        # Distance 0 -> [10]
        self.assertEqual(self.tree.getNodesAtDistance(0), [10])
        # Distance 1 -> [5, 20]
        self.assertEqual(self.tree.getNodesAtDistance(1), [5, 20])
        # Distance 2 -> [3, 7, 15, 30]
        self.assertEqual(self.tree.getNodesAtDistance(2), [3, 7, 15, 30])

    def test_equals(self):
        """Test if two trees are equal"""
        tree2 = BinarySearchTree()
        tree2.insert(10)
        tree2.insert(5)
        tree2.insert(20)
        tree2.insert(3)
        tree2.insert(7)
        tree2.insert(15)
        tree2.insert(30)
        self.assertTrue(self.tree.equals(tree2))

        # Now modify tree2 and it should no longer be equal
        tree2.insert(25)
        self.assertFalse(self.tree.equals(tree2))

    def test_num_edges(self):
        """Test counting the number of edges in the tree"""
        self.assertEqual(self.tree.numEdges(), 6)  # Total 6 edges: 6 connections between nodes

if __name__ == '__main__':
    unittest.main()
```
