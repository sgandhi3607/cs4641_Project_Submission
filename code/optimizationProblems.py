import mlrose
import numpy as np
from time import time
import writeToExcel


def maxKColor(edges, nodes, colors):
    fitness = mlrose.MaxKColor(edges)

    problem = mlrose.DiscreteOpt(length = nodes, fitness_fn = fitness, maximize = False, max_val = colors)
    t0 = time()
    best_state, best_fitness = mlrose.random_hill_climb(problem, max_attempts=100, max_iters=np.inf,
                          init_state=None)
    finish = time() - t0

    print(best_state)
    print(best_fitness)
    print(finish)

def KQueens(numQueens, sizeOrIterations):
    fitness = mlrose.Queens()
    problem = mlrose.DiscreteOpt(length = numQueens, fitness_fn = fitness, maximize = False, max_val = numQueens)
    rhcfitnessMatrix = []
    safitnessMatrix = []
    genalgfitnessMatrix = []
    mimicfitnessMatrix = []
    numIterations = 10000
    dataPoints = 100
    #rhc
    print("Begin RHC")
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("RHC I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.random_hill_climb(problem, max_attempts=100, max_iters=i,
                              init_state=None)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            rhcfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))


    #simulated annealing
    schedule = mlrose.ExpDecay()
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("SA I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.simulated_annealing(problem, schedule = schedule,
                                                      max_attempts = 100, max_iters = i,
                                                      init_state = None)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            safitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))


    #genetic alg
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("GA I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.genetic_alg(problem, pop_size=200, mutation_prob=0.1, max_attempts=100,
                max_iters=i)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            genalgfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))

    #mimic
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("Mimic I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.mimic(problem, pop_size=200, keep_pct=0.2, max_attempts=100, max_iters=i)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            mimicfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))
    if not sizeOrIterations:
        writeToExcel.writeOptimzationProblem(rhcfitnessMatrix, safitnessMatrix, genalgfitnessMatrix, mimicfitnessMatrix, "QueensIterations.xlsx")
        return None
    else:
        return rhcfitnessMatrix, safitnessMatrix, genalgfitnessMatrix, mimicfitnessMatrix

def FourPeaks(arrayLen, sizeOrIterations):
    fitness = mlrose.FourPeaks(t_pct=0.15)
    problem = mlrose.DiscreteOpt(length = arrayLen, fitness_fn = fitness, maximize = True, max_val = 2)
    rhcfitnessMatrix = []
    safitnessMatrix = []
    genalgfitnessMatrix = []
    mimicfitnessMatrix = []
    numIterations = 10000
    dataPoints = 100
    #rhc
    print("Begin RHC")
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("RHC I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.random_hill_climb(problem, max_attempts=100, max_iters=i,
                              init_state=None)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            rhcfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))


    #simulated annealing
    schedule = mlrose.ExpDecay()
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("SA I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.simulated_annealing(problem, schedule = schedule,
                                                      max_attempts = 100, max_iters = i,
                                                      init_state = None)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            safitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))


    #genetic alg
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("GA I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.genetic_alg(problem, pop_size=200, mutation_prob=0.1, max_attempts=100,
                max_iters=i)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            genalgfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))

    #mimic
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("Mimic I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.mimic(problem, pop_size=200, keep_pct=0.2, max_attempts=100, max_iters=i)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            mimicfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))
    if not sizeOrIterations:
        writeToExcel.writeOptimzationProblem(rhcfitnessMatrix, safitnessMatrix, genalgfitnessMatrix, mimicfitnessMatrix, "4PeaksIterations.xlsx")
        return None
    else:
        return rhcfitnessMatrix, safitnessMatrix, genalgfitnessMatrix, mimicfitnessMatrix


def TravellingSalesman(coords, sizeOrIterations):
    fitness_coords = mlrose.TravellingSales(coords = coords)
    problem = mlrose.TSPOpt(length = len(coords), fitness_fn = fitness_coords, maximize=False)

    rhcfitnessMatrix = []
    safitnessMatrix = []
    genalgfitnessMatrix = []
    mimicfitnessMatrix = []
    numIterations = 10000
    dataPoints = 100
    #rhc
    print("Begin RHC")
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("RHC I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.random_hill_climb(problem, max_attempts=100, max_iters=i,
                              init_state=None)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            rhcfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))


    #simulated annealing
    schedule = mlrose.ExpDecay()
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("SA I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.simulated_annealing(problem, schedule = schedule,
                                                      max_attempts = 100, max_iters = i,
                                                      init_state = None)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            safitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))


    #genetic alg
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("GA I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.genetic_alg(problem, pop_size=200, mutation_prob=0.1, max_attempts=100,
                max_iters=i)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            genalgfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))

    #mimic
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("Mimic I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.mimic(problem, pop_size=200, keep_pct=0.3, max_attempts=100, max_iters=i)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            mimicfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))
    if not sizeOrIterations:
        writeToExcel.writeOptimzationProblem(rhcfitnessMatrix, safitnessMatrix, genalgfitnessMatrix, mimicfitnessMatrix, "TSIterations.xlsx")
        return None
    else:
        return rhcfitnessMatrix, safitnessMatrix, genalgfitnessMatrix, mimicfitnessMatrix

def KnapSack(weights, values, sizeOrIterations):
    max_pct = .6
    fitness = mlrose.Knapsack(weights, values, max_pct)
    total = 0
    for item in weights:
        total = total + item
    print (total)
    problem = mlrose.DiscreteOpt(length = len(weights), fitness_fn = fitness, maximize = True, max_val = 3)

    rhcfitnessMatrix = []
    safitnessMatrix = []
    genalgfitnessMatrix = []
    mimicfitnessMatrix = []
    numIterations = 10000
    dataPoints = 100
    #rhc
    print("Begin RHC")
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("RHC I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.random_hill_climb(problem, max_attempts=100, max_iters=i,
                              init_state=None)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            rhcfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))


    #simulated annealing
    schedule = mlrose.ExpDecay()
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("SA I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.simulated_annealing(problem, schedule = schedule,
                                                      max_attempts = 100, max_iters = i,
                                                      init_state = None)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            safitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))


    #genetic alg
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("GA I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.genetic_alg(problem, pop_size=200, mutation_prob=0.1, max_attempts=100,
                max_iters=i)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            genalgfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))

    #mimic
    startingTime = time()
    for i in range(numIterations):
        if i % dataPoints == 0 and not sizeOrIterations or i == 1000 and sizeOrIterations:
            print("Mimic I: " + str(i))
            t0 = time()
            best_state, best_fitness = mlrose.mimic(problem, pop_size=200, keep_pct=0.3, max_attempts=100, max_iters=i)
            finish = time() - t0
            currentTime = time() - startingTime
            print("CurrentTime: " + str(currentTime))
            mimicfitnessMatrix.append((i, best_fitness, finish))
    finishtime = time() - startingTime
    print("Finish Time: " + str(finishtime))
    if not sizeOrIterations:
        writeToExcel.writeOptimzationProblem(rhcfitnessMatrix, safitnessMatrix, genalgfitnessMatrix, mimicfitnessMatrix, "KSIterations.xlsx")
        return None
    else:
        return rhcfitnessMatrix, safitnessMatrix, genalgfitnessMatrix, mimicfitnessMatrix
