# 简易文件服务器
> 使用python django
总共三个映射,默认80端口<br>
/postfile/ 上传接口<br>
/upload/ 上传页面接口<br>
/public/ 上传文件列表接口<br>
/还有个主页访问获取当前网卡ip<br>
会在运行目录生成server.log日志

## 安装
```shell
[编译版本]setup.py install
[测试版本]pip install -i https://test.pypi.org/simple/ Filetransfer
[发行版本]pip install Filetransfer
```

## 运行
``` python
python -m filetransfer.cli #默认运行
python -m filetransfer.cli -h #帮助
```

## windows使用
```
[上传]浏览器打开http://localhost/upload/
[浏览和下载]浏览器打开http://localhost/public/
其他机器访问localhost换成当前网卡的ip
```
## linux 使用
``` bash
[上传]curl http://localhost/postfile/ -F "file=@/path" 
[上传]curl localhost/postfile/ -F "file=@/root/demo"
[上传多个]curl localhost/postfile/ -F "file=@filename1" -F "file=@filename2"
[浏览] curl http://localhost/public/
[下载] wget http://localhost/public/filename
```
>path是绝对路径，也可以用当前路径
filename填你要下载的文件名
有一种no files for upload!叫做文件正在写入