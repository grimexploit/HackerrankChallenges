if __name__ == '__main__':
    s = input()                 #ehleed zugeer res gedeg nertei bugdengiinh ni utga false baidag list uusgey
    res = ["False", "False", "False", "False", "False"]
    for i in s:             #for davtalt guilgej stringee unshiv
        if i.isalnum():         
            res[0] = "True"     #hervee string ni alphanumeric baival true utga ugnu
        if i.isalpha():         
            res[1] = "True"     #zuvhun usegnees burdsen baival true utga ugnu
        if i.isdigit():
            res[2] = "True"     #zuvhun too baival true utga ugnu
        if i.islower():
            res[3] = "True"      #zuvhun jijig useg baival ture utga ugnu
        if i.isupper():         
            res[4] = "True"
    print(*res, sep="\n")       #*res gedeg ni res listig buhleer ni hevlene. sep gedeg ni seperate buyu endline aar tusgaarlaj baina