#queens iteration testing
#KQueens(8, False)

#num queens testiing at 1000 iterations
# rhcFit = []
# saFit = []
# genFit = []
# mimicFit = []
# for i in range(4, 20):
#     print("Queens: " + str(i))
#     rhc, sa, gen, mimic = KQueens(i, True)
#     add = (i, rhc[0][1], rhc[0][2])
#     rhcFit.append(add)
#     add = (i, sa[0][1], sa[0][2])
#     saFit.append(add)
#     add = (i, gen[0][1], gen[0][2])
#     genFit.append(add)
#     add = (i, mimic[0][1], mimic[0][2])
#     mimicFit.append(add)
# writeToExcel.writeOptimzationProblem(rhcFit, saFit, genFit, mimicFit, "KQueens.xlsx")

#4 peaks iteration testing
#FourPeaks(8, False)
#4 Peaks length of array testing
# rhcFit = []
# saFit = []
# genFit = []
# mimicFit = []
# for i in range(4, 30):
#     print("Array Len: " + str(i))
#     rhc, sa, gen, mimic = FourPeaks(i, True)
#     add = (i, rhc[0][1], rhc[0][2])
#     rhcFit.append(add)
#     add = (i, sa[0][1], sa[0][2])
#     saFit.append(add)
#     add = (i, gen[0][1], gen[0][2])
#     genFit.append(add)
#     add = (i, mimic[0][1], mimic[0][2])
#     mimicFit.append(add)
# writeToExcel.writeOptimzationProblem(rhcFit, saFit, genFit, mimicFit, "FourPeaksLength.xlsx")

