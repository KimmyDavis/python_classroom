import timeit
file_str = open("wist.txt").read()
result_dict = {}

for chr in file_str:
    if chr in result_dict:
        result_dict[chr] += 1
    else:
        result_dict[chr] = 1
print("It took:", timeit.timeit())    
    
print(result_dict)
