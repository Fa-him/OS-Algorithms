#C_SCAN
#Here the track is 0 to 199

n=int(input("Enter how many tracks: "))
track=[int(input()) for i in range(n)]
head=int(input("Enter head: "))
h_or_l=int(input("Towards high or low? (1/0): "))

movement=0
track.sort()

if h_or_l:
    right=[t for t in track if t>=head]
    left=[t for t in track if t<head]

    if right:
        movement+=(199-head)
        if left:
            movement+=199
            movement+=left[-1]
else:
    left=[t for t in track if t<=head]
    right=[t for t in track if t>head]

    print(right)
    print(left)

    if left:
        movement+=head
        if right:
            movement+=199
            movement+=(199-right[0])

print("Total movement: ", movement)
