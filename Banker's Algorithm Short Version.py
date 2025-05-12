def main():
    process = int(input("Enter number of processes: "))
    resources = int(input("Enter number of resources: "))

    print("Enter Allocation Matrix:")
    allocation = [list(map(int, input().split())) for _ in range(process)]

    print("Enter Maximum Matrix:")
    maximum = [list(map(int, input().split())) for _ in range(process)]

    print("Enter Available Resources:")
    available = list(map(int, input().split()))

    current_res = [[maximum[i][j] - allocation[i][j] for j in range(resources)] for i in range(process)]

    print("\nCurrent Resource Need Matrix:")
    for row in current_res:
        print(' '.join(map(str, row)))

    arr = [False] * process
    sequence = []
    cnt = 0

    print("\nAvailable Resources after each allocation:")
    for _ in range(process):
        for i in range(process):
            if not arr[i] and all(current_res[i][j] <= available[j] for j in range(resources)):
                arr[i] = True
                sequence.append(i)
                cnt += 1
                for j in range(resources):
                    available[j] += allocation[i][j]
                print(' '.join(map(str, available)))

    print()
    if cnt == process:
        print("Safe Sequence:")
        print("->".join(f"P{p}" for p in sequence))
    else:
        print("Deadlock")

main()
