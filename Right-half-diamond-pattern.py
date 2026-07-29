cnt = 1
m = int(input("Enter the number you are up to print{numbers should be in range 2-9}:"))
space = m - 1

# Upper half:
for i in range(1, m + 1):
    print(space * " " + cnt * str(i))
    space -= 1
    cnt += 1

# Lower half:
cnt -= 2
for i in range(m - 1, 0, -1):
    print(cnt * str(i))
    cnt -= 1
