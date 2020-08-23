def prime_eratosthenes(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
print(prime_eratosthenes(int(input("n = "))))




#Some old ugly code that doesnt really work
#
#
# user_data = int(input("n = "))
#
# x = 0
# p = 2
#
#
# list_nb = list(range(2, user_data + 1 ))
# temp_list = list(range(2, user_data + 1 ))
# prime_list
# while x <= (user_data - 2):
#     nums = range(p, user_data , p)
#     non_prime_list = list(nums)
#     print(non_prime_list)
#     p = temp_list[x]
#
#     for number in list(list_nb):
#         if number in non_prime_list:
#             if number not in prime_list:
#                 prime_list.append(number)
#
#     if p**2 >= user_data:
#         break
#     x += 1
# print("OUIIIIII ===== ", prime_list)
#
#
# for n in list_nb:
#     print(n)
