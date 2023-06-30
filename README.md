# Particle Swarm Optimization (PSO)
  **Author: Gustavo Mazzure**

  PSO is a metaheuristic in which uses the power of particle swarm to find optimizations on the search scope.

  In this implemetation, are given functions to generate 3d meshes, the objective is to optimize the value of Z, when
  x and y are given as variables, the optimization may be Maximization or Minimization
  
## Arguments:
| Argument    | Name  | Description |
| ----------- | -------------------- | ----------- |
|-h           | Help                 | Show this help message and exit |
|-f           | Function {1,2,3}     | 1: Schwefel; 2: Rastrigin; 3: custom function |
|-t           | type of optimization | 1: Maximization; 2: Minimization |
|-i           | scavangers count     | Number of scavangers |
|-m           | Max iterations without optimization     | Stop criterium |

## Requirements
  - Python 3.6+
  - numpy
  - pylab

## Usage

  ```
    python3 main.py
  ```