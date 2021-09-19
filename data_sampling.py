import statistics
import csv
import plotly.figure_factory as ff 
import pandas as pd 

data = pd.read_csv('data.csv')
population_mean = statistics.mean(data["reading_time"])

def random_set_of_means(30):
    dataset = []
    for i in range(0,30):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_means(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

def show_fig(mean_list):
    df  = mean_list
    fig = ff.create_distplot([df],["reading time"],show_hist = False)
    fig.show()
