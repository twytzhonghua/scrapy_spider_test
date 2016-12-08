import opencc
cc = opencc.OpenCC('mix2s')     #mix2s - Mixed to Simplified Chinese

str = '啊大家快樂的監考老師發'
newstr = cc.convert(str)

print(newstr)