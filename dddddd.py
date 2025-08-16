
# test.py

# 示例子主题字符串，格式为"编号.内容"
sub_idea = "3.人工智能的应用前景"

# 去除编号，只保留内容部分
sub_idea_new = ".".join(sub_idea.split(".")[1:])
# sub_idea_new = sub_idea.split(".")[1:]

print("原始子主题：", sub_idea)
print("去除编号后的子主题：", sub_idea_new)
