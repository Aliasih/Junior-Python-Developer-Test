import json
from dateutil import parser
with open('sample-data.json') as f:
    data = json.load(f)

containers = data

for container in containers:
    name = container['name']
    cpu = container.get('cpu', {}).get('usage', 0)
    memory = container.get('state', {}).get('memory', {}).get(
        'usage', 0) if container and container.get('state') else 0
    created_at = container['created_at']
    status = container['status']
    addresses = []

    if container and container.get(
            'state') and 'network' in container['state']:
        if 'lo' in container['state']['network']:
            if 'addresses' in container['state']['network']['lo']:
                for address in container['state']['network']['lo'][
                        'addresses']:
                    addresses.append(address['address'])

    date = parser.parse(created_at)
    timestamp = date.timestamp()

    print(f'Name: {name}')
    print(f'CPU usage: {cpu}')
    print(f'Memory usage: {memory}')
    print(f'Created at: {created_at}')
    print(f'Status: {status}')
    print(f'IP Address: {addresses}')
