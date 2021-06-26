import numpy as np

import individuo as uo

class ambient:

    def __init__(self):
        self.dificulty = np.random.rand(1)
        self.problem = np.random.rand(150, 150)
        self.solution = np.zeros((150, 150))
        self.create_world()


    def create_world(self):
        self.poblation = [uo.Individuo(i) for i in range(100)]

    def display(self):
        self.solution = np.zeros((150, 150))
        for indivi in self.poblation:
            self.solution = (self.solution + indivi.information) % 255

        return self.solution


    def try_resol(self):
        self.capacity = [np.where((self.problem - individ.get_information() > self.dificulty), 1, 0)
                         for individ in self.poblation]

        self.capacity_evaluation = [capacity_.mean() for capacity_ in self.capacity]

        for cap, indivi in zip(self.capacity, self.poblation):
            indivi.fit(cap)

