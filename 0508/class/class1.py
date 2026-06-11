def unique_sort(lst):
  return sorted(set(lst))

lst = [80, 20, 20, 30, 60, 30]
print("주어진 리스트", lst)
newLst = unique_sort(lst)
print("정렬된 리스트", newLst)
