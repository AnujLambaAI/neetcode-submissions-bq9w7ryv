class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))

        for sz in sizes:
            res+= str(sz)
            res += ","
        res += "#"

        for s in strs:
            res+= s
        return res
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizses, res, i = [], [], 0
        while s[i] != "#":
            curInt = ""
            while s[i] != ",":
                curInt += s[i]
                i += 1
            sizses.append(int(curInt))
            i += 1
        i += 1

        for sz in sizses:
            res.append(s[i : i + sz])
            i += sz
        return res



