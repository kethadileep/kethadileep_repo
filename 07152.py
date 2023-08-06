# Jumping on the clouds, where some of the clouds are thunderheads and others are cumulus. A player  can jump  one/two clouds from the current cloud by avoiding the jump on thunderheads. Find the minimum number of jumps from the first cloud to end cloud.  In array: 1: thunderhead and 0 cumulus. Example:  arr={0,1,0,0,0,1,0}
#   Two paths are possible 0->2->4->6 and 0->2->3->4->6   
#              Answer : 3 (minimum jumps)



arr=[0,1,0,0,0,1,0]

cumulus = []
index = 0
assending = 0
for i in arr:
    if i == 0:
        # cumulus.append(arr.index(i))
        cumulus.append(index)
    index +=1


print(cumulus)



