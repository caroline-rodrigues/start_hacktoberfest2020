arr = [2, 22, 11, 90, 72,43,15,64, 34, 25, 1] 

def selectionSort(num):

    for i in range(len(num)):
        min_index = i
        
        # find the smallest number in the remaining unsorted array
        for j in range(i+1,len(num)):
            if(num[min_index] > num[j]):
                min_index = j
        # swap it with the first number in the remaining unsorted array
        num[i],num[min_index] = num[min_index],num[i]

    print(num)

selectionSort(arr)
