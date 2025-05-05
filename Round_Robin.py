def input_at_bt(n):
    at_arr, bt_arr = [], []

    for i in range(n):
        at, bt = map(int, input(f"P{i + 1}: ").split())
        at_arr.append(at)
        bt_arr.append(bt)
    return at_arr, bt_arr


def find_ct_rr(at_arr, bt_arr, n, time_quantum):
    ct_arr = [0] * n
    remaining_time = bt_arr.copy()
    curr_time = 0
    order = []

    while True:
        all_completed = True
        for i in range(n):
            if remaining_time[i] > 0 and at_arr[i] <= curr_time:
                all_completed = False
                if remaining_time[i] > time_quantum:
                    curr_time += time_quantum
                    remaining_time[i] -= time_quantum
                else:
                    curr_time += remaining_time[i]
                    remaining_time[i] = 0
                    ct_arr[i] = curr_time
                order.append(process[i])

        if all_completed:
            break

    return ct_arr, order


# Main Execution
n = int(input("Enter how many processes: "))
process = [f"P{i + 1}" for i in range(n)]

print("Enter Arrival Time and Burst Time for all processes (Format: AT BT)")
at_arr, bt_arr = input_at_bt(n)

time_quantum = int(input("Enter Time Quantum: "))

ct_arr, order = find_ct_rr(at_arr, bt_arr, n, time_quantum)
tat_arr = [ct_arr[i] - at_arr[i] for i in range(n)]
wt_arr = [tat_arr[i] - bt_arr[i] for i in range(n)]

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{process[i]}\t{at_arr[i]}\t{bt_arr[i]}\t{ct_arr[i]}\t{tat_arr[i]}\t{wt_arr[i]}")

avg_tat = sum(tat_arr) / n
avg_wt = sum(wt_arr) / n

print(f"Order of Execution: {order}")
print(f"Average TAT: {avg_tat}")
print(f"Average WT: {avg_wt}")
