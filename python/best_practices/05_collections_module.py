# https://www.geeksforgeeks.org/python/python-collections-module/
from collections import Counter


cnt_lst = Counter([1,1,1,2,2,3,4,5,6,6,7,8,9,9,9])
print(f"From list to Counter {cnt_lst}")
print(f"Counter method most_common {cnt_lst.most_common(2)}")

dict_cnt = Counter({'A': 6, 'B': 3})
print(f"From dict to Counter {dict_cnt}")


keywrd_cnt = Counter(A=5, U=7)
print(f"From keyword arguments to Counter {keywrd_cnt}")



from collections import defaultdict

