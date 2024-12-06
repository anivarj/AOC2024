import re
from functools import cmp_to_key

def get_positions_and_rules(update, rules_set):
    page_positions = {page: i for i, page in enumerate(update)}
    relevant_rules = [rule for rule in rules_set if rule[0] in update and rule[1] in update]
    
    return page_positions, relevant_rules

# Validation function for an update
def is_valid_update(page_positions, relevant_rules):
    for before, after in relevant_rules:
        if page_positions[before] > page_positions[after]:
            return False  # Rule violated
    return True


# Custom comparator that uses relevant rules (which are changed in each iteration)
def get_custom_comparator(relevant_rules):
    # the custom comparator function
    def custom_comparator(a, b):
        # Match the relevant rule with the current pair of pages
        for before, after in relevant_rules:
            # If a comes before b, return -1
            if before == a and after == b:
                return -1  
            # If b comes before a, return 1
            elif before == b and after == a:
                return 1  
        return 0  # No rule defines the order
    return custom_comparator

with open('5-1.txt') as f:
    lines = [l.strip() for l in f.readlines()]

# Regex patterns
rules_pattern = re.compile(r'(\d+)\|(\d+)')  # Matches number|number
pages_pattern = re.compile(r'^(\d+(?:,\d+)*)$')  # Matches number,number,...

# Process rules with list comprehensions
# Find all rules (number|number) and convert to tuples
rules = [
    tuple(map(int, rules_pattern.search(line).groups())) for line in lines if rules_pattern.search(line)
]

rules_set = set(rules)

# Find all pages (number,number,...) and convert to list of lists. Each list is an update (row).
pages = [
    list(map(int, pages_pattern.search(line).group(1).split(','))) for line in lines if pages_pattern.search(line)
]

# Part 1
valid_middle_pages = []
for page_list in pages:
    page_positions, relevant_rules = get_positions_and_rules(page_list, rules_set)

    if is_valid_update(page_positions, relevant_rules):
        # Add the middle page if the update is valid
        middle_page = page_list[len(page_list) // 2]
        valid_middle_pages.append(middle_page)

# Sum the middle pages of valid updates
result = sum(valid_middle_pages)
print(f"Sum of middle pages: {result}")   


# Part 2
fixed_middle_pages = []

for page_list in pages:
    page_positions, relevant_rules = get_positions_and_rules(page_list, rules_set)

    # if the update is not value, sort the list using a custom comparator
    if not is_valid_update(page_positions, relevant_rules):
        comparator = get_custom_comparator(relevant_rules)
        sorted_list = sorted(page_list, key=cmp_to_key(comparator))    
        middle_page = sorted_list[len(sorted_list) // 2]
        fixed_middle_pages.append(middle_page)

part2_result = sum(fixed_middle_pages)
print(part2_result)
