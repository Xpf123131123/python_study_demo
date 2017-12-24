import math
import random
from time import sleep

network = [4, [16], 1]

population = 50
elitism = 0.2
random_behaviour = 0.1
mutation_rate = 0.5
mutation_range = 2
historic = 0
low_historic = False
score_sort = -1
n_child = 1

def sigmoid(z):
    return 1.0/(1.0 + math.exp(-z))

# (-1 ~ 1)
def random_clamped():
    return random.random()*2 - 1

class Neuron():
    def __init__(self):
        self.biase = 0
        self.weights = []


    def init_weights(self, n):
        self.weights = []
        for i in range(n):
            self.weights.append(random_clamped())

    def __repr__(self):
        return 'Neuron weight size:{}  biase value:{}'.format(len(self.weights), self.biase)


class Layer():
    def __init__(self, index):
        self.index = index
        self.neurons = []

    def init_neurons(self, n_neuron, n_input):
        self.neurons = []
        for i in range(n_neuron):
            neuron = Neuron()
            neuron.init_weights(n_input)
            self.neurons.append(neuron)

    def __repr__(self):
        return 'Layer ID:{}  Layer neuron size:{}'.format(self.index, len(self.neurons))


# class 