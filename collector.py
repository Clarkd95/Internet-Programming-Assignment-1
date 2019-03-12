import math

#Clark Wilson
#CS4720/03
#Ben Setzer
#1/21/2019
class Collector:



    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def count(self):
        return len(self.data)
    def sum(self):
        sum = 0
        for x in self.data:
            sum += x
        return sum
    def sum_squares(self):
        sum_squares = 0
        for x in self.data:
            sum_squares += x*x
        return sum_squares
    def average(self):
        average = self.sum()/len(self.data)
        return average
    def variance(self):
        variance = self.sum_squares() / self.count() - self.average() * self.average()
        return variance
    def standard_deviation(self):
        return math.sqrt(self.variance())