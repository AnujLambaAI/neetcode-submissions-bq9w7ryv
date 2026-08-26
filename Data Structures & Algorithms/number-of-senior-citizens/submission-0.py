class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0 
        for d in details:
            phnNum = d[:10]
            gender = d[10:11]
            age = int(d[11:13])
            seat = d[13:]

            if age > 60:
                res += 1
        return res
    