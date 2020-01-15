#!/usr/bin/python
import csv

fp = open('data.txt', "r")
lines = fp.readlines()
fp.close()
 
new_dict = []

print(len(lines))

for i in range(len(lines)):
    tmp = lines[i].split( )
    tmp1 = tmp[3].split("=")

    if eval(tmp1[1]) == "e1det_gneE128_0":
        # print("yes")
        tmp2 = tmp[5].split("=")
        new_dict.append(float(eval(tmp2[1])))

# print(len(new_dict))
# with open('train.csv', 'w', newline='') as csvfile:
#     writer  = csv.writer(csvfile)
#     for i in range(0,1160):
#         writer.writerow([new_dict[i]])
  
# with open('test.csv', 'w', newline='') as csvfile:
#     writer  = csv.writer(csvfile)
#     for i in range(1161,1450):
#         writer.writerow([new_dict[i]])
   

with open('toal_data.csv', 'wb') as csvfile:
    writer  = csv.writer(csvfile)
    for i in range(1460):
        writer.writerow([new_dict[i]])

print(new_dict)