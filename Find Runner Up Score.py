if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) #array buyu massive iig avch baina
    k = max(arr)	#tuhain array-d ugugdsun elementuudiin hamgiin ih utgiig k huvisagchid hadgalav.
    for i in range(n):
        if max(arr) == k : 	#davtalt guilgeed hervee tuhain array iin max element ni bidnii umnu hadgalsan k tai tentsuu baih ym bol
            arr.remove(max(arr))	#tuhain elementiig listees hasna
    arr.sort(reverse=True)		#ihees ni bagaruu sortlono

    print(arr[0])		#hamgiin ehnii element runner up score baih bolno.
