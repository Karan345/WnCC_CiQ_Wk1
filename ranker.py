import pandas as pd
import numpy as np
import sys

data = pd.read_csv('marksheet.csv')
print(data)
k = data.sort_values(by=['Marks'],ascending=False)
print(k)
marks_series = k["Marks"]
marks_list = marks_series.values.tolist()
kk = 1
rank_list = []
tied_list = []
tied_list1 = []
for i in range(len(marks_list)):
  if i!=0 :   
      m = marks_list[i]         
      n = marks_list[(i-1)]     
  if i == 0 :
      rank_list.append(i+1)
      tied_list.append(0)
  elif m==n :   
      rank_list.append(rank_list[i-1]) 
      kk += 1
      tied_list.append(0)
  else :     
      rank_list.append(i+1)
      for i in range(len(tied_list)) :
       tied_list1.append(kk)
       print(tied_list1)
       print(len(tied_list1))
      tied_list = []
      kk=1     

k.insert(2,"Rank",rank_list,True)
#print("Length of tied")
#print(len(tied_list))
#print(tied_list)
k.insert(3,"Tied Between",tied_list,True)
k.to_csv('sorted_ranked.csv', index= False)



#def marks_fetcher(roll_no) :
#   print(data.loc[data['Roll Number']==roll_no])
def rank_fetcher(roll_no):
   print(k.loc[k['Roll Number']==roll_no])  


while True:
   
     print("Enter Roll No. :")
     roll1 = input()
     if roll1 == 'stop' :
         sys.exit("USer ended.")

     roll = int(roll1)
    # marks_fetcher(roll)
     rank_fetcher(roll)
 
    
