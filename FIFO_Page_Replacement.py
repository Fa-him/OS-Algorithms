def fifo_function(n, f, pages):
    memory=[-1]*f
    timeline=[[-1 for _ in range(n)] for _ in range(f)]
    next_replace=0
    miss=0
    hit=0

    for time in range(n):
        current_page=pages[time]

        if current_page in memory:
            hit+=1
        else:
            miss+=1
            memory[next_replace]=current_page
            next_replace=(next_replace + 1)% f

        for i in range(f):
            timeline[i][time]=memory[i]
    print("\nMemory Table (Each column is a step): \n")
    for i in range(f):
        row=[
            str(timeline[i][j]) if timeline[i][j] != -1 else "-"
            for j in range(n)
        ]
        print(" ".join(row))

    total=hit+miss
    print(f"\nPage Fault= {miss}")
    print(f"\nPage Hits= {hit}")
    print(f"\nMiss Rate= {miss/total *100:.2f}%")
    print(f"\nHit Rate= {hit/total *100:.2f}%")



n=int(input("Enter number of page references: "))
f=int(input("Enter number of frames: "))
pages=list(map(int , input("Enter the page reference string: ").split()))

fifo_function(n,f,pages)
