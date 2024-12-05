import re

with open('3-1.txt', 'r') as f:
    data = f.read()
    
    # find all instances of mul(num1, num2) in file
    exp = re.compile(r'mul\((\d+),(\d+)\)')
    matches = exp.findall(data)

    #extract integers, multiply and sum
    match_nums = [(int(num1), int(num2)) for num1, num2 in matches]
    products = sum([num1*num2 for num1, num2 in match_nums])
    print(products)


    # part 2
    # find the first instance of don't() and get all instances of mul(num1, num2) before it
    exp3 = re.compile(r'don\'t\(\)')
    dont_index = exp3.search(data)
    matches_before = exp.findall(data[:dont_index.start()])
    tuples_before_dont = [(int(num1), int(num2)) for num1, num2 in matches_before]
    products_before_dont = sum([num1*num2 for num1, num2 in tuples_before_dont])
    
    # find all do()don't() pairs and get the text between
    exp2 = re.compile(r'do\(\)(.*?)don\'t\(\)')
    blocks = exp2.findall(data)

    matches2 = []
    # for each do()don't() block, find all instances of mul(num1, num2)
    for block in blocks:
        matches2.extend(exp.findall(block))
    
    tuples2 = [(int(num1), int(num2)) for num1, num2 in matches2]
    products2 = sum([num1*num2 for num1, num2 in tuples2])

    print(products2 + products_before_dont)
    