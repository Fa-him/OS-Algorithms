b = int(input("Enter number of blocks: "))
block = [int(input(f"Block {i+1}: ")) for i in range(b)]
p = int(input("Enter the number of processes: "))
process = [int(input(f"Process {i+1}: ")) for i in range(p)]

temp = block.copy()
int_frag = 0
ext_frag = 0
total = sum(process)

for i in range(p):
    candidate = [x for x in temp if x >= process[i]]
    near = min(candidate)
    idx = block.index(near)
    temp[idx] -= process[i]
    int_frag += (near - process[i])
    total -= process[i]

if total != 0:
    ext_frag = sum(temp[i] for i in range(b) if temp[i] == block[i])

print(f"Internal Fragmentation: {int_frag}")
print(f"External Fragmentation: {ext_frag}")
print(f"Remaining Blocks: {temp}")
