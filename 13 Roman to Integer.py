class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {
            'I':    1,
            'V':    5,
            'X':    10,
            'L':    50,
            'C':    100,
            'D':    500,
            'M':    1000,
        }
        
        arr_rom = list(s)
        value = 0
        skip = False
        for idx,ele in enumerate(arr_rom):
            if skip == False:
                try:
                    if dict_roman[arr_rom[idx+1]] > dict_roman[ele]:
                        value = value + (dict_roman[arr_rom[idx+1]] - dict_roman[ele])
                        skip = True
                    else:
                        value = value + dict_roman[ele]
                except:
                    value = value + dict_roman[ele]
            else:
                skip = False
        
        return value


sol = Solution()

print(sol.romanToInt(s='MCMXCIV'))