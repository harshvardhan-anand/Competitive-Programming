s = 'abba'
n = len(s)
table = [[False]*n for i in range(n)]

max_len = 0
for i in range(n):
    table[i][i] = True
    if max_len<1:
        max_len = 1
        start = i
        end = i

for i in range(n-1):
    if s[i]==s[i+1]:
        table[i][i+1] = True
        if max_len<2:
            max_len = 2
            start = i
            end = i
k = 3
while k<n:
    for i in range(n-2):
        if s[i] == s[i+k-1]:
            if table[i+1][i+k-2]:
                table[i][i+1] = True
                print(i+k-1)
                if max_len<(i+k-1):
                    max_len = i+k-1
                    start = i
                    end = i+k-1
    k+=1

max_len