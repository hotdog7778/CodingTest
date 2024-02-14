import sys
inputLC = sys.stdin.readline().rstrip()
alphabet_count_in_password, alphabet_count = map(int, inputLC.split())
alphabets = sys.stdin.readline().rstrip().split()

# print(alphabet_count_in_password, alphabet_count, alphabets)

from itertools import combinations
alphabets.sort()
words = list(combinations(alphabets, alphabet_count_in_password))
# print(words)
for password in words:
    # password는 튜플
    # 자음 모음 검사
    vow = 0 # 모음
    con = 0 # 자음
    for word in password:
        if word in ["a","e","i","o","u"]:
            vow += 1
        else :
            con += 1
    
    if vow >= 1 and con >= 2:
        print(''.join(list(password)))