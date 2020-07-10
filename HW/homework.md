[ahomework](https://www.udemy.com/course/git-bash/)   

homework = understand what every line in a script works

```
n=int(input("Enter number of rows: "))  # n = cipars! Ievadiet rindu daudzumu
a=[] # Empty list
for i in range(n):   #
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()
```



uztaisīt statistiku cik cipari cik reizes atkārtojas 2** 1000
