from itertools import combinations 

def kombinacje(asd, r):  
	return list(combinations(asd, r)) 

if __name__ == "__main__": 
	asd = [1, 2, 3, 4] 
	r = 3
	print (kombinacje(asd, r)) 