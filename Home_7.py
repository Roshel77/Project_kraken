import json

result = []
profit = {}
cost = []

with open('h7.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline().split()
        if not line:
            break
        profit[line[0]] = float(line[-2]) - float(line[-1])
        if profit[line[0]] > 0:
            cost.append(profit[line[0]])
result = [profit, {'average-cost': sum(cost) / len(cost)}]

with open('hw7.json', 'w', encoding='utf-8') as fw:
    json.dump(result, fw)