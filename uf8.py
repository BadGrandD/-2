def BinarySearch(inp, key):
  value = key + "\n"
  mid = len(inp) // 2
  low = 0
  low1 = "а"
  high = len(inp)-1
  high1 = "я"
  i = 0

  while inp[mid] != value and low <= high:
    if ord(value[0]) > ord(inp[mid][0]):
      low = mid + 1
      low1 = inp[mid+1][0]
      if inp[mid+1] == value:
        break
    else:
      high = mid - 1
      hihg1 = inp[mid-1][0]
      if inp[mid-1] == value:
        break
    mid = round((low + high) // 2)
    print(mid)
    print(inp[mid])
    print(value)
    print(inp[mid] == value)
  
  if low > high:
    print("No value")
  else:
    print("ID of ", value, " = ", mid)
    print(i)

def BinSearch(inp, key):
	count = 0
	low = 0
	high = len(inp) - 1
	
	while low <= high:
		md = (low + high) // 2
		if inp[md] == key:
			return md
		elif key > inp[md]:
			low = md + 1
		elif key < inp[md]:
			high = md
		count += 1
	return NULL