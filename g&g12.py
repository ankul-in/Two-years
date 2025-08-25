#https://www.geeksforgeeks.org/problems/better-string/1?page=1&category=Recursion&difficulty=Hard&sortBy=submissions
# from itertools import combinations

# arr=[]
# answer=[]
# setAns=set()
# for i in arr:
#     x=list(arr)
#     for y in range(len(i)):
    
#         comb=combinations(x,y)
#         for j in comb:
#             answer.append("".join(j))
        
#         setAns=set(answer)
#         count=len(setAns)
        
# from itertools import combinations

# def count_unique_combinations(arr):
#     unique = set()
#     for r in range(1, len(arr) + 1):
#         for comb in combinations(arr, r):
#             unique.add("".join(comb))
#     return len(unique)

# def find_max_combination_arr(arr_list):
#     max_count = -1
#     best_arr = None

#     for arr in arr_list:
#         count = count_unique_combinations(arr)
#         print(f"Combinations from {arr}: {count}")
#         if count > max_count:
#             max_count = count
#             best_arr = arr

#     return best_arr, max_count


# arr_list = [
#     ['a', 'b', 'c'],
#     ['ab', 'bc', 'ca'],
#     ['x', 'y'],
#     ['abc', 'def', 'ghi']
# ]

# best_arr, count = find_max_combination_arr(arr_list)
# print(f"\nBest arr: {best_arr} with {count} unique combinations")

            
def count_distinct_subsequences(s):
    MOD = 10**9 + 7
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty subsequence

    last_occurrence = {}

    for i in range(1, n + 1):
        dp[i] = (2 * dp[i - 1]) % MOD
        ch = s[i - 1]
        if ch in last_occurrence:
            dp[i] = (dp[i] - dp[last_occurrence[ch] - 1]) % MOD
        last_occurrence[ch] = i

    return dp[n]

def compare_subsequences(s1, s2):
    count1 = count_distinct_subsequences(s1)
    count2 = count_distinct_subsequences(s2)

    return s1 if count1 >= count2 else s2

s1 = "aahjbfjhnac"
s2 = "aablifeahn wiefu bragl a"
print(compare_subsequences(s1, s2))  

#i couldnt make sense of this fr
