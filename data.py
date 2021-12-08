import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

mean = sum(dice_result)/len(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
std_deviation=statistics.stdev(dice_result)

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_deviation))

fig= ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.show()