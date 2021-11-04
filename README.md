# vis_page_builder
豆瓣250观影网页生成器

## 文件说明

- main.py 主要逻辑以及爬虫部分
- change_json.py 修改影片是否观看的记录
- gen.py 根据爬取的影片以及 vis.json 自动生成 html
- vis.json 影片是否看过的记录
- - 如需重新生成，请将其初始化为`{}`


## 如何使用

1. 安装相关依赖
```cmd
pip install -r requirements.txt
```

2. 开始运行
```cmd
python main.py
```

## 效果预览

<img src="https://img-blog.csdnimg.cn/037cbf7f1d674176be2786e88f8b5ccc.jpg">

<img src="https://img-blog.csdnimg.cn/ba7aa56323a14ca6a145733913b255cc.jpg">
