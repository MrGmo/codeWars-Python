from collections import defaultdict

def who_is_online(friends):
    d = defaultdict(list)
    for f in friends:
        name = f['username']
        status = f['status']
        last = f['last_activity']
        d['away' if status == 'online' and last > 10 else status].append(name)
    return d