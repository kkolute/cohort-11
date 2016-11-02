def find_missing(list1,list2):
# initialize missing to zero
	missing = 0
# find and  display missing number if first list is smaller
	if len(list1) < len(list2):
		miss = (set(list2) - set(list1))
		absent = miss.pop()
		return absent
	#find and  display missing number if second list is smaller
	if len(list2) < len(list1):
		miss = (set(list1) - set(list2))
		absent = miss.pop()
		return missing

	else:
	  return 0