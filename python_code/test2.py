import re

# text = "式咖啡[]机-,.{}[]\()（）*&……%￥#@！!、，。`？?|；;~——_''￥【】《》<>abdfs1234"

# pattern = re.compile(r'[*{}^……=%￥#@！!、,，。`;；？?_【】《》<>()（）~|&]+')
# text = pattern.sub(' ', text)
# # pattern = re.compile('\[]')
# text = pattern.sub(' ', text)
# print(text)


text = '航空母'
result = re.search(r'[机歼艇舰枪炮弹]', text)

if result:
    print('有')
else:
    print('没有')