### 리드미 매니저 - 리드미 내용 자동 구성 ###

import os

readme_template = """
# **📂 Today I Learned**

- 미루지 말기 내일의 나를 믿지 말기
- 중요한 내용은 한 번 더 다듬어서 [블로그](https://devpanpan.tistory.com/)에 업로드하기
- Issue, Project 기능 적극 활용하기


---

"""

exclude = ['.git', 'readme-manager.py', 'README.md', 'imgs']  # README에서 제외할 디렉토리


def search_directory(root, directory, depth):
    print_directory(directory, depth)

    move = root + f"\{directory}"
    os.chdir(move)
    files = os.listdir()
    directories = []
    for file in files:
        if file in exclude:
            continue
        new_path = move + "\\" + file
        if os.path.isdir(new_path):
            directories.append(file)
        else:
            print_file(file, new_path)
    for dir in directories:
        search_directory(move, dir, depth+1)

def print_directory(directory, depth):
    global readme_template

    readme_template += '\n'
    readme_template += ('#' * depth) + ' ' + directory + '\n'
    readme_template += '\n'


def print_file(file, path):
    global root, readme_template

    backslash = '\\'
    ext = file.split('.')[-1]
    filename = file.replace('.'+ext, '')
    readme_template += '-' + ' ' + \
        f'[{filename.replace("_", " ")}]({path.replace(root, "").replace(backslash, "/")})' + '\n'



root = os.getcwd()
README = open(f'{root}\README.md', 'w', encoding='UTF-8')
directorys = os.listdir()
for d in directorys:
    if d in exclude:
        continue
    search_directory(root, d, 2)
README.write(readme_template)
README.close()
