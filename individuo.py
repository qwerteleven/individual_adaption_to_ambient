import numpy as np


class Individuo:


    def __init__(self, id, amb):
        self.id = id
        self.amb = amb
        self.accuracy_regeneration_ = np.random.rand(1)
        self.regeneration_ = np.random.rand(1)
        self.information = np.random.rand(150, 150)


    def regeneration(self, cap):
        self.amb.solution = (cap + self.information) % 255 
        self.information = self.amb.solution

    def fit(self, cap):
        self.regeneration(cap)

    def accuracy_regeneration(self):
        self.accuracy_regeneration_ = np.abs(self.old_information - self.information).mean()


    def get_information(self):
        return self.information

