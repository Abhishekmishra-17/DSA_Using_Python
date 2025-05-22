#0,1,1,2,3,5,8,13....
def fab_at_index(n):
    if n==1 or n==0:
        return n
    else:
        return fab_at_index(n-1)+fab_at_index(n-2)
    
# def fab_range(n):
#     if n==0:
#         return n
#     if n==1:
#         return 0, 1

if __name__ == "__main__":
    number = int(input("Enter the index number(Base 1)"))
    print(fab_at_index(number))

    for i in range(number+1):
        print(fab_at_index(i),end =" ")