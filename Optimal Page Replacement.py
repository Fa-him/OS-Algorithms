def optimal_page_replacement(pages, frame_count):
    n = len(pages)
    arr = [[-1] * n for _ in range(frame_count)]
    frames = [-1] * frame_count
    page_faults = 0
    page_hits = 0

    for i in range(n):
        page = pages[i]

        if page in frames:
            page_hits += 1
        else:
            if -1 in frames:
                empty_index = frames.index(-1)
                frames[empty_index] = page
            else:
                future_index = []
                for f in frames:
                    found = False
                    for j in range(i + 1, n):
                        if pages[j] == f:
                            future_index.append(j)
                            found = True
                            break
                    if not found:
                        future_index.append(float('inf'))

                max_future = -1
                replace_idx = -1
                for idx in range(len(frames)):
                    if future_index[idx] > max_future:
                        max_future = future_index[idx]
                        replace_idx = idx

                frames[replace_idx] = page

            page_faults += 1

        for k in range(frame_count):
            arr[k][i] = frames[k]

    print("ref_str", *pages)
    for i in range(frame_count):
        print(f"f{i+1}", end=" ")
        for j in range(n):
            if arr[i][j] == -1:
                print("x", end=" ")
            else:
                print(arr[i][j], end=" ")
        print()

    total = page_faults + page_hits
    print(f"PAGE FAULTS = {page_faults}")
    print(f"PAGE HITS = {page_hits}")
    print(f"FAULT RATE = {page_faults/total*100:.2f}%")
    print(f"HIT RATE = {page_hits/total*100:.2f}%")

n = int(input("Enter number of pages: "))
f = int(input("Enter number of frames: "))
pages = list(map(int, input("Enter the pages: ").split()))
optimal_page_replacement(pages, f)
