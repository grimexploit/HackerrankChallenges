if __name__ == '__main__':		#List bolon Tuple iin yalgaag olj medeerei.
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))