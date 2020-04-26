def count_substring(string, sub_string):			
    total = 0 
    for i in range(0, len(string)):					#for davtalt guilgej stringee unshaad i dah elementees duustal ni guilgene
        if string[i:].startswith(sub_string):		#guij baih yavtsad sub_string taarah yum bol total iig 1 eer increment hiine. 
            total += 1 
    return total

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)