def search_symbol(arg):
    '''
    input args:
    -   A random string in UTF8   5465468465326568766
    output:
    -   find  most frequently occurring character
    '''
    symbol_cnt = 0
    symbol = []
    for i in range(len(arg)):
        cnt = 0
        for j in range(len(arg)):
            if arg[i]==arg[j]:
                cnt = cnt + 1
        if cnt > symbol_cnt:
            symbol = arg[i]
            symbol_cnt = cnt

    return symbol

    


if __name__ == '__main__':
    #arg = input()
    arg = "123456"
    print(search_symbol(arg))
    a = [ 0.2, 3, 4, 5, 6 ]
    b = map(int, a)
    print(b)