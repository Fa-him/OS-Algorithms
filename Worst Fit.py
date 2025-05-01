def worst_fit(blocks, processes):
    n = len(blocks)
    temp = blocks.copy()
    allocation = [-1] * len(processes)
    internal_frag = 0

    for i, p in enumerate(processes):
        worst_idx = -1
        max_diff = -1
        for j in range(n):
            if temp[j] >= p and temp[j] - p > max_diff:
                worst_idx = j
                max_diff = temp[j] - p
        if worst_idx != -1:
            allocation[i] = worst_idx
            internal_frag += temp[worst_idx] - p
            temp[worst_idx] = -1

    external_frag = sum(temp[j] for j in range(n) if temp[j] != -1)

    print("\nWorst Fit:")
    print(f"Internal Fragmentation: {internal_frag}")
    print(f"External Fragmentation: {external_frag}")
    for i, alloc in enumerate(allocation):
        if alloc != -1:
            print(f"Process {i+1} allocated to Block {alloc+1}")
        else:
            print(f"Process {i+1} Not Allocated")


def main():
    b = int(input("Enter number of blocks: "))
    blocks = [int(input(f"Block {i+1}: ")) for i in range(b)]

    p = int(input("Enter number of processes: "))
    processes = [int(input(f"Process {i+1}: ")) for i in range(p)]

    worst_fit(blocks, processes)


if __name__ == "__main__":
    main()
