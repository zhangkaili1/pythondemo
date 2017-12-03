import csv
path=r"D:\pythondemo\data\member_info.csv"
filter = open(path,"r")
data_table=csv.reader(filter)
for i in data_table:
    print(i)