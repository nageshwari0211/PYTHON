n=int(input())
for i in range(1,n+1):
    if(i==1):
        star="* "
        mid_space=2*n-(i+i)
        row=star+mid_space*"  "+star
    else:
        star="* "
        left_hollow=(2*i-4)*" "
        mid_space=2*n-(i+i)
        right_space=(2*i-4)*" "
        row=star+left_hollow+star+mid_space*"  "+star+right_space+star
    print(row) 
for i in range(n):
    if(i==n-1):
        star="* "
        mid_space=2*n-2
        row=star+mid_space*"  "+star
    else:
        star="* "
        left_hollow=(((n-i)-1)-1)*"  "
        mid_space=(2*n-2*(n-i))
        right_space=(((n-i)-1)-1)*"  "
        row=star+left_hollow+star+mid_space*"  "+star+right_space+star
    print(row)