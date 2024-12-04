

### 2-1 ###

# creates a subtraction array showing the differences between elements
def make_diff(input_list):
    list1 = input_list[:-1]
    list2 = input_list[1:]
    diff = [x - y for x, y in zip(list1, list2)]
    return(diff)

# check to see that all signs are positive or all negative (no mixed)
def check_sign(diff_list):
    if 0 in diff_list:
        return False
     
    return all(x > 0 for x in diff_list) or all(x < 0 for x in diff_list)

# check to see that no difference is greater than 3 or less than -3
def check_range(diff_list):
    return all( -3 <= x <= 3 for x in diff_list)


safelist = 0
with open('2-1.txt', 'r') as file:
    for line in file:
        int_list = [int(x) for x in line.strip().split()]
        diff = make_diff(int_list)
        
        if check_sign(diff) and check_range(diff) == True:
            safelist += 1

print("Number of safe reports: ", safelist)

### 2-2 ###


safelist2 = 0

with open('2-1.txt', 'r') as file:
    for line in file:
        int_list2 = [int(x) for x in line.strip().split()]
        diff2 = make_diff(int_list2)
        
        print("safelist2", safelist2)
        print(diff2)
        
        sign = check_sign(diff2)
        range_verdict = check_range(diff2)
        print("check sign", sign)
        print("check_range", range_verdict)


        if sign == False or range_verdict == False:
            print("attempting to fix issues...")
            list_length = len(diff2)
            for i in range(list_length):
                new_list = diff2[:i] + diff2[i+1:]
                print("new list", new_list)
                sign = check_sign(new_list)
                range_verdict = check_range(new_list)
                
                if sign and range_verdict == True:
                    print("issue resolved!")
                    break
                else:
                    print("Issues persist. Continuing on...")
                    continue
            
        print("final check sign:", sign)
        print("final check range:", range_verdict)

        if sign and range_verdict == True:
            print("adding to safe list...")
            safelist2 += 1
       
        else:
            print("nothing added to safelist2")

print("Number of safe reports: ", safelist2)