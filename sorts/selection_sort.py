def selection_sort(arr):

    for i in range(len(arr)):

        for k in range(i+1, len(arr)):
		
            if arr[i] > arr[k]:
			
                temp=arr[i]
                arr[i]=arr[k]
                arr[k]=temp

    return arr
  
if __name__=="__main__":
  
    arr = [5,7,1,2,9]
  
    print(selection_sort(arr))
  
  
