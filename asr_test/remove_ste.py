# 需要去除的字符列表
import re

chars_to_remove = ['\"', ',']
# 构建正则表达式
regex_pattern = '[' + ''.join(chars_to_remove) + ']'
# 使用正则表达式去除字符
clean_text = re.sub(regex_pattern, '', "\"on\" september 24 1759 arthur guinness signed a 9,000 year lease for the st james' gate brewery in dublin ireland")
print(f"清理后的文本: {clean_text}")
