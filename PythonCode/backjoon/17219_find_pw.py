import sys
import io

input_string = '''16 4
noj.am IU
acmicpc.net UAENA
startlink.io THEKINGOD
google.com ZEZE
nate.com VOICEMAIL
naver.com REDQUEEN
daum.net MODERNTIMES
utube.com BLACKOUT
zum.com LASTFANTASY
dreamwiz.com RAINDROP
hanyang.ac.kr SOMEDAY
dhlottery.co.kr BOO
duksoo.hs.kr HAVANA
hanyang-u.ms.kr OBLIVIATE
yd.es.kr LOVEATTACK
mcc.hanyang.ac.kr ADREAMER
startlink.io
acmicpc.net
noj.am
mcc.hanyang.ac.kr'''

# Replace sys.stdin with StringIO object containing the input_string
sys.stdin = io.StringIO(input_string)

N, M = map(int, sys.stdin.readline().split())
d = dict()

for _ in range(N):
    url, pw = map(str, sys.stdin.readline().split())
    d[url] = pw

for _ in range(M):
    req = sys.stdin.readline().strip()
    print(d[req])

