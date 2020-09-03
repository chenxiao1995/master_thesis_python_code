def min_cost(n, v1, v2, v3, v4):
    cost = 0
    n_cur = 0
    if n == 0:
        return 0
    n_cur += 1
    cost += v4
    print("+1")
    while n_cur < n:

        # while (v2 <= n_cur * v4 and (n_cur * 2 <= n)):
        #     n_cur = n_cur * 2
        #     cost += v2
        #     print("*2")

        while ((2 * v4 * n_cur)>=max(v1,(v2 + n_cur * v4)) and n_cur < n):
            if v1<(v2 + n_cur * v4):
                n_cur = n_cur * 3
                cost += v1
                print("*3")
            else:
                n_cur = n_cur * 2
                cost += v2
                print("*2")

        while(n_cur<n):
            n_cur += 1
            cost += v4
            print("+1")

    while n_cur > n:
        n_cur-=1
        cost = cost + v3
        print("-1")

    return cost

print(min_cost(256,1,1,1,1))
