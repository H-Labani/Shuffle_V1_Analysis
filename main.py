from math import sqrt

n = 900 # The total number of items to be shuffled
r = 3 # The number of rounds

# The set of batch lengths that are going to be analised
l = [5, 10, 15, (int(sqrt(n))), 50, 90, 100, 150, 300, 600, 900]

# Get the probability of item
def get_prob(l, i):
    # If the batch size is less than the number of batches
    if l < n / l:
        return ((1 / l)  * ((1 / l)  ** (i + 1)))

    # If the batch size is equal or greater than the number of batches
    else:
        return ((1 / l) * ((1 / (n / l)) ** (i + 1)))


if __name__ == '__main__':

# Iterate the over the number of rounds
    for i in range(r):
        print(f'round{i+1}')

        # analyse the choosen batches sizes by finding the attacker winning the game
        for j in range(len(l)):
            print('{:<4}: {}'.format(l[j], get_prob(l[j], i)))

