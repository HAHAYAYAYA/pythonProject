import os

root_dir = "dataset/train"
target_dir = 'bees_images'
img_path = os.listdir(os.path.join(root_dir, target_dir))
label = target_dir.split('_')[0]    #切片后的列表取第一个元素，即ants/bees
'''split() 方法通过指定分隔符对字符串进行切片，该方法将字符串分割成子字符串并返回一个由这些子字符串组成的列表。
str.split(str="", num=string.count(str))
如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。
参数:str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数，如果设置了这个参数，则最多分割成 maxsplit+1 个子字符串。默认为 -1, 即分隔所有。
返回值:返回分割后的字符串列表。'''
out_dir = 'bees_label'
for i in img_path:
    file_name = i.split('.jpg')[0]
    with open(os.path.join(root_dir, out_dir,"{}.txt".format(file_name)),'w') as f:
        f.write(label)  #写入ants/bees
