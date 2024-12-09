# 포켓몬 도감 완성시키기!
# 현재 가지고 있는 포켓몬 도감에서
# 포켓몬 이름을 보면 => 포켓몬의 번호를 말한다.
# 포켓몬의 번호를 보면 => 포켓몬의 이름을 말한다.


# 포켓몬의 개수 n, 문제의 개수 m
# n개의 줄에 거쳐 1번인 포켓몬부터 n번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어온다.
# 이후 M개의 줄에 내가 맞춰야 하는 문제가 입력으로 들어옴

import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
pokemon = dict()
pokemon_name = dict()
for i in range(1,n+1):
  poke = input().rstrip('\n')
  pokemon[i] = poke
  pokemon_name[poke] = i

for i in range(m):
  pk = input().rstrip('\n')
  if pk.isdigit():
    print(pokemon[int(pk)])
  else:
    print(pokemon_name[pk])


    
