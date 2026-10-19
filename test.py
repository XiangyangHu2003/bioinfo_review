if __name__ == '__main__':
    N = int(input())

    ls = []

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            i = command[1]
            e = command[2]
            ls.insert(i, e)

        if command[0] == "print":
            print(ls)

        if command[0] == "remove":
            i = command[1]
            ls.remove(i)

        if command[0] == "append":
            i = command[1]
            ls.append(i)

        if command[0] == "sort":
            ls.sort()

        if command[0] == "pop":
            ls.pop()

        if command[0] == "reverse":
            ls.reverse()
