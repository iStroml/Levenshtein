# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def alignment(word1, word2):
    editDist = [[sys.maxsize for _ in word2 + ' '] for _ in word1 + ' ']
    bestPrev = [[None for _ in word2 + ' '] for _ in word1 + ' ']

    def update_edit_distance(d, i, k, pair):
        if editDist[i][k] > d:
            editDist[i][k] = d
            bestPrev[i][k] = pair

    # Handling deletion, insertion, match and replacement
    editDist[0][0] = 0
    for i in range(len(word1) + 1):
        for k in range(len(word2) + 1):
            if i > 0:
                # deletion
                d = editDist[i - 1][k] + 1
                update_edit_distance(d, i, k, (i - 1, k))
            if k > 0:
                # insertion
                d = editDist[i][k - 1] + 1
                update_edit_distance(d, i, k, (i, k - 1))
                if i > 0:
                    if word1[i - 1] == word2[k - 1]:
                        # match
                        d = editDist[i - 1][k - 1]
                    else:
                        # replacement
                        d = editDist[i - 1][k - 1] + 1
                    update_edit_distance(d, i, k, (i - 1, k - 1))

    def print_pairs(i, k):
        # printing the alignments
        if bestPrev[i][k]:
            new_i, new_k = bestPrev[i][k]
            print_pairs(new_i, new_k)

            if new_i < i:
                if new_k < k:  # replacement of match
                    print(word1[i - 1] + ':' + word2[k - 1], end=' ')
                else:
                    print(word1[i - 1] + ':', end=' ')
            else:
                print(':' + word2[k - 1], end=' ')

    print_pairs(len(word1), len(word2))

    return editDist[-1][-1]


for line in ["DistanceOne DistanceOnn",
             "DistanceTwo DistanceTou",
             "DistanceThree DistanceTh",
             "DistanceFour DistanceBla"]:
    w1, w2 = line.split()
    print(alignment(w1, w2))

# Result
# D:D i:i s:s t:t a:a n:n c:c e:e O:O n:n e:n 1
# D:D i:i s:s t:t a:a n:n c:c e:e T:T w: o:o :u 2
# D:D i:i s:s t:t a:a n:n c:c e:e T:T h:h r: e: e: 3
# D:D i:i s:s t:t a:a n:n c:c e:e F:B o:l u:a r: 4
