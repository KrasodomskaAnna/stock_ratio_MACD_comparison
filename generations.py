import itertools
import random
import pandas as pd

from code_1 import liczMACD_SIGNAL, autoAkcjonariusz


def initial_population(population_size):
    items = []
    for _ in range(population_size):
        individual = [0] * 3
        individual[0] = random.randint(1, 15)
        individual[1] = random.randint(15, 50)
        individual[2] = random.randint(5, 15)
        items.append(individual)
    return items


def fitness(individual, dane, max_x_length):
    toople = liczMACD_SIGNAL(dane, max_x_length, individual[0], individual[1], individual[2])
    return autoAkcjonariusz(dane, toople[0], toople[1])


def population_best(population, dane, max_x_length):
    best_individual = None
    best_individual_fitness = -1
    for individual in population:
        individual_fitness = fitness(individual, dane, max_x_length)
        if individual_fitness > best_individual_fitness:
            best_individual = individual
            best_individual_fitness = individual_fitness
    return best_individual, best_individual_fitness


items = pd.read_csv('data.csv')
dane_calosciowe = pd.read_csv('snx_d.csv')
dane = dane_calosciowe["Zamkniecie"]
max_x_length = 1000
data_length = len(dane) - max_x_length

population_size = 20
generations = 40
n_selection = 10  # ilość rodziców do wybrania
n_elite = 1  # ile wziąść maxymalnych elem.

best_solution = None
best_fitness = 0
population_history = []
best_history = []
population = initial_population(population_size)
for _ in range(generations):
    population_history.append(population)
    print(population)

    # 2. Wybór rodziców (selekcja ruletkowa)
    sum_f = sum([fitness(individual, dane, max_x_length) for individual in population])
    p = [(fitness(individual, dane, max_x_length) / sum_f) for individual in population]
    parents = random.choices(population, p, k=n_selection)

    # 3. Tworzenie kolejnego pokolenia
    elite = population_best(population, dane, max_x_length)[0]
    tuples = itertools.combinations(parents, 2)
    parents_tuples = random.sample([*tuples], population_size - n_elite)
    children = [[random.choice(p) for p in zip(p1, p2)] for p1, p2 in parents_tuples]

    # 4. Mutacja
    # wybór dzieci, które będziemy mutować
    rnd_mutations = random.choices(children, k=random.randint(0, n_selection))
    for child in rnd_mutations:
        # wybór ilości cech mutowanych - max to 2 cechy
        rnd_nmb = random.randint(0, 2)
        for i in range(rnd_nmb):
            wartosci_poprawne = False
            while not wartosci_poprawne:
                idx = random.randint(1, child.__len__() - 1)
                val = random.randint(1, 5)
                dir = random.randint(1, 1)
                child[idx] = child[idx] + val if dir else child[idx] - val
                if 0 < child[idx] < 50:
                    if child[0] < child[1]:
                        wartosci_poprawne = True

    # 5. Aktualizacja populacji rozwiązań
    population = children + [elite]

    best_individual, best_individual_fitness = population_best(population, dane, max_x_length)
    if best_individual_fitness > best_fitness:
        best_solution = best_individual
        best_fitness = best_individual_fitness
    best_history.append(best_fitness)

print('Best individual:', best_individual)
print('Best solution value:', best_fitness)
