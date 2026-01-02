# 20201022 - Wash Your Hands
def wash_hands(N, nM):
    return str(N * nM * 30 * 21//60) + " minutes and " + str((N * nM * 30 * 21) - (N * nM * 30 * 21//60) * 60) + " seconds"

print(wash_hands(8, 7))
print(wash_hands(7, 9))