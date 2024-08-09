import os
import csv
totalprofit = 0 
month = 0 
months = []
profitchange = []
Ph1challenge = os.path.join('PythonHW2.csv') 

with open(Ph1challenge) as PH1:
     Ph1data = csv.reader(PH1, delimiter = ",")
     Ph1dataHeader = next(Ph1data)
     #nextpro = int(next(Ph1data)[1])
     for row in Ph1data:
          #print(row) 
          month = month + 1
          profit2 = int(row[1])
          totalprofit = totalprofit + profit2
          #profitchange = (profit2 - nextpro) / 85
          #profitchange2 = profitchange[i + 1] - profitchange[i]
          months.append(row[0])
          profitchange.append(int(row[1]))
          
changes = [profitchange[i+1] - profitchange[i] for i in range(len(profitchange) - 1)]
changes_sum = sum(changes) / 85
changes_sum_r = round(changes_sum, 2)
max_increase = max(changes)
max_decrease = min(changes)
 
 

output = (
  f"Financial Analysis\n"
  f"-------------------\n"
  f"Total Months: {month}\n"
  f"Total: ${totalprofit}\n"
  f"Average Change: ${changes_sum_r}\n"
  f"Greatest Increase in Profits: ${max_increase}\n"
  f"Greatest Decrease in Profits: ${max_decrease}\n"
)

#print(output)

with open ("output.txt", "w") as hwfile:
     hwfile.write(output)



