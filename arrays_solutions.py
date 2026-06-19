# 1.Smallest Element in Array
n=int(input())
arr=list(map(int, input().split()))
print(min(arr))

# 2.Largest Element in Array
n=int(input())
arr=list(map(int, input().split()))
print(max(arr))

# 3.Second Smallest Element
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr[1])

# 4.Second Largest Element
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr[-2])

# 5.Reverse Array
n=int(input())
arr=list(map(int,input().split()))
print(*arr[::-1])

# 6.Frequency of Elements
n=int(input( ))
arr=list(map(int,input().split()))
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    print(i,freq[i])

# 7.Remove Duplicates
n=int(input())
arr=list(map(int,input().split()))
arr1=[]
for i in arr:
    if i not in arr1: 
        arr1.append(i)
    else:
        pass
print(*arr1)

#or

n=int(input())
arr=list(map(int,input().split()))
print(*list(set(arr)))

# 8.Rotate Array by K Positions
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
print(arr)
print(arr[-k:]+arr[:-k])

# 9. Find Repeating Elements
n=int(input( ))
arr=list(map(int,input().split()))
freq={ }
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    if freq[i]>1:
       print(i)

# 10. Find Non-Repeating Elements
n=int(input( ))
arr=list(map(int,input().split()))
freq={ }
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
nr=[]
for i in freq:
    if freq[i]==1:
        nr.append(i)
print(*nr)

# 11. Equilibrium Index
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    l=sum(arr[:i])
    r=sum(arr[i+1:])
    if l==r:
        print(i)

#or 

n = int(input())
arr = list(map(int, input().split()))
total_sum = sum(arr)
left_sum = 0
for i in range(n):
    # right sum = total_sum - left_sum - arr[i](in both can use one)
    if left_sum == total_sum - left_sum - arr[i]:
        print("Equilibrium Index:", i)
    left_sum += arr[i]

# 12. Maximum Product Subarray
n=int(input())
arr=list(map(int,input().split()))
max_pro=0
for i in range(n):
    pro=1
    for j in range(i,n):
        pro=pro*arr[j]
        if pro>max_pro:
            max_pro=pro
        else:
            pass
print(max_pro)

#or

n=int(input())
arr=list(map(int,input().split()))
pro=1
for i in arr:
    pro*=i
print(pro)

# 13. Median of Array
n=int(input( ))
arr=list(map(int,input( ).split( )))
arr.sort( )
if n%2==1:
    print(arr[n//2])
else:
     print((arr[n//2-1]+arr[n//2])/2)


# # 14. Array Subset Check
n1=int(input())
a=list(map(int,input( ).split( )))
m1=int(input())
b=list(map(int,input( ).split( )))
for i in a:
    if i in b: 
        print("yes")
        break
else:
    print("No")

#15. Search Element
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
for i in arr:
    if i==target:
        print("Found")
        break
else:
    print("Not found")

# 16. Symmetric Pairs
n=int(input())
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))
sym=[]
for a,b in arr:
    if (b,a) in sym:
        print(a,b)
    else:
        sym.append((a,b))

#or

n=int(input())
d=[]
l=[]
for i in range(n):
    a,b=list(map(int,input().split()))
    if b in d and d[b]==a:
        l.append([b,a])
    else:
        d[a]=b
print(i)

# 17. Missing Number
n=int(input())
arr=list(map(int,input().split()))
ex=sum(range(min(arr),max(arr)+1))
missing=ex-sum(arr)
print(missing)

#or

n=int(input())
arr=list(map(int,input().split()))
total=n*(n+1)//2
total-sum(arr)
print(total-sum(arr))

# 18. Leaders in Array
n=int(input("Enter range:"))
l=list(map(int,input().split()))
for i in range(n):
    if i==n-1 or l[i]>=max(l[i+1:]) :
        print(l[i],end=" ")

#or

n=int(input("Enter range:"))
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]==max(l[i:]):
        print(l[i],end=" ")

# 19. Pair Sum
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
for i in arr:
    for j in arr:
        if i+j==target:
            print(i,j)
    break

# 20. Union and Intersection
N1 = int(input())
arr1 = list(map(int, input().split()))
N2 = int(input())
arr2 = list(map(int, input().split()))
set1 = set(arr1)
set2 = set(arr2)
union_result = sorted(set1.union(set2))
intersection_result = sorted(set1.intersection(set2))
print("Union:", *union_result)
print("Intersection:", *intersection_result)

# 21. Maximum Sum Subarray
n=int(input("Enter range"))
arr=list(map(int,input().split()))
max_sum=arr[0]
for i in range(n):
    sum=0
    for j in range(i,n):
        sum=sum+arr[j]
        max_sum=max(max_sum,sum)
print(max_sum)

#or

n = int(input("Enter size of array: "))
arr = list(map(int, input().split()))

max_sum = arr[0]
curr_sum = arr[0]

for i in range(1, n):
    # Either extend the current subarray or start new from arr[i]
    curr_sum = max(arr[i], curr_sum + arr[i])
    max_sum = max(max_sum, curr_sum)
print("Maximum Subarray Sum:", max_sum)

