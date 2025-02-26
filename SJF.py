def input_at_bt(n):
    at_arr, bt_arr=[], []
    for i in range(n):
        at,bt=map(int,(input(f"P{i+1}: ").split()))
        at_arr.append(at)
        bt_arr.append(bt)
    return at_arr,bt_arr

def find_ct(at_arr, bt_arr, n):
    ct_arr=[0]*n
    curr=0
    order=[]
    completed=[False]*n

    for _ in range(n):
        min_bt=float('inf')
        idx=-1
        for i in range(n):
            if not completed[i] and at_arr[i]<= curr and bt_arr[i]<min_bt:
                min_bt=bt_arr[i]
                idx=i
        if idx== -1:
            curr+=1
            continue
        curr+=bt_arr[idx]
        ct_arr[idx]=curr
        completed[idx]=True
        order.append(f'P{idx+1}')

    return ct_arr, order

#main

n=int(input("Enter how many processes: "))
process=[f"P{i+1}: " for i in range(n)]

print("Enter AT and BT for all process: ")
at_arr, bt_arr=input_at_bt(n)

ct_arr, order=find_ct(at_arr,bt_arr,n)

tat_arr=[ct_arr[i]-at_arr[i] for i in range(n)]
wt_arr=[tat_arr[i]- bt_arr[i] for i in range(n)]

print('\nPro\tAT\tBT\tCT\tTAT\tWT')
for i in range(n):
    print(f'{process[i]}\t{at_arr[i]}\t{bt_arr[i]}\t{tat_arr[i]}\t{wt_arr[i]}')

avg_tat, avg_wt=sum(tat_arr)/n , sum(wt_arr)/n

print(f'order: {order}')
print(f'Average TAT: {avg_tat}')
print(f'Average WT: {avg_wt}')