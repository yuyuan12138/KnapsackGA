# Knapsack Genetic Algorithm

This project implements a genetic algorithm (GA) to solve the Knapsack Problem, a popular combinatorial optimization problem. The goal is to maximize the total value of items placed in a knapsack without exceeding its weight capacity.

## Description

The Knapsack Problem involves a set of items, each with a designated weight and value. The challenge is to determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. This implementation uses a genetic algorithm with customizable parameters such as population size, number of generations, crossover rate, and mutation rate.

## Features

- **Customizable Genetic Algorithm Parameters**: Adjust the population size, generations, crossover rate, and mutation rate to explore different genetic dynamics.
- **Roulette Wheel Selection**: Enhances diversity in genetic selection by using fitness proportionate selection.
- **Single-Point Crossover**: Maintains genetic diversity across generations.
- **Bit Flip Mutation**: Introduces variability into the offspring, helping to avoid local minima.

## Installation

No external libraries are required for the basic functionality of this genetic algorithm as it uses numpy. Ensure you have Python and numpy installed.

```bash
pip install numpy
```

## Usage

To run the genetic algorithm with default settings, use the following code snippet in your Python environment:

```python
from knapsack_ga import KnapsackGA

# Example parameters
values = [10, 40, 30, 50]
weights = [5, 10, 20, 30]
max_weight = 50

# Create and run the GA instance
ga = KnapsackGA(values, weights, max_weight, population_size=100, generations=50)
ga.run()
```

This will output the best value found in each generation to the console.

## Configuration

The parameters for the genetic algorithm can be configured at instantiation:

- **values**: List of item values.
- **weights**: List of item weights.
- **max_weight**: Maximum allowable weight for the knapsack.
- **population_size**: Number of individuals in the population.
- **generations**: Number of generations to simulate.
- **crossover_rate**: Probability of crossover between pairs of individuals.
- **mutation_rate**: Probability of mutating a given gene.

## Contributing

Contributions are welcome! If you have suggestions for improving the algorithm or extending the project, feel free to make a pull request or open an issue.
