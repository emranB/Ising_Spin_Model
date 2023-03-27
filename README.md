1. Setup config file
    - Config file must a json file of the following format:
        {
            "input-file-path": "./data/input.txt",
            "debug": false,
            "run-standalone-model": true,
            "run-scipy-model": true
        }
    - This will install all requried dependencies
    - Config flags:
        - "input-file-path" -> path to input file relative to root of this project
        - "debug" -> enable/disable logging information
        - "run-standalone-model" -> enable/disable running standalone model
        - "run-scipy-model" -> enable/disable running scipy model

2. Run application by navigating to the root of this project (where run.sh is located) and use:
    - sh run.sh

3. Algorithm description:
1 Introduction
An Ising spin model can be considered a graph with nodes and edges, in which
each node has a spin which can be positive (+1) or negative (-1). The spin
of node v is denoted sv. The nodes have weights given by a vector h, and
the edges have weights given by an upper triangular matrix J; weights can be
positive, negative, or zero. The spin configuration, i.e., whether each node’s
spin is positive or negative, is known as the state. The energy of the system
depends on the state and the weights given by h and J. 

The equation for the system energy given by state S = (s1, ..., sn) is:

        E(S) = (1 <= i <= n) SUM(H_i * S_i) + (1 <= i < j <= n) SUM(J_ij * S_i * J_i)

We are generally interested in finding a ground state, i.e., a state that minimizes
the energy of the system. Put another way, a state Sg is a ground state if and
only if Sg = argminS E(S). The energy of a ground state is known as the ground
state energy and is equal to minS E(S). Thus the problem of finding a ground
state is a minimization problem

2 The algorithm
This problem on general graphs is NP-complete, but on trees, it is solvable in
polynomial time.
Write a program that computes a ground state (as a vector of spins)
and the ground state energy for an Ising spin model on a tree.
The program can be written in any language, but it must be able to be run
on GNU/Linux. The algorithm should require no more than O(n log n) time
and space. In particular, since J is an extremely sparse matrix, it should not be
stored as a full matrix. 

3 Input format
Each input will be contained in a separate file containing text lines defined as
follows. There are three fields: u, v, and weight. If u ̸= v the (J) weight is
assigned to the edge between nodes u and v. If u = v, the (h) weight is assigned
to that node. You may assume the weights are integers. Here is an example file:

        0 1 1
        1 2 1
        1 3 1
        0 0 -1
        1 1 -1
        2 2 -1

4 Output format
The output should consist of two lines. The first should contain the ground
state energy. The second should contain a ground state as a series of + and -.
Output for the above problem could be:

        -4
        +-++