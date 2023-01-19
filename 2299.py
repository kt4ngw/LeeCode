class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        lowerCase = False
        upperCase = False
        oneNumber = False
        oneSpecical = False
        conTwo = True
        l = list('!@#$%^&*()-+')
        for i in range(len(password)):
            if (i < len(password) - 1):
                if password[i + 1] == password[i]:
                    conTwo = False
                    break
            if password[i] <= 'z' and password[i] >= 'a':
                lowerCase = True
            if password[i] <= 'Z' and password[i] >= 'A':
                upperCase = True
            if password[i] <= '9' and password[i] >= '0':
                oneNumber = True
            if password[i] in l:
                oneSpecical = True

        return lowerCase and upperCase and oneNumber and oneSpecical and conTwo



