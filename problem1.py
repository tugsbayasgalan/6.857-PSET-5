#Urn voting

import random

urn_box = [61, 51, 31]
max_limit = 10003
winning_dist = {0: 0, 1: 0, 2: 0}

def get_type(sample, box):

    index = 0
    remain = sample

    while index < len(box) - 1 and remain >= box[index]:
        remain -= box[index]
        index += 1

    return index


def get_max(box):

    best_cand = 0
    best_val = box[0]

    for index, val in enumerate(box):
        if val > best_val:
            best_val = val
            best_cand = index

    return best_cand

for i in range(100000):

    if i % 5000 == 0:
        print ("Finished {} trials so far".format(i))

    while sum(urn_box) <= max_limit:

        rand_sample = random.randint(0, sum(urn_box))

        type = get_type(rand_sample, urn_box)

        urn_box[type] += 1

    for i in range(len(urn_box)):
        urn_box[i] -= 1

    winner = get_max(urn_box)
    winning_dist[winner] += 1
    urn_box = [61, 51, 31]


total = sum([winning_dist[k] for k in winning_dist])
first_cand_win = winning_dist[0]
print (winning_dist)
print ("First Candidate wins with a prob {}".format(first_cand_win/total))
