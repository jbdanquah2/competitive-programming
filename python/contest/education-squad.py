from collections import Counter

line1 = list(input())
line2 = list(input())
line3 = list(input())

heads_set = set(line1) | set(line2) | set(line3)
num_head = len(heads_set)/2

line1_len = len(Counter(line1).keys())
line2_len = len(Counter(line2).keys())
line3_len = len(Counter(line3).keys())

heads = {}
if line1_len < num_head:
    heads[str(line1_len)+'_line1'] = list(Counter(line1).keys())
if line2_len < num_head:
    heads[str(line2_len)+'_line2'] = list(Counter(line2).keys())
if line3_len < num_head:
    heads[str(line3_len)+'_line3'] = list(Counter(line3).keys())
    
lst_heads = []
lst_heads.extend([line1, line2, line3])

first_col = []
second_col = []
third_col = []

for ele in lst_heads:
    first_col.append(ele[0])
    second_col.append(ele[1])
    third_col.append(ele[2])

first_col_len = len(Counter(first_col).keys())
second_col_len = len(Counter(second_col).keys())
third_col_len = len(Counter(third_col).keys())

if first_col_len < num_head:
    heads[str(first_col_len)+'_first_col'] = list(Counter(first_col).keys())

if second_col_len < num_head:
    heads[str(second_col_len)+'_second_col'] = list(Counter(second_col).keys())
    
if third_col_len < num_head:
    heads[str(third_col_len)+'_third_col'] = list(Counter(third_col).keys())

diagonal1 = []
diagonal2 = []

diagonal1.append(line1[0])
diagonal1.append(line2[1])
diagonal1.append(line3[2])

diagonal2.append(line1[2])
diagonal2.append(line2[1])
diagonal2.append(line3[0])

diagonal1_len = len(Counter(diagonal1).keys())
diagonal2_len = len(Counter(diagonal2).keys())

if diagonal1_len < num_head:
    heads[str(diagonal1_len)+'_diagonal1'] = list(Counter(diagonal1).keys())
if diagonal2_len < num_head:
    heads[str(diagonal2_len)+'_diagonal2'] = list(Counter(diagonal2).keys())

count_1 = 0
count_above_1 = 0

for key in heads.keys():
    num = int(key.split('_')[0])
    
    if num == 1:
        count_1 += 1
    if num > 1:
        count_above_1 += 1
        
print(count_1)
print(count_above_1)