#Travelling Salesman iteration testing
# np.random.seed(2)
# coordinates = []
# cities = 10
# for i in range(cities):
#     point1 = int(np.random.uniform(0, 50, None))
#     point2 = int(np.random.uniform(0, 50, None))
#     coord = (point1, point2)
#     coordinates.append(coord)
# print(coordinates)
# TravellingSalesman(coordinates, False)

#Travelling Salesman Num Cities increase
# rhcFit = []
# saFit = []
# genFit = []
# mimicFit = []
# np.random.seed(2)
# coordinates = []
# cities = 4
# for i in range(cities):
#         point1 = int(np.random.uniform(0, 50, None))
#         point2 = int(np.random.uniform(0, 50, None))
#         coord = (point1, point2)
#         coordinates.append(coord)
# for numCities in range(4, 40):
#     print("Num Cities: " + str(numCities))
#     print(len(coordinates))
#     print(coordinates)
#     point1 = int(np.random.uniform(0, 50, None))
#     point2 = int(np.random.uniform(0, 50, None))
#     coord = (point1, point2)
#     coordinates.append(coord)
#     rhc, sa, gen, mimic = TravellingSalesman(coordinates, True)
#     add = (i, rhc[0][1], rhc[0][2])
#     rhcFit.append(add)
#     add = (i, sa[0][1], sa[0][2])
#     saFit.append(add)
#     add = (i, gen[0][1], gen[0][2])
#     genFit.append(add)
#     add = (i, mimic[0][1], mimic[0][2])
#     mimicFit.append(add)

# writeToExcel.writeOptimzationProblem(rhcFit, saFit, genFit, mimicFit, "TSNumCitiesMax.xlsx")

#Knapsack fixed len
rhcFit = []
saFit = []
genFit = []
mimicFit = []
np.random.seed(2)
values = []
weights = []
for i in range(10):
    val = int(np.random.uniform(1, 10, None))
    weight = int(np.random.uniform(1, 10, None))
    values.append(val)
    weights.append(weight)
KnapSack(weights, values, False)

#knapsack increase len

# rhcFit = []
# saFit = []
# genFit = []
# mimicFit = []
# np.random.seed(2)
# values = []
# weights = []
# for i in range(4):
#     val = int(np.random.uniform(1, 10, None))
#     weight = int(np.random.uniform(1, 10, None))
#     values.append(val)
#     weights.append(weight)
# for items in range(4, 20):
#     print (items)
#     print (weights)
#     print (values)
#     val = int(np.random.uniform(1, 10, None))
#     weight = int(np.random.uniform(1, 10, None))
#     values.append(val)
#     weights.append(weight)
#     rhc, sa, gen, mimic = KnapSack(weights, values, True)
#     print (rhc)
#     print (sa)
#     print (gen)
#     print (mimic)
#     add = (items, rhc[0][1], rhc[0][2])
#     rhcFit.append(add)
#     add = (items, sa[0][1], sa[0][2])
#     saFit.append(add)
#     add = (items, gen[0][1], gen[0][2])
#     genFit.append(add)
#     add = (items, mimic[0][1], mimic[0][2])
#     mimicFit.append(add)

# writeToExcel.writeOptimzationProblem(rhcFit, saFit, genFit, mimicFit, "KnapSackMoreItems.xlsx")





