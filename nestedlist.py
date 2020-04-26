score_list = [] 	#hooson array uusgej baina
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name, score])  #array ruugee name bolon score oo hiij baina
    second_lowest = sorted(set([score for name,score in score_list]))[1]	#list-dee set ashiglan buh onoonii davhardliig arilgana
    # daraa ni array-gaa bagaas ni ihruu ni sortlood [1] buyu ehneese 2doh elemtiig second_lowest huvisagchid hadgalj baina
    print('\n'.join(sorted([name for name, score in score_list if score == second_lowest])))	

    #'\n'.join gedeg ni hevleh ner bolgoniigoo shine murund hevlej baigaa bolno. Neg ysnii endline 
    #hevlehdee mun adil listee sortlood second_lowest-d hargalzsan utga ni score dund baih ym bol bugdeng ni hevlene