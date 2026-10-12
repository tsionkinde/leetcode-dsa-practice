class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(nums1)):
            found=False
            for j in range(len(nums2)):
                if nums1[i][0]== nums2[j][0]:
                    ans.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                    found=True
                    break
            if not found:
                ans.append(nums1[i])
        for j in range(len(nums2)):
            found=False
            for i in range(len(nums1)):
                if nums1[i][0]== nums2[j][0]:
                    found=True
                    break
            if not found:
                ans.append(nums2[j])
        ans.sort()
        return ans            





            
                
           
                 
        