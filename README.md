# 技术准备
* 安装python-markdown
    * [installation instruction](http://pythonhosted.org/Markdown/install.html)
    
# 修改文档
* 将本仓库下载到本地
`git clone git@github.com:tinyfox266/offer.tips.git` 

* 打开要编辑的文件，如index.md
* 做相应编辑，并保存
* 将md文件转化为html文件
    ./markdown2html.py index.md
    
    生成的index.html文件会被放在当前目录下
* 上传修改
``` 
    git add .
    git commit -m "modify index.md"
    git push
```

# Markdown简介
* [Markdown 语法说明](http://www.appinn.com/markdown/)
    * [a local copy](http://ssg.ustcsz.edu.cn/~zzp/tech/markdown/tutorial.html)
* [zybuluo](https://www.zybuluo.com/mdeditor)
