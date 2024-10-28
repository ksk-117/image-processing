import os

# ファイルを作成するディレクトリのパスを指定
directory = "ensyu3"  

# ディレクトリが存在しない場合は作成
if not os.path.exists(directory):
    os.makedirs(directory)

# ファイル名の範囲を指定
for i in range(1, 6):  # 1 ~ n-1 までのファイルを作成
    filename = os.path.join(directory, f"{i:02}.py")
    with open(filename, 'w') as file:
        pass

print("ファイルが作成されました。")