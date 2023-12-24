# Trees
1. General Idea about Trees 

    - Different Nodes - child and parent
    - Child nodes inherited from Parent node
    - one parent and 2 child
    - Levels of tree - from top to bottom  (starts at 1)
    - Height of tree - from bottom to top (starts at 0)
    - Depth of tree- from top to bottom (starts at 0)

2. Traversals

    - BFS (Breath First Search) 
        Searches by level
    - DFS (Depth First Search)
        3 Ways
        - PreOrder RoLR (Root-Left-Right)
        - InOrder LRoR (Left-Root-Right)
        - PostOrder LRRo (Left-Right-Root)

3. Different Trees:

    - Binary Tree
        - Duplicated Value allowed.
        - there is no ordering in terms of how the nodes are arranged.
        - Faster in accessing data.
        - sub types:
            - Full/proper/strict binary tree. 
                - Each node has 0 or 2 child.
                - no of leaf nodes= no of internal nodes + 1.
                
            - Complete binary tree.
            - prefect binary tree.
            - degenerate binary tree.
    - Binary Search Tree:
        - No duplicate value.
        - The elements on left side must have value less than root and element on right side must have value greater than root.
        - Faster in operations.
        - sub types:
            - AVL tree.
            - Red Black Trees.
            - T-trees.