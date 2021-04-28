class LevenshteinDistance:

    def getDistance(self, stringA, stringB):
        if (len(stringB) == 0):
            return len(stringA)
        elif (len(stringA) == 0):
            return len(stringB)
        elif (stringA[0] == stringB[0]):
            return self.getDistance(stringA[1:], stringB[1:])
        else:
            return (
                1 + min(
                    self.getDistance(
                        stringA[1:],
                        stringB),
                    self.getDistance(
                        stringA,
                        stringB[1:]),
                    self.getDistance(
                        stringA[1:],
                        stringB[1:])))


# A = "kucing"
# B = "kacang"

# lev = LevenshteinDistance()
# print(lev.getDistance(A, B))
