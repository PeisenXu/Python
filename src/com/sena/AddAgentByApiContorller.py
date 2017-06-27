from urllib import request
import re
import urllib

url = "http://www.xicidaili.com/nt/"

header = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2595.400 QQBrowser/9.6.10872.400',
   'Connection':'keep-alive',
   'Access-Control-Allow-Methods':'POST, PUT, GET, OPTIONS, DELETE',
   'Access-Control-Allow-Origin':'*',
   'Access-Control-Allow-Headers':'Origin, X-Requested-With, Content-Type, Accept,Authorization,X-Center-Id,X-UID'
}
req = request.Request(url,headers = header)
r= request.urlopen(req)
strs = r.read().decode('UTF-8')

k = re.split(r'\s+',strs)

j = 0
ip = ''
port = ''
type = ''
survivalTime = ''
errorCount = 0
for i in k :
    if (re.match(r'<td>',i)):
        if re.search(r'</td>',i):
            m = re.search(r'<td>(.*?)</td>.*',i)
            j = j + 1
            if j == 1 :
                ip = m.group(1)
            elif j == 2 :
                port = m.group(1)
            elif j == 3 :
                type = m.group(1)
            else :
                survivalTime = m.group(1)
                
            if j == 4 :
                print(ip + port + type + survivalTime)
                addurl = "http://120.76.113.231/api/v1/agent/agent.sena"
                date = {
                   'ip' : ip,
                   'port' : port,
                   'type' : type,
                   'survivalTime' : survivalTime
                }
                tmp_pdata=urllib.parse.urlencode(date)
                req = request.Request(url = addurl,data = tmp_pdata.encode(encoding="utf-8", errors="ignore"), headers=header,method='POST')
                try:  
                    r= request.urlopen(req)  
                except Exception as err:  
                    print(err)
                finally:
                    ip = ''
                    port = ''
                    type = ''
                    survivalTime = ''
                    j = 0

print("End.  Success!  ErrorCount:" + errorCount)
            