
# You can find the full explanation for this solution on my blog:
# https://blog.everythingdev.com/2020/12/google-foobar-please-pass-coded-messages.html

def solution(l):
    lLen = len(l)
    max = 1 << lLen
    l.sort(reverse=True)
    maxAttempt = 0
    for mask in reversed(range(max)):
        attempt = ""
        for index in range(mask.bit_length()):
            attempt += str(l[index]) if (mask >> index) & 1 == 1 else ''
        if attempt == '':
            attempt = 0
        attempt = int(attempt)
        if attempt % 3 == 0:
            if attempt > maxAttempt:
                maxAttempt = attempt

    return maxAttempt
