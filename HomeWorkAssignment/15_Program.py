def merge_arrays(a, b):
    n, m = len(a), len(b)

    def next_gap(gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)

    gap = next_gap(n + m)

    while gap > 0:
        i = 0
        j = gap

        while j < n + m:
            # Both pointers in array a
            if i < n and j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]

            # i in a, j in b
            elif i < n and j >= n:
                if a[i] > b[j - n]:
                    a[i], b[j - n] = b[j - n], a[i]

            # Both pointers in array b
            else:
                if b[i - n] > b[j - n]:
                    b[i - n], b[j - n] = b[j - n], b[i - n]

            i += 1
            j += 1

        gap = next_gap(gap)


