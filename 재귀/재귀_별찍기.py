N = int(input())

def print_star(n):
    if n==1:
        return "*"
    
    star_ret = print_star(n//3)

    L = []
    for star in star_ret:
        L.append(star+ star + star)
    for star in star_ret:
        L.append(star + " "*(n//3) + star )
    for star in star_ret:
        L.append(star + star + star)
    
    return L


result = print_star(N)
print('\n'.join(result))

