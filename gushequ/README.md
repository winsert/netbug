# gushequ 用于爬取www.gushequ.com上的内容

gsq.py      实现从所有页面中解析出title和href

gushequ_dict.py     gushequ_dict.txt
将爬取的title和href以字典的形式保存到gushequ_dict.txt

gushequ_json.py     gushequ_dict.json
将爬取的title和href以字典的形式保存到gushequ_dict.json

gushequ_json_module.py  gushequ.json
程序模块化：将爬取的title和href以字典的形式保存到gushequ.json

gushequ_add.py
用于向gushequ.json中增加新记录

request.py  对指定url进行解析,结果保存到soup.txt

soup.txt    用于保存解析结果

soup.py     对soup.txt中的内容进行步步解析

json_loads.py       实现读取*.json文件
