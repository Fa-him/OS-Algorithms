b=int(input("Enter number of block: "))
block=[int(input(f"Block {i+1}: ")) for i in range(b)]
p=int(input("Enter the number of process: "))
process=[int(input(f"Process {i+1}: ")) for i in range(p)]
temp=block.copy()
int_frag=0
ext_frag=0
total=sum(process)

for i in range(p):
    for j in range(b):
        if process[i]<=block[j] and temp[j]==block[j]:
            temp[j]-=process[i]
            int_frag+=temp[j]
            total-=process[i]
            break
if total!=0:
    ext_frag += sum(temp[i] for i in range(b) if temp[i] == block[i])

print(f"Internal Fragmentation: {int_frag}")
print(f"External Fragmentation: {ext_frag}")
print(temp)

