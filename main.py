def sum_range(start, end):
    if start < end:
        return sum(range(start, end + 1))
    else:
        return sum(range(end, start + 1))

print(sum_range(s, e))