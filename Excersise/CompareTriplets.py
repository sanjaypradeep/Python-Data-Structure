# Please check the question here - https://www.hackerrank.com/challenges/compare-the-triplets


aliceTriplets = input().split()
bobTriplets = input().split()
alice, bob = 0,0

for i in range(len(aliceTriplets)):
    if (int(aliceTriplets[int(i)]) > int(bobTriplets[int(i)])):
        print (aliceTriplets[i], bobTriplets[i])
        alice = alice + 1
    elif (int(aliceTriplets[int(i)]) < int(bobTriplets[int(i)])):
        bob  +=1
    else:
        print ("inside else")

print (alice, bob)

# 5 6 7
# 3 6 10