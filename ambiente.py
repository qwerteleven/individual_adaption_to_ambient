import numpy as np

import individuo as uo

class ambient:

    def __init__(self):
        self.dificulty = np.random.rand(1)
        self.problem = np.random.rand(150, 150)
        self.solution = np.zeros((150, 150))
        self.create_world()

    def create_world(self):
        self.poblation = [uo.Individuo(i, self) for i in range(100)]

    def get_world(self):
        return self.solution

    def display(self):
        return self.solution


    def try_resol(self):
        self.capacity = np.random.rand(150, 150)

        for indivi in self.poblation:
            indivi.fit(self.capacity)

