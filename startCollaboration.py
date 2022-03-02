from weakref import ref
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("math-score.csv")

data = df["Math_score"].tolist()

mean = statistics.mean(data)
print("Mean is :",mean)

std_deviation = statistics.stdev(data)
print("Standard Deviation is :",std_deviation)

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

meanList = []
for i in range (0,1000):
    setOfMean = randomSetOfMean(100)

    meanList.append(setOfMean)

mean = statistics.mean(meanList)
print("Mean is : ",mean)

StdDev = statistics.stdev(meanList)
print("Standard deviation is :",StdDev)

first_std_start,first_std_end = mean-std_deviation,mean+std_deviation
sec_std_start,sec_std_end = mean-(2*std_deviation),mean+(2*std_deviation)
third_std_start,third_std_end = mean-(3*std_deviation),mean+(3*std_deviation)

print("Standard Deviation 1 is :",first_std_start,first_std_end)
print("Standard Deviation 2 is :",sec_std_start,sec_std_end)
print("Standard Deviation 3 is :",third_std_start,third_std_end)



df = pd.read_csv("marks-1.csv")
data = df["Math_score"].tolist()
meanOfSample1 = statistics.mean(data)
print("Mean of sample 1 is: ",meanOfSample1)


df = pd.read_csv("marks-2.csv")
data = df["Math_score"].tolist()
meanOfSample2 = statistics.mean(data)
print("Mean of sample 2 is: ",meanOfSample2)


df = pd.read_csv("marks-3.csv")
data = df["Math_score"].tolist()
meanOfSample3 = statistics.mean(data)
print("Mean of sample 3 is: ",meanOfSample3)

fig = ff.create_distplot([meanList],["student_marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_start,first_std_start],y=[0,0.17],mode="lines",name="FIRST_STD"))
fig.add_trace(go.Scatter(x=[sec_std_start,sec_std_start],y=[0,0.17],mode="lines",name="SEC_STD"))
fig.add_trace(go.Scatter(x=[third_std_start,third_std_start],y=[0,0.17],mode="lines",name="THIRD_STD"))

fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="FIRST_STD_END"))
fig.add_trace(go.Scatter(x=[sec_std_end,sec_std_end],y=[0,0.17],mode="lines",name="SEC_STD_END"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines",name="THIRD_STD_END"))

fig.add_trace(go.Scatter(x=[meanOfSample1,meanOfSample1],y=[0,0.17],mode="lines",name="MEAN_OF_SAMPLE_1"))
fig.add_trace(go.Scatter(x=[meanOfSample2,meanOfSample2],y=[0,0.17],mode="lines",name="MEAN_OF_SAMPLE_2"))
fig.add_trace(go.Scatter(x=[meanOfSample3,meanOfSample3],y=[0,0.17],mode="lines",name="MEAN_OF_SAMPLE_3"))
fig.show()

Z_Score = (meanOfSample1-mean)/std_deviation
print("Z score for the first sample is :",Z_Score)

Z_Score2 = (meanOfSample2-mean)/std_deviation
print("Z score for the second sample is :",Z_Score2)

Z_Score3 = (meanOfSample3-mean)/std_deviation
print("Z score for the third sample is :",Z_Score3)