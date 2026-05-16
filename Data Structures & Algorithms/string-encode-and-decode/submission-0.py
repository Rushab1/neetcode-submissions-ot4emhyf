class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        ret = []
        for s in strs:
            ret += [f"{len(s)}"]

        return ",".join(ret) + "$" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        counts = s.split("$",1)
        s = counts[1]
        counts = counts[0].split(",")
        ret = []
        i = 0
        for n in counts:
            n = int(n)
            ret += [s[i:i + n]]
            i += n
        return ret

