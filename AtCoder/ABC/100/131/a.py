S = list(input())

count = 0

for i in range(0, len(S)-1) :
    if S[i] == S[i+1] :
        count += 1

if count == 0 :
    print('Good')
else :
    print('Bad')