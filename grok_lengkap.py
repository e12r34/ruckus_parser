from pygrok import Grok
import socket

a=open("example.txt","r").readlines()
pattern = '%{SYSLOGTIMESTAMP:timestamp} %{HOSTNAME:host} %{DATA:source}: @@%{NUMBER:event_code},%{DATA:event_name},%{GREEDYDATA:message}'
grok = Grok(pattern)
for lines in a:
    example=lines.replace("\n","")
    if example!="":
        hasil=grok.match(example)
        data={'agent.name':socket.gethostname()}
        for i in hasil:
            data[i]=hasil[i]
        if data['event_code']!='3001':
            coba=hasil['message']
            sub=coba.replace('"','')
            cobakoma=sub.split(',')
            for j in cobakoma:
                hasil=j.split('=')
                data[hasil[0]]=hasil[1]
            del data['message']
        keluaran=open("keluaran.json","a")
        keluaran.write(str(data).replace("'",'"')+"\n")
        keluaran.close()