# Write a recursive function that takes one parameter: n and counts down from n.

def counting_down(n):
    print(n)
    if n == 0:
        return 0
    else:
        return counting_down(n-1)

counting_down(10)