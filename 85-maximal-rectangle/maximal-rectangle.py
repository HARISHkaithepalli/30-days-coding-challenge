class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        c=len(matrix[0])
        h=[0]*c
        m_a=0
        for r in matrix:
            for i in range(c):
                if r[i]=='1':
                    h[i]+=1
                else:
                    h[i]=0 
            s=[]
            for i in range(c+1):
                c_h=h[i] if i<c else 0
                while s and c_h<h[s[-1]]:
                    h1=h[s.pop()]
                    w=i if not s else i-s[-1]-1
                    m_a=max(m_a,h1*w)
                s.append(i)
        return m_a 

        