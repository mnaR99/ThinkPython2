
# ---- 11.2

def invert_dict(d):
    invd = dict()
    for key in d:
        val = d[key]
        invd.setdefault(val, list()).append(key)
    return invd


print(invert_dict({'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}))
