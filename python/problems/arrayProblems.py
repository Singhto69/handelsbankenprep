import math
import numpy
import re
from helpfunctions.helpfunctions import *
from collections import defaultdict


class ArrayProblems():
    def __init__(self):
        self.dummy = 0

    def arrayProblem001(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()

    def arrayProblem002(self):
        nums = [3, 2, 2, 3]
        val = 3
        i = 0
        while i != len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue
            i = i + 1
        k = (len(nums) + 1)

    def arrayProblem003(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        i = 0
        e = len(nums) - 1
        """
        while i != e:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
                e = e - 1
                continue
            i = i + 1
        k = len(nums) + 1
        """
        # partition1 = nums[:int(len(nums)/2)]
        # partition2 = nums[int(len(nums)/2):]
        x = set(nums)
        nums = sorted(x)
        k = len(nums)

    def arrayProblem004(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        myDict = {}
        for i in nums:
            myDict[i] = myDict.get(i, 0) + 1
        k = max(zip(myDict.keys(), myDict.values()))[0]
        # print(k)

    def arrayProblem005(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
        i = 0
        k = len(nums)
        while i < k - 2:
            if nums[i] == nums[i + 1] & nums[i] == nums[i + 2]:
                nums.pop(i)
                k = k - 1
                continue
            i = i + 1

    def arrayProblem006(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        #    temp = nums[-k:]
        #    nums = nums[:-k]
        #    nums = temp + nums
        nums = nums[-k:] + nums[:-k]

    def arrayProblem007(self):
        prices = [7, 1, 5, 3, 6, 4]
        maxProfit = 0
        lowestStockPrice = float('inf')
        i = 0
        e = len(prices)
        while i != len(prices):
            if lowestStockPrice > prices[i]:
                lowestStockPrice = prices[i]
                i = i + 1
                continue
            currentMaxProfit = prices[i] - lowestStockPrice
            if currentMaxProfit > maxProfit:
                maxProfit = currentMaxProfit
            i = i + 1

    """
    Naive solution , what happens if the array is [5,9,13,2,1,4]?
    How does the solution handle holding stocks? It does not take into account a net loss
    """

    def arrayProblem008(self):
        # prices = [7, 1, 5, 3, 6, 4]
        prices = [5, 9, 13, 3, 2, 9]
        totalProfit = 0
        totalLoss = 0
        lowestStockPrice = float('inf')
        i = 0
        while i != len(prices):
            if prices[i] > lowestStockPrice:
                totalProfit += prices[i] - lowestStockPrice
            if lowestStockPrice > prices[i]:
                totalLoss = totalLoss + (lowestStockPrice - prices[i])
            lowestStockPrice = prices[i]
            i += 1
        print(totalProfit)
        print(totalLoss)

    def arrayProblem009(self):
        nums = [1, 1, 2, 2, 0, 1, 1]
        if len(nums) < 1:
            return False
        accumulatedJumps = nums[0]
        for i in range(0, len(nums) - 1):
            evaluatedJumps = nums[i]
            # We only grab extra jumps if we are running out. Evaluating in place from the new max position eliminates,
            # the need to check forwards in time.
            if accumulatedJumps < evaluatedJumps:
                accumulatedJumps = evaluatedJumps
            if accumulatedJumps == 0:
                return False
            i = i + 1
            accumulatedJumps = accumulatedJumps - 1
        return True

    def arrayProblem010(self):
        nums = [4, 1, 1, 3, 1, 1, 1]
        """
        BFS greedy , imagine a spaceship sending probes into unknown space to probe next fuel stop, fuel being
        harvestable dark matter.
        """
        x = 0
        spaceFuel = nums[x]
        if len(nums) < 2:
            return 0
        refills = 1
        while True:
            if x + spaceFuel >= len(nums) - 1:
                return refills
            probeXCoordinate = x + 1
            probeEndCoordinate = x + spaceFuel
            localMax = (0, 0, 0)
            while probeXCoordinate <= probeEndCoordinate:
                potentialFuel = nums[probeXCoordinate]
                potentialFuelTravelDistance = probeXCoordinate + potentialFuel
                if potentialFuelTravelDistance >= localMax[2]:
                    localMax = (probeXCoordinate, potentialFuel, potentialFuelTravelDistance)
                probeXCoordinate += 1
            x = localMax[0]
            spaceFuel = localMax[1]
            refills += 1

    def arrayProblem011(self):
        citations = [3, 0, 6, 1, 5]
        citations = sorted(citations, reverse=True)
        mid = int(len(citations) / 2)
        hindex = 0
        for i in range(0, mid + 1):
            hindex = max(min(i + 1, citations[i]), hindex)
        return hindex

    # if len(citations) == 1:
    #    return min(citations[0], 1)
    """
    condA = citations[i] >= hIndex
    condB = i <= citations[i]
    if condA & condB:
        hIndex = citations[i]
    if condB & (condA == False):

    # else hindex = min(citaions i , i )
    i = i - 1
    """

    def arrayProblem012(self):
        nums = [2, 3, 4, 5, 6]
        answer = [1] * len(nums)
        product = 1
        for i in range(0, len(nums) - 1):
            product = product * nums[i]
            answer[i + 1] = product
        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product = product * nums[i]
            answer[i - 1] = answer[i - 1] * product
        return answer

    """
    Why is this solution top 90% when it has an extra for loop and also 3 extra arrays instead of 1?
    """

    def arrayProblem012netsolution(self):
        nums = [2, 3, 4, 5, 6]
        l = len(nums)
        prefix_product = [1] * l
        suffix_product = [1] * l

        # Calculating prefix products
        for i in range(1, l):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

        # Calculating suffix products
        for i in range(l - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

        # Combining prefix and suffix products
        result = []
        for i in range(l):
            result.append(prefix_product[i] * suffix_product[i])

        return result

    def arrayProblem013(self):
        gas = [1, 1, 3]
        cost = [2, 2, 1]
        for i in range(0, len(gas)):
            cost[i] = gas[i] - cost[i]
        if sum(cost) >= 0:
            return kadanesmaxintpositionformaxsubarray(cost)
        else:
            return -1

    def arrayProblem013optimized(self):
        gas = [1, 1, 3]
        cost = [2, 2, 1]
        maxsubarraystart = 0
        maxsubarraysum = 0
        totalsum = 0
        for i in range(0, len(gas)):
            val = gas[i] - cost[i]
            maxsubarraysum += val
            totalsum += val
            if val >= maxsubarraysum:
                maxsubarraystart = i
                maxsubarraysum = val
        if totalsum >= 0:
            return maxsubarraystart
        else:
            return -1

    def arrayProblem014(self):
        ratings = [3, 2, 1, 2, 3]
        l = len(ratings)
        candies = [1] * l
        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)

    def arrayProblem015(self):
        s = "IV"
        translator = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        i = len(s) - 1
        while i > 0:
            if translator[s[i]] > translator[s[i - 1]]:
                sum += translator[s[i]] - translator[s[i - 1]]
                i = i - 2
                continue
            sum += translator[s[i]]
            i -= 1
        if i == 0:
            sum += translator[s[i]]
        return sum

    def arrayProblem016(self):
        s = 1958
        translator = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        tens = s // 10
        remainder = s % 10
        s = ""
        while tens != 0:
            if tens >= 100:
                s += "M"
                tens = tens - 100
                continue
            if tens >= 50:
                s += "D"
                tens = tens - 50
                continue
            if tens >= 10:
                s += "C"
                tens = tens - 10
                continue
            if tens >= 5:
                s += "L"
                tens = tens - 5
                continue
            if tens >= 1:
                s += "X"
                tens = tens - 1
                continue
        return s

    def arrayproblem017(self):
        s = "Hello    World "
        """
        if len(s) == 0:
            return 0
        s = s.split(" ")
        for i in range(len(s) - 1, -1, -1):
            if len(s[i]) == 0:
                continue
            return len(s[i])
        """
        return len(s.strip().split()[-1])

    def arrayproblem018(self):
        strs = ["flower", "flow", "flight"]
        strs = sorted(strs, key=len)
        prefix = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:
                if s[i] != c:
                    return prefix
            prefix += c
        return prefix

    def arrayproblem019(self):
        # Compute max height
        # compare from black blocks?
        return

    def interviewproblem151(self):
        s = "a good   example for you"
        s = s.strip().split()
        lp = 0
        rp = len(s) - 1
        while lp <= rp:
            s[lp], s[rp] = s[rp], s[lp]
            lp += 1
            rp -= 1
        return ' '.join(s)

    def interviewproblem028(self):
        haystack = "hello"
        needle = "ll"
        o = ""
        for i in range(0, len(haystack)):
            o += haystack[i]
            if len(o) > len(needle):
                o = o[1:]
            if needle == o:
                return i - (len(needle) - 1)
        return -1

    def interviewproblem125(self):
        s = "A man, a plan, a canal: Panama"
        s = re.sub(r'[^a-zA-Z0-9]', '', s).strip().lower()
        lp = 0
        rp = len(s) - 1
        while lp <= rp:
            if s[lp] != s[rp]:
                return False
            lp += 1
            rp -= 1
        return True

    def interviewproblem392(self):
        s = "abc"
        t = "ahbgde"
        if len(s) == 0:
            return False
        target = 0
        for c in t:
            if c == s[target]:
                target += 1
            if target == len(s):
                return True
        return False

    def interviewproblem167(self):
        numbers = [2, 4, 7, 8, 9, 14]
        target = 12
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l, r]
            if sum > target:
                r -= 1
                continue
            if sum < target:
                l += 1
                continue

    def interviewproblem11(self):
        height = [2, 3, 4, 5, 18, 17, 6]
        l = 0
        r = len(height) - 1
        biggestarea = 0
        while l < r:
            area = (min(height[l], height[r]) * (r - l))
            biggestarea = max(biggestarea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return biggestarea
