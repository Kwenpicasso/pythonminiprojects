import random
print("fanatasy name generator")
first_name=['kwen','leke', 'dbaby', 'chris']
last_name = ['sese', 'john', 'ada']

counts = int(input("how many names do you want?: "))

for count in range(counts):
    first = random.choice(first_name)
    last = random.choice(last_name)
    print(f"{first}{last} {count}")