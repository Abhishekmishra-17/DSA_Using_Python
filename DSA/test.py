class Solution:
    def findLength(self, color, radius):
        stack = []
        for item in zip(color, radius):
            print(item)
        for c, r in zip(color, radius):
            # breakpoint()
            if stack and stack[-1] == (c, r):
                stack.pop()
            else:
                stack.append((c, r))
            print(stack)
        return len(stack)
    
if __name__ == "__main__":
    color = [1, 2, 3, 4, 4, 6, 7, 8]
    radius = [1, 2, 3, 4, 4, 6, 7, 8]
    sol = Solution()
    print(sol.findLength(color, radius))  # Output: 0