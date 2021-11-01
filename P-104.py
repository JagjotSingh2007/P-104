import pandas as pd 
import statistics
import csv 


df  = pd.read_csv("SOCR-HeightWeight.csv")
weight = df["Weight"].tolist()


mean_of_weight = statistics.mean(weight)
mode_of_weight = statistics.mode(weight)
median_of_weight = statistics.median(weight)

print(f"THE MEAN OF THE GIVEN WEIGHT : {mean_of_weight}")
print(f"THE MODE OF THE GIVEN WEIGHT : {mode_of_weight}")
print(f"THE MEADIAN OF THE GIVEN WEIGHT : {median_of_weight}")