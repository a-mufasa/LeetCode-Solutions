class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_map = dict()
        ts_map = dict()

        for i in range(len(s)):
            if (s[i] in st_map and st_map[s[i]] != t[i]):
                return False
            if (t[i] in ts_map and ts_map[t[i]] != s[i]):
                return False
            
            st_map[s[i]] = t[i]
            ts_map[t[i]] = s[i]

        return True
        