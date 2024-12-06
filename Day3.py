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
# find the first instance of don't() and get all instances of mul(num1,num2) before it
first_chunk = re.split(r'don\'t\(\)', data)[0]
first_matches = exp.findall(first_chunk)

# find the last instance of do() and get all instances of mul(num1,num2) after it
end_chunk = re.split(r'do\(\)', data)[-1]
end_matches = exp.findall(end_chunk)

# combine the two lists of matches and calculate the sum of products
termini_matches = first_matches + end_matches
termini_matches = [(int(num1), int(num2)) for num1, num2 in termini_matches]
termini_products= sum([num1*num2 for num1, num2 in termini_matches])

# find all do()don't() pairs and get the text between
do_dont = re.compile(r'do\(\)(.*?)don\'t\(\)')
dd_blocks = do_dont.findall(data)
dd_matches = []

# for each do()don't() block, find all instances of mul(num1, num2)
for block in dd_blocks:
    dd_matches.extend(exp.findall(block))

# extract integers, multiply and sum
dd_tuples = [(int(num1), int(num2)) for num1, num2 in dd_matches]
dd_products = sum([num1*num2 for num1, num2 in dd_tuples])
print(dd_products + termini_products)
    