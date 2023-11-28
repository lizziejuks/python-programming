#inserting items into sorted lists
  x = [4, 1]
  x.sort()
  import bisect
  bisect.insort(x, 2)
  x
[1, 2, 4]