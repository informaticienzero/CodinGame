from sys import stderr

n: int = int(input())
nb_max_stars: int = (n - 1) * 2 + 1
nb_spaces: int = nb_max_stars - 1
stars: int = 1

print('.' + (' ' * nb_spaces) + '*')
for i in range(1, n):
    stars += 2
    print(' ' * nb_spaces + '*' * stars)
    nb_spaces -= 1
  
stars = 1  
spaces_between: int = nb_max_stars
for i in range(n):
    print(' ' * nb_spaces + '*' * stars + ' ' * spaces_between + '*' * stars)
    stars += 2
    spaces_between -= 2
    nb_spaces -= 1
