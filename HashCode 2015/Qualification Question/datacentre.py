# 2 5 1 2 5  2 rows of 5 slots each, 1 slot unavailable, 2 pools and 5 servers
# 0 0 Coordinates of the first and only unavailable slot
# 3 10 First server takes three slots and has a capacity of 10
# 3 10 Second server takes three slots and has a capacity of 10
# 2 5 Third server takes two slots and has a capacity of 5
# 1 5 Fourth server takes one slot and has a capacity of 5
# 1 1 Fifth server takes one slot and has a capacity of 1

# First Line:

# R = Rows (1-1000)
# S = Slots (1-1000)
# U = Unavailable Slots (0-R*S)
# P = Pools (1-1000)
# M = Servers (1-R*S)

# U subsequent lines are the unavailable slots, row number then slot number eg (0,1) = row 0 slot 1
# M subsequent lines are the servers, physical size of server then capacity of the server eg (3,10) = 3 slots, 10 capacity

# Test file first line = 16 100 80 45 625
# 16 Rows
# 100 Slots
# 80 Unavailable Slots
# 45 Pools
# 625 Servers

# Followed by 80 lines of unavailable slots and 625 lines of servers

import pandas as pd
import numpy as np

with open("HashCode 2015\Qualification Question\dc.in", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
# print(lines)
rows = int(lines[0].split()[0])
slots = int(lines[0].split()[1])
unavailable = int(lines[0].split()[2])
pools = int(lines[0].split()[3])
servers = int(lines[0].split()[4])

badSlots = lines[1:unavailable+1]
servers = lines[unavailable+1:unavailable+1+servers]

RxS = rows * slots
availableSlots = RxS - unavailable

totalSize = 0
totalCapacity = 0

# print(rows)
# print(slots)
# print(unavailable)
# print(pools)
# print(servers)
# print(badSlots)
# print(len(badSlots))
# print(servers)
# print(len(servers))

serversTuple = []
for server in servers:
    serversTuple.append(tuple(map(int, server.split(' '))))

df = pd.DataFrame(serversTuple, columns=['size', 'capacity'])

totalSize = df['size'].sum()
totalCapacity = df['capacity'].sum()
df["ratio"] = df["capacity"] / df["size"] 
print(df)

print("Total Size:", totalSize)
print("Available Slots", availableSlots)
deficit = totalSize - availableSlots
print("Deficit", deficit)

print("Total Capacity:", totalCapacity)

print("Ideal Capacity per Pool:", totalCapacity/pools)
print("Ideal Capacity per row:", totalCapacity/rows)


df = df.sort_values('ratio', ascending=False)
print(df)

# loop over df and sum the capacity of servers and the size of servers until the available slots

# df = pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})

# for index, row in df.iterrows():
#     print(row['c1'], row['c2'])

runningCapacity = 0
runningSize = 0

for index, row in df.iterrows():
    if (runningSize + row["size"]) > availableSlots:
        break
    # print(row)
    runningCapacity += row["capacity"]
    runningSize += row["size"]
    totalServers = index

print(runningCapacity)
print(runningSize)
print(totalServers)

badSlots = [tuple(map(int, badSlot.split(' '))) for badSlot in badSlots]
print(badSlots)
print(len(badSlots))

myvec = np.arange(0, RxS)
mydf = pd.DataFrame(myvec.reshape(-1, slots))
print(mydf)

for x in badSlots:
    mydf.iloc[x] = "BLOCKED"
print(mydf)

mydf2 = mydf[mydf]