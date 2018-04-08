import os

def delFiles(path,suffix):
		length = 0
		paths = []
		for root,dirs,files in os.walk(path):
			for name in files:
				if(name.endswith(suffix)):
					length+=1
					paths.append(os.path.join(root,name))
		return length,paths

targetPath = input("请输入目标文件夹全路径：")
if (not os.path.exists(targetPath)):
	targetPath = input("请输入合法的目标文件夹全路径：")
targetSuffix = input("请输入待删除文件后缀：")
state = input("%s%s%s%s%s" % ("是否确认删除文件夹",targetPath,"下所有后缀为",targetSuffix,"的文件？\n注意，此操作不可逆！\n[输入Y继续,其余任意字符取消]\n"))
if state == "Y":
	length,paths = delFiles(targetPath,targetSuffix)
	for path in paths:
		os.remove(path)
		print(path)		
	print("\nDelete Files:" + str(length) + "\n")
else:
	print("操作已取消")
