def selection_sort(arr):

    for i in range(len(arr)):
	
        min=i
	
        for k in range(i+1, len(arr)):
		
            if arr[k] < arr[min]:
		
                min=k
                
                
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp
                
    return arr
  
if __name__=="__main__":
  
    arr = [7,3,1,11,9]
  
    print(selection_sort(arr))
  
  
