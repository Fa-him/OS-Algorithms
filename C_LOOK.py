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
        movement+=(max(track)-head)
        if left:
            movement+=(max(track)-left[0])
            movement+=(left[-1]-left[0])
else:
    left=[t for t in track if t<=head]
    right=[t for t in track if t>head]
    if left:
        movement+=(head-left[0])
        if right:
            movement+=(max(track)-left[0])
            movement+=(max(track)-right[0])

print("Total movement: ", movement)
