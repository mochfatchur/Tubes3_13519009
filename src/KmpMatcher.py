class KmpMatcher:
    def match(self, keyword, message):
        n = len(message)
        m = len(keyword)
        fail = self.computeFail(keyword)
        i = 0
        j = 0
        while (i < n):
            if (keyword[j] == message[i]):
                if (j == m - 1):
                    return True  # match

                i += 1
                j += 1
            elif (j > 0):
                j = fail[j - 1]
            else:
                i += 1

        return False  # no match

    def computeFail(self, keyword):
        fail = [-1 for i in range(len(keyword))]
        fail[0] = 0
        m = len(keyword)
        j = 0
        i = 1
        while (i < m):
            if (keyword[j] == keyword[i]):
                # j + 1 chars match
                fail[i] = j + 1
                i += 1
                j += 1
            elif (j > 0):
                # j follows matching prefix
                j = fail[j - 1]
            else:
                # no match
                fail[i] = 0
                i += 1

        return fail


# text = "ada tugas apa saja sejauh ini ?"

# kmp = KmpMatcher(text)
# print(kmp.match("sejauh ana", text))
