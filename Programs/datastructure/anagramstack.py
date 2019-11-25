from datastructure.Utility import prime, is_anagram, leng_th


# def prime():
#     lst = []
#     for num in range(1, 1000 + 1):
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 lst.append(num)
#     return lst
#
#
# def anagram(a):
#     # initialize a list
#     anagram_list = []
#     for i in a:
#         for j in a:
#             if i != j and (sorted(str(i)) == sorted(str(j))):
#                 anagram_list.append(i)
#     return anagram_list
#
#
# a = prime()
# t100 = a[0:1000]
#
# print(anagram(t100))

number = 12345

p = leng_th(number)
print(p)
