def merge_the_tools(string, k):
    n = len(string)
    # create list of u's
    u_list = [string[i:i+n] for i in range(0, len(string), k)]
    for u in u_list:
        # for each u: remove repeated chars
        u_fixed = ''.join(sorted(set(u), key=u.index))
        print(u_fixed)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
