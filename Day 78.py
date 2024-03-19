class Solution:
    def isValid(self, A, B, max_pages):
        students = 1
        pages_allocated = 0
        for pages in A:
            pages_allocated += pages
            if pages_allocated > max_pages:
                students += 1
                pages_allocated = pages
            if students > B:
                return False
        return True
    
    def books(self, A, B):
        if len(A) < B:
            return -1
        
        total_pages = sum(A)
        min_pages = max(A)
        max_pages = total_pages
        
        result = -1
        while min_pages <= max_pages:
            mid_pages = (min_pages + max_pages) // 2
            if self.isValid(A, B, mid_pages):
                result = mid_pages
                max_pages = mid_pages - 1
            else:
                min_pages = mid_pages + 1
        
        return result
