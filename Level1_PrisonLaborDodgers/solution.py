
def solution(x, y):
    first = x
    second = y
    if len(x) > len(y):
        second = x
        first = y
    exists = {}
    for ID in first:
        exists[ID] = True
    for ID in second:
        if ID not in exists.keys():
            return ID
