class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        result = 0
        # 直接模拟
        for i in range(len(brackets)):
            if i == 0:
                if income > brackets[i][0]:
                    result += (brackets[i][0]) * brackets[i][1] / 100
                else:
                    result += income * brackets[i][1] / 100
                continue
            else:
                if income > brackets[i - 1][0]:
                    if income > brackets[i][0]:
                         result += (brackets[i][0] - brackets[i - 1][0]) * brackets[i][1] / 100
                    else:
                        result += (income - brackets[i - 1][0]) * brackets[i][1] / 100
                        break
        return result