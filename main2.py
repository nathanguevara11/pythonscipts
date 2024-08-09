import os
import csv
rowcount = 0 
can1 = 0
can2 = 0
can3 = 0
votepeople = []
diction = {}
ph2challenge = os.path.join('PythonHW1.csv')
with open (ph2challenge)as PH2:
    ph2data = csv.reader(PH2, delimiter = ",")
    ph2dataheader = next(ph2data)
    for row in ph2data:
          #print(row)
          rowcount = rowcount + 1
          if row[2] == "Raymon Anthony Doane":
               can1 = can1 + 1
          elif row[2] == "Diana DeGette":
                can2 = can2 + 1
          else:
                can3 = can3 + 1
#           if row[2] not in votepeople:
#                votepeople.append(row[2])
#     for items in ph2data:
         

# print(f"{percent}")
          
         
        

    



# print("votepeople", votepeople)

               
        #   if row[2] == "Raymon Anthony Doane":
        #        can1 = can1 + 1
        #   elif row[2] == "Diana DeGette":
        #         can2 = can2 + 1
        #   else:
        #         can3 = can3 + 1
#if the name isnt in my name array then I want to add it 

        
can1_percent = (can1 / rowcount) * 100
can2_percent = (can2 / rowcount) * 100
can3_percent = (can3 / rowcount) * 100

can_1_r = round(can1_percent, 3)
can_2_r = round(can2_percent, 3)
can_3_r = round(can3_percent, 3)

output =(
 f"Election Results\n"
 f"----------------------------------------\n"
 f"Total Votes: {rowcount}\n"
 f"----------------------------------------\n"
 f"Raymon Anthony Doane: {can_1_r}%\n"
 f"Diana Degette: {can_2_r}%\n"
 f"Charles Casper Stockham: {can_3_r}%\n"
 f"----------------------------------------\n"
 f"Winner: Diana DeGette"
)
          
print(output)

with open ("output2.txt", "w") as hw2file:
     hw2file.write(output)