data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:  # % = 餘數 , 1002 % 1000 = 2  1006 % 1000 = 6
			print(len(data))
print('總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[8])

good = []  #[d for d in data if 'good' in d]
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到')
print(good[6])



