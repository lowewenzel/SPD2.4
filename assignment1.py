
def problem_one(a, t):
    seen = {}
    for k in a:
        val = seen.get(t-k, False)
        if val:
            return (k, t-k)
        seen[k] = True


def problem_two(a, k):
    if k > len(a):
        raise Error('count is larger than number of items')

    a.sort()

    return[(len(a) - k):]
