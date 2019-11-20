from django.http import HttpResponse
from django.conf import settings
import os,socket

# Create your views here.
def postfile(request):
 if request.method == "POST":    # 请求方法为POST时，进行处理  
        myFile =request.FILES.get("file", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not myFile:  
            returnHttpResponse("no files for upload!")  
        destination = open(os.path.join(settings.MEDIA_ROOT,myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作  
        for chunk in myFile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()  
        return HttpResponse("upload over!")
 
def upload(request):
 return HttpResponse("""<form enctype="multipart/form-data" action="/postfile/" method="post">  
   <input type="file" name="file" />  
   <br/>  
   <input type="submit" value="upload"/>  
</form> """)

def index(request):
  ip=get_host_ip()
  return HttpResponse("welcome! <a href=\"http://"+ip+"\">"+ip+"</a>")
 

def get_host_ip():
    '''获取本机ip'''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        return ip
    finally:
        s.close()