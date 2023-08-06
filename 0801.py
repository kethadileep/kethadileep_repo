import time

# start1 = time.time_ns()
# len([1,2,3,4,5,6,7,8,9,10])
# time.sleep(1)
# end1 = time.time_ns()
# print(end1 - start1)



list2 = [i for i in range(10000000)]
start2 = time.time_ns()
for i in range(3000):
    len(list2)
end2 = time.time_ns()
timetaken = end2 - start2
print(timetaken/3000)

