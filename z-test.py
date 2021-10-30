import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

#reading school data
df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()

#Getting random set of means
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []

for i in range(0, 1000):
	set_of_mean = random_set_of_mean(100)
	mean_list.append(set_of_mean)

#finding out the smaple mean and sample deviation
sample_mean = statistics.mean(mean_list)
sample_stdev = statistics.stdev(mean_list)

#finding the standard deviation 1, 2, 3
sample_stdev1start, sample_stdev1end = sample_mean - sample_stdev, sample_mean + sample_stdev;
sample_stdev2start, sample_stdev2end = sample_mean - (sample_stdev * 2), sample_mean + (sample_stdev * 2)
sample_stdev3start, sample_stdev3end = sample_mean - (sample_stdev * 3), sample_mean + (sample_stdev * 3)


df_1 = pd.read_csv("medium_data.csv")
data_list1 = df_1['claps'].tolist()

mean_1 = statistics.mean(data_list1)

fig = ff.create_distplot([mean_list], ["Mean"], show_hist = False)
fig.add_trace(go.Scatter(x = [sample_mean, sample_mean], y = [0, 0.008], mode = 'lines', name = 'mean'))
fig.add_trace(go.Scatter(x = [mean_1, mean_1], y = [0, 0.008], mode = 'lines', name = 'mean_1'))
fig.add_trace(go.Scatter(x = [sample_stdev1end, sample_stdev1end], y = [0, 0.008], mode = 'lines', name = 'stdev1end'))
fig.add_trace(go.Scatter(x = [sample_stdev2end, sample_stdev2end], y = [0, 0.008], mode = 'lines', name = 'stdev2end'))
fig.add_trace(go.Scatter(x = [sample_stdev3end, sample_stdev3end], y = [0, 0.008], mode = 'lines', name = 'stdev3end'))
fig.show()


#finding the zscore using the formula
z_score = (mean_1 - sample_mean) / sample_stdev
print(f'The sample mean is - {sample_mean}')
print(f'The standard deviation is - {sample_stdev}')
print(f'Mean of sample one is - {mean_1}')
print(f'The z-score is - {z_score}')
