class Solution:
    
    def reverse(self,arr) :
        N  = len(arr)
        a = []
        for i in range(N-1,-1,-1) :
            a.append(arr[i])
        return a
    
    def maxArea(self, arr,d = 0) :
        N = len(arr)
        area = []
        rev_area = []
        rev = arr.copy()
        rev.reverse()
        for i in range(N) :
            sub = []
            offset = 0
            offset_r = 0
            flag = 0
            for j in range(N-1,i,-1) :
                if flag == 2 :
                	break
                res = arr[j] - arr[i]
                res_r = rev[j] - rev[i]
                if res >= 0 and offset == 0 :
                	offset = j - i
                	flag += 1
                if res_r >= 0 and offset_r == 0 :
                	offset_r = j - i
                	flag += 1
            rev_area.append(rev[i]*offset_r)
            area.append(arr[i]*offset)
        return max(max(rev_area),max(area))

        
A = [1,8,6,2,5,4,8,3,7]
#[7,3,8,4,5,2,6,8,1]
sol = Solution()
print(sol.maxArea(A))
print(sol.maxArea([1,2]))