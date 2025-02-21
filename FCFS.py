def assign_name(n):
    return [f"P{i + 1}" for i in range(n)]


def input_at_bt(n):
    at_arr, bt_arr = [], []

    for i in range(n):
        at, bt = map(int, input(f"P{i + 1}: ").split())
        at_arr.append(at)
        bt_arr.append(bt)

    return at_arr, bt_arr


def find_ct(at_arr, bt_arr, n):
    ct_arr = [0] * n
    curr = 0

    indices = list(range(n))
    sorted_indices = sorted(indices, key=lambda x: at_arr[x])

    for i in sorted_indices:
        if curr < at_arr[i]:
            curr = at_arr[i]
        curr += bt_arr[i]
        ct_arr[i] = curr

    return ct_arr


def find_tat(ct_arr, at_arr, n):
    return [ct_arr[i] - at_arr[i] for i in range(n)]


def find_wt(tat_arr, bt_arr, n):
    return [tat_arr[i] - bt_arr[i] for i in range(n)]


# Main Execution
n = int(input("Enter how many processes: "))
process = assign_name(n)

print("Enter Arrival Time and Burst Time for all processes (Format: AT BT)")
at_arr, bt_arr = input_at_bt(n)

ct_arr = find_ct(at_arr, bt_arr, n)
tat_arr = find_tat(ct_arr, at_arr, n)
wt_arr = find_wt(tat_arr, bt_arr, n)

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{process[i]}\t{at_arr[i]}\t{bt_arr[i]}\t{ct_arr[i]}\t{tat_arr[i]}\t{wt_arr[i]}")

avg_tat=sum(tat_arr)/n
avg_wt=sum(wt_arr)/n

print(f"Average TAT : {avg_tat}")
print(f"Average WT : {avg_wt}")