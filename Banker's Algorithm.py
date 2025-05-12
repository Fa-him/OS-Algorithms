def get_input_mat(p,r,name):
    print(f"Enter {name} matrix : ")
    matrix=[]
    for i in range(p):
        row=list(map(int, input(f"Row {i}: ").split()))
        while len(row)!=r:
            print(f"Each row must have {r} values.")
            row=list(map(int, input(f"Row {i}: ").split()))
        matrix.append(row)
    return matrix

def calculate_need_mat(maximum, allocation):
    return [[maximum[i][j] - allocation[i][j] for j in range(len(maximum[0]))] for i in range(len(maximum))]

def calculate_available(t_resource, allocation):
    r=len(t_resource)
    available=t_resource[:]
    for j in range(r):
        used=sum(allocation[i][j] for i in range(len(allocation)))
        available[j]-=used
    return available

def is_less_equal(need, available):
    return all(need[i]<=available[i] for i in range(len(available)))



def bankers():
    r=int(input("Enter the number of resources : "))
    t_resource=list(map(int,input(f"Enter all instances of {r} resource: ").split()))
    while len(t_resource)!=r:
        t_resource=list(map(int, input(f"Enter {r} values: ").split()))
    p=int(input("Enter the number of process: "))

    allocation=get_input_mat(p, r, "Allocation")
    maximum=get_input_mat(p,r, "Maximum")
    need=calculate_need_mat(maximum, allocation)
    available=calculate_available(t_resource, allocation)

    print("Initial Available Resources: ", available)
    print("Current resource need : ")
    for row in need:
        print(row)

    finished=[False]*p
    safe_seq=[]

    while True:
        found=False
        candidates=[]

        for i in range(p):
            if not finished[i] and is_less_equal(need[i], available):
                candidates.append(i)
        if not candidates:
            break

        i=min(candidates)
        print(f"Process p{i} can run.")
        for j in range(r):
            available[j]+=allocation[i][j]
        finished[i]=True
        safe_seq.append(f"P{i}")
        print("Updated available Resources: ", available)

    if all(finished):
        print("\nSystem is safe, no deadlock.")
        print("Safe sequence ",':'.join(safe_seq))
        print("Final available resource: ", available)
    else:
        print("Deadlock!")
        print("Process completed ", ":".join(safe_seq))
        print("Current Available Resource: ", available)

bankers()
