import statistics
import pandas as pd
import plotly.express as px
import math
import random
import plotly.figure_factory as ff

df = pd.read_csv("P110data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist = False)

population_mean = statistics.mean(data)
print("Mean: ", population_mean)
population_stdev = statistics.stdev(data)
print("Standard Deviation: ", population_stdev)

dataset = []
for i in range(0, 1000):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
stdev = statistics.stdev(data)
print("Mean of 1000 vaules: ", mean)
print("Standard deviation of 1000 vaules: ", stdev)