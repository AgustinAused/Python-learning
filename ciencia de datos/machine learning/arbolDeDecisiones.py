import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

table = pandas.read_csv("ciencia de datos\machine learning\cars2.csv")

print(table)