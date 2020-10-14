import pandas as pd
import time,datetime
tags = pd.read_csv('C:\\Users\\Peipengyu\\Desktop\\ml-25m\\tags.csv')
ratings = pd.read_csv('C:\\Users\\Peipengyu\\Desktop\\ml-25m\\ratings.csv')
movies = pd.read_csv('C:\\Users\\Peipengyu\\Desktop\\ml-25m\\movies.csv')
links = pd.read_csv('C:\\Users\\Peipengyu\\Desktop\\ml-25m\\links.csv')
data1 = tags.append(ratings)['userId']
print("共有%d个不同的用户"%len(data1.drop_duplicates()))
print("共有%d个不同的电影"%len(movies['movieId'].drop_duplicates()))
temp_list=movies["genres"].str.split("|").tolist()
print("共有%d不同的电影种类"%len(list(set([i for j in temp_list for i in j ]))))
print("共有%d部电影没有外部链接"%(len(movies['movieId'].drop_duplicates())
                        -len(links['movieId'].drop_duplicates())))
def tim(stamp):
    timeArray = time.localtime(stamp)
    otherStyleTime = time.strftime("%Y",timeArray)
    return otherStyleTime
ratings["timestamp"]=ratings["timestamp"].apply(tim)
print("2018年一共有%d人进行过电影评分"%(len(ratings[ratings.timestamp=='2018'].drop_duplicates(['userId']))))