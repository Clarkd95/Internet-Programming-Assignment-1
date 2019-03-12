from collector import Collector

coll = Collector()
data = [5, 7, 13, 24, 37, 56, 1001, 251, 300, 55, 4, 8, 14, 76, 15, 1051, 751,]
for x in range(len(data)):
    coll.add(data[x])
print(f"The list contains {coll.count()} numbers")
print(f"Sum                = {coll.sum():15}")
print(f"Sum of Squares     = {coll.sum_squares():15}")
print(f"Average            = {coll.average():15f}")
print(f"Variance           = {coll.variance():15f}")
print(f"Standard Deviation = {coll.standard_deviation():15f}")
