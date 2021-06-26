import numpy as np


class Individuo:


    def __init__(self, id):
        self.id = id
        self.accuracy_regeneration_ = np.random.rand(1)
        self.regeneration_ = np.random.rand(1)
        self.information = np.random.rand(150, 150)
        self.old_information = self.information.copy()


    def regeneration(self, cap):
        self.information = np.where(self.regeneration_ > cap, self.old_information, self.information)

    def fit(self, cap):
        self.regeneration(cap)

    def accuracy_regeneration(self):
        self.accuracy_regeneration_ = np.abs(self.old_information - self.information).mean()


    def get_information(self):
        return self.information

