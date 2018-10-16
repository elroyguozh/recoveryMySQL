import os
import shutil

sourcefile_dir = "E:\\MyDoc\\"
targetfile_dir = "E:\\MyDoc\\WorkSpace\\"
# os.chdir(file_dir)                                     # 获取当前工作目录
# shutil.copyfile("old","new") 　　　　  # 复制文件，都只能是文件
shutil.copyfile(sourcefile_dir+"new.txt",targetfile_dir+"new.txt")        # copy test_org.txt 为 test_copy.txt 若存在，则覆盖
# shutil.copyfile("test_org.txt","test1.txt")            # 存在，覆盖

