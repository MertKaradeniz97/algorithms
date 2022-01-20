from array import array

def insertion_sort(s):
    s=[11,1,2,3,3,2]

    k=0
    for i in range(1,len(s)):
        for k in range(0,len(s)):
            if (s[i]<s[k]):

                s[k],s[i]=s[i],s[k]

            k+=1


    return s

s=[11,1,2,3,3,2]
insertion_sort(s)
