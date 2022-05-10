from difflib import SequenceMatcher
import jellyfish
import numpy as np

def lcs(a, b):
    prev = [0]*len(a)
    for i,r in enumerate(a):
        current = []
        for j,c in enumerate(b):
            if r==c:
                e = prev[j-1]+1 if i* j > 0 else 1
            else:
                e = max(prev[j] if i > 0 else 0, current[-1] if j > 0 else 0)
            current.append(e)
        prev = current
    return current[-1]

#레반슈타인 알고리즘 ( 편집거리 알고리즘 )
def edit_distance(s: str, t: str):
    m = len(s) + 1
    n = len(t) + 1
    D = [[0] * m for _ in range(n)]
    D[0][0] = 0

    for i in range(1, m):
        D[0][i] = D[0][i - 1] + 1

    for j in range(1, n):
        D[j][0] = D[j - 1][0] + 1

    for i in range(1, n):
        for j in range(1, m):
            cost = 0

            if s[j - 1] != t[i - 1]:
                cost = 1

            D[i][j] = min(D[i][j - 1] + 1, D[i - 1][j] + 1, D[i - 1][j - 1] + cost)

    return D[n - 1][m - 1]

str1 = 'AM Facial Moisturizing Lotion SPF 30 | Oil-Free Face Moisturizer with Sunscreen'
str2 = 'AM Facial Moisturizing Lotion SPF 30 | Oil-Free Face Moisturizer with Sunscreen, 1 Pack of 3 Ounce'
str3 = 'AM Facial Moisturizing Lotion SPF 30 | Oil-Free Face Moisturizer with Sunscreen | Non-Comedogenic | 1 Pack of 3 Ounce'


# str1 = '"Mighty Patch Original from Hero Cosmetics - Hydrocolloid Acne Pimple Patch for Covering Zits and Blemishes, Spot Stickers for Face and Skin, Vegan-friendly and Not Tested on Animals (36 Count)"'
# str2 = '"Maybelline Instant Age Rewind Eraser Dark Circles Treatment Multi-Use Concealer,110 Fair, 0.2 Fl Oz (Pack of 1) - Packaging May Vary"'

a = str1
b = str3

print(SequenceMatcher(None, a, b).ratio())
print(jellyfish.jaro_distance(a, b))
print(edit_distance(a, b))
