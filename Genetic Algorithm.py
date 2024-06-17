import numpy as np

class KnapsackGA:
    def __init__(self, values, weights, max_weight, population_size, generations, crossover_rate=0.7, mutation_rate=0.01):
        """
        Initialize the genetic algorithm class.

        Parameters:
        values (list): List of item values.
        weights (list): List of item weights.
        max_weight (int): Maximum weight the knapsack can carry.
        population_size (int): Size of the population.
        generations (int): Number of generations.
        crossover_rate (float): Crossover rate.
        mutation_rate (float): Mutation rate.
        """
        self.values = np.array(values)
        self.weights = np.array(weights)
        self.max_weight = max_weight
        self.population_size = population_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.chromosome_length = len(values)
        self.population = self.initialize_population()

    def initialize_population(self):
        """Generate the initial population, randomly selecting items."""
        return np.random.randint(2, size=(self.population_size, self.chromosome_length))

    def fitness(self, individual):
        """Calculate the fitness of an individual, considering the weight constraint."""
        value = np.sum(individual * self.values)
        weight = np.sum(individual * self.weights)
        if weight <= self.max_weight:
            return value
        else:
            return 0

    def select_population(self):
        """Selection operation using the roulette wheel method to select the new population."""
        fitness_scores = np.array([self.fitness(ind) for ind in self.population])
        probabilities = fitness_scores / np.sum(fitness_scores)
        indices = np.random.choice(self.population_size, size=self.population_size, replace=True, p=probabilities)
        return self.population[indices]

    def crossover(self):
        """Single point crossover operation."""
        new_population = []
        for _ in range(self.population_size // 2):
            if np.random.rand() < self.crossover_rate:
                parent1, parent2 = np.random.choice(self.population_size, 2, replace=False)
                point = np.random.randint(1, self.chromosome_length)
                offspring1 = np.concatenate([self.population[parent1, :point], self.population[parent2, point:]])
                offspring2 = np.concatenate([self.population[parent2, :point], self.population[parent1, point:]])
                new_population.extend([offspring1, offspring2])
            else:
                new_population.extend(self.population[np.random.choice(self.population_size, 2, replace=False)])
        self.population = np.array(new_population)

    def mutate(self):
        """Mutation operation, randomly flipping a bit."""
        for i in range(self.population_size):
            for j in range(self.chromosome_length):
                if np.random.rand() < self.mutation_rate:
                    self.population[i, j] = 1 - self.population[i, j]

    def run(self):
        """Run the genetic algorithm."""
        for generation in range(self.generations):
            self.population = self.select_population()
            self.crossover()
            self.mutate()
            best_value = max([self.fitness(ind) for ind in self.population])
            print(f"Generation {generation}: Best Value = {best_value}")

if __name__ == "__main__":
    # Example parameters
    values = [10, 40, 30, 50]
    weights = [5, 10, 20, 30]
    max_weight = 50

    # Create and run the GA instance
    ga = KnapsackGA(values, weights, max_weight, population_size=100, generations=50)
    ga.run()
