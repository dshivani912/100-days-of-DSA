# Find the Union and Intersection of the two sorted arrays.

def union_intersection(a,b):
  c=[]
  union=set(a+b)
  a=set(a)
  b=set(b)
  for i in a:
      if i in b:
          c.append(i)
  return list(union),c
a=list(map(int,input().split()))
b=list(map(int,input().split()))
union,intersection=union_intersection(a,b)
print(union)
print(intersection)
