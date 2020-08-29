
def min_henchmen(total_lambs):
    count=0
    sum=0

    while count <= total_lambs:
        currentvalue = 2**count

        if sum + currentvalue > total_lambs:
            break

        sum += currentvalue
        count += 1

    return count


def max_henchmen(total_lambs):
    previous = 0
    current = 1
    count = 0
    sum = 0
    while sum < total_lambs:
        old_current = current
        current = current + previous
        sum = sum + current
        count = count + 1
        previous = old_current2
    return count


def solution(total_lambs):
    return max_henchmen(total_lambs) - min_henchmen(total_lambs)
