# 简易文件服务器
> 使用python django
总共三个映射,默认80端口
/postfile/ 上传接口
/upload/ 上传页面接口
/public/ 上传文件列表接口
还有个主页访问获取当前网卡ip

## 运行
``` python
pip install django
python manage.py runserver 0.0.0.0:80
```

## windows使用
[上传]浏览器打开http://localhost/upload/
[浏览和下载]浏览器打开http://localhost/public/
其他机器访问localhost换成当前网卡的ip

## linux 使用
``` bash
[上传]curl http://localhost/postfile/ -F "file=@/path" 
[浏览] curl http://localhost/public/
[下载] wget http://localhost/public/filename
```
>path是绝对路径
filename填你要下载的文件名