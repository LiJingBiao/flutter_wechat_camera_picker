import os
import re

# 获取当前目录的路径
current_dir = os.getcwd()

# 定义一个正则表达式，用于匹配单引号或双引号包围的字符串
regex = re.compile(r"'([^']*)'|\"([^\"]*)\"")

# 创建一个新的文件，用于存储检索到的字符串
output_file = open(os.path.join(current_dir, 'output.txt'), 'w')

# 使用os.walk函数遍历当前目录及其所有子目录
for root, dirs, files in os.walk(current_dir):
  # 遍历每个子目录中的文件
  for file in files:
    # 判断文件名是否以.dart结尾
    if file.endswith('.dart'):
      # 拼接文件的完整路径
      file_path = os.path.join(root, file)
      # 打开文件并读取内容
      with open(file_path, 'r') as f:
        content = f.read()
        # 使用正则表达式在内容中查找所有字符串
        matches = regex.findall(content)
        # 遍历每个匹配结果，打印出文件名和字符串内容，并写入到输出文件中
        for match in matches:
          # 获取第一个捕获组或第二个捕获组，根据单引号或双引号
          string = match[0] or match[1]
          # 判断字符串是否包含中文字符，如果是则写入到输出文件中
          if re.search(r'[\u4e00-\u9fff]', string):
            # 打印文件名和字符串内容
            print(f'{file}: {string}')
            # 写入到输出文件中，每个字符串占一行
            output_file.write(f'{string}\n')

# 关闭输出文件
output_file.close()
