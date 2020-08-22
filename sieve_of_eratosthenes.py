

user_data = int(input("n = "))

x = 0
p = 2


list_nb = list(range(2, user_data + 1 ))
temp_list = list(range(2, user_data + 1 ))

while x <= (user_data - 2):
    nums = range(p, user_data + 1, p)
    non_prime_list = list(nums)
    print(non_prime_list)
    p = temp_list[x]

    for i in list_nb[:]:
        if i in non_prime_list:
            list_nb.remove(i)
            non_prime_list.remove(i)

    if p**2 >= user_data:
        break
    x += 1



for n in list_nb:
    print(n)
