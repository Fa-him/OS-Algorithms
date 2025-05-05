#SCAN

#Here the track is 0 to 199

n=int(input("Enter how many tracks: "))
track=[int(input()) for i in range(n)]
head=int(input("Enter head: "))
h_or_l=int(input("Towards high or low? (1/0): "))

movement=0
if h_or_l:
    movement+=(199-head)
    movement+=(199-min(track))
else:
    movement+= head
    movement+=(max(track))

print("Total movement : " ,movement)
