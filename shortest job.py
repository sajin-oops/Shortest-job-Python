print('Shortest Job First Scheduling Algorithm')
print('****************************************')
n = int(input('enter no of processes:'))
total = 0
process = [0] * n
bt = [0] * n
wt = [0] * n
tat = [0] * n
for i in range(n):
 print("P" + str(i + 1))
 bt[i] = int(input('Enter burst time:'))
 process[i] = i+1
for i in range(n):
 pos = i
 for j in range(i+1,n):
  if bt[j] < bt[pos]:
     pos = j
process = [i for _i in sorted(zip(bt,process))]
bt = [i for _,i in sorted(zip(process,bt))]
print(process,bt)
#first process has waiting time 0
wt[0] = 0
#calculate waiting time
for i in range(1,n):
 wt[i]=0
 for j in range(i):
  wt[i] += bt[j]
total += wt[i]
#calculating average waiting time
wait_avg = total/n
total = 0
print('\n Pno BT WT TAT')
for i in range(n):
 tat[i] = bt[i] + wt[i]
 total += tat[i]
 print('\n', process[i],' ',bt[i],' ',wt[i],' ',tat[i])
tat_avg = total/n
print('Average Waiting Time:%0.2f ms' %(wait_avg))
print('Average Turn Around Time:%0.2f ms' %(tat_avg))
