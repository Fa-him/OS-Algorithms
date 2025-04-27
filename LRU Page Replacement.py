def lru_page_replacement(pages, frame_count):
    n = len(pages)
    arr = [[-1] * n for _ in range(frame_count)]
    frames = []
    page_faults = 0
    page_hits = 0

    for i in range(n):
        page = pages[i]

        if page in frames:
            page_hits += 1
        else:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                last_used = []
                for f in frames:
                    found = False
                    for j in range(i - 1, -1, -1):
                        if pages[j] == f:
                            last_used.append(j)
                            found = True
                            break
                    if not found:
                        last_used.append(-1)

                min_index = float('inf')
                replace_frame = None
                for idx in range(len(frames)):
                    if last_used[idx] < min_index:
                        min_index = last_used[idx]
                        replace_frame = frames[idx]

                replace_position = frames.index(replace_frame)
                frames[replace_position] = page
            page_faults += 1

        for k in range(frame_count):
            if k < len(frames):
                arr[k][i] = frames[k]
            else:
                arr[k][i] = -1

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
lru_page_replacement(pages, f)
