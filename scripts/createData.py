import pandas as pd

data = pd.read_csv("manga.csv")

data2 = data[["title", "type","status" , "genres", "themes",
              "score", "scored_by", "volumes", "chapters",
              "start_date", "end_date"]]
data3 = data2.dropna()
print(data3.count())

out = data3#.sample(10000)
out.to_csv("../data/final.csv")


