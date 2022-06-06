
# ---- 9.9

def is_reversible(age1, age2):
    s1, s2 = str(age1), str(age2)

    pad = max(len(s1), len(s2))

    s1 = s1.zfill(pad)
    s2 = s2.zfill(pad)[::-1]

    return s1 == s2


def reversible_ages(dif):

    age_pairs = []

    for age in range(150):
        if is_reversible(age, age + dif):
            age_pairs += [[age, age + dif]]
    return age_pairs


for dif in range(100):
    ages = reversible_ages(dif)
    if len(ages) == 8:
        break

print(ages)
