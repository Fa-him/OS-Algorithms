def first_fit(blocks, processes):
    n = len(blocks)
    temp = blocks.copy()
    allocation = [-1] * len(processes)
    internal_frag = 0

    for i, p in enumerate(processes):
        for j in range(n):
            if temp[j] >= p:
                allocation[i] = j
                internal_frag += temp[j] - p
                temp[j] = -1
                break

    external_frag = sum(temp[j] for j in range(n) if temp[j] != -1)
    print("\nFirst Fit:")
    print_result(allocation, internal_frag, external_frag, blocks)


def next_fit(blocks, processes):
    n = len(blocks)
    temp = blocks.copy()
    allocation = [-1] * len(processes)
    internal_frag = 0
    last_alloc = 0

    for i, p in enumerate(processes):
        start = last_alloc
        while True:
            if temp[last_alloc] >= p:
                allocation[i] = last_alloc
                internal_frag += temp[last_alloc] - p
                temp[last_alloc] = -1
                last_alloc = (last_alloc + 1) % n
                break
            last_alloc = (last_alloc + 1) % n
            if last_alloc == start:
                break

    external_frag = sum(temp[j] for j in range(n) if temp[j] != -1)
    print("\nNext Fit:")
    print_result(allocation, internal_frag, external_frag, blocks)


def best_fit(blocks, processes):
    n = len(blocks)
    temp = blocks.copy()
    allocation = [-1] * len(processes)
    internal_frag = 0
    total = sum(temp)  # To calculate total free space at the beginning
    for i, p in enumerate(processes):
        best_idx = -1
        min_diff = float('inf')
        for j in range(n):
            if temp[j] >= p and temp[j] - p < min_diff:
                best_idx = j
                min_diff = temp[j] - p
        if best_idx != -1:
            allocation[i] = best_idx
            internal_frag += temp[best_idx] - p
            temp[best_idx] = -1

    external_frag = sum(temp[j] for j in range(n) if temp[j] != -1)
    print("\nBest Fit:")
    print_result(allocation, internal_frag, external_frag, blocks)


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
    print_result(allocation, internal_frag, external_frag, blocks)


def print_result(allocation, internal_frag, external_frag, blocks):
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

    first_fit(blocks, processes)
    next_fit(blocks, processes)
    best_fit(blocks, processes)
    worst_fit(blocks, processes)


if __name__ == "__main__":
    main()
