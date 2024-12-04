

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

dampening = False

safelist = 0
with open('2-1.txt', 'r') as file:
    for line in file:
        int_list = [int(x) for x in line.strip().split()]
        diff = make_diff(int_list)
        
        if dampening == False:
            if check_sign(diff) and check_range(diff) == True:
                safelist += 1
        
        
        elif dampening == True:
            sign = check_sign(diff)
            range_verdict = check_range(diff)

            if sign == False or range_verdict == False:
                list_length = len(int_list)
                for i in range(list_length):
                    new_list = int_list[:i] + int_list[i+1:]
                    new_diff = make_diff(new_list)
                    sign = check_sign(new_diff)
                    range_verdict = check_range(new_diff)

                    if sign and range_verdict == True:
                        break
                    else:
                        continue

            if sign and range_verdict == True:
                safelist += 1
     
    print("Dampening", dampening, ". Number of safe reports: ", safelist)



