from collections import Counter


data = [
    {
        "Name": "Андрей",
        "Hours": 9
    },
    {
        "Name": "Василий",
        "Hours": 11
    },
    {
        "Name": "Роман",
        "Hours": 7
    },
    {
        "Name": "X Æ A-12",
        "Hours": 45
    },
    {
        "Name": "Иван Петров",
        "Hours": 3
    },
    {
        "Name": "Андрей",
        "Hours": 6
    },
    {
        "Name": "Роман",
        "Hours": 11
    }
]

workers = Counter(d.get('Name') for d in data if d.get('Name'))
for worker, count in workers.most_common():
    hours = [employee.get('Hours') for employee in data if employee.get('Name') == worker]
    total = sum(employee.get('Hours') for employee in data if employee.get('Name') == worker)
    print("%s: %s; sum: %d" % (worker, ', '.join(str(hour) for hour in hours), total))
