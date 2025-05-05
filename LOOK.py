#LOOK
#Here the track is 0 to 199
n=int(input("Enter how many tracks: "))
track=[int(input()) for i in range(n)]
head=int(input("Enter head: "))
h_or_l=int(input("Towards high or low? (1/0): "))

movement=0
if h_or_l:
    movement+=(max(track)-head)
    movement+=(max(track)-min(track))
else:
    movement+=(head-min(track))
    movement+=(max(track)-min(track))

print("Total movement : " ,movement)
