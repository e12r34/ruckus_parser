from pygrok import Grok
import socket
text = 'Aug 14 07:32:06 Kominfo-Pusat Core: @@347,apHealthAirtimeUtilizationFlag,"apMac"="58:FB:96:19:2B:80","apName"="AP GU2 Depan Ruang Ukir","currentValue"="77","configuredThreshold"="50","radio"="5GHz","fwVersion"="6.1.0.0.9240","model"="R850","zoneUUID"="a62be396-3911-49a6-9dbb-9a5bba36953d","zoneName"="Gedung Utama","timeZone"="WIB-7","apLocation"="Ged. Utama","apGps"="","apIpAddress"="10.101.12.18","apIpv6Address"="","apGroupUUID"="3ef60251-bb2d-4f69-9af1-8cb8e76e576e","domainId"="8b2081d5-9662-40d9-a3db-2a3cf4dde3f7","serialNumber"="922102001100","domainName"="Administration Domain","idealEventVersion"="3.5.1","apDescription"=""'
pattern = '%{SYSLOGTIMESTAMP:timestamp} %{HOSTNAME:host} %{DATA:source}: @@%{NUMBER:event_code},%{DATA:event_name},%{GREEDYDATA:message}'
grok = Grok(pattern)
hasil=grok.match(text)
data={'agent.name':socket.gethostname()}
for i in hasil:
    data[i]=hasil[i]
# data['event_code']=data['event_code']
coba=hasil['message']
sub=coba.replace('"','')
cobakoma=sub.split(',')
for j in cobakoma:
    hasil=j.split('=')
    data[hasil[0]]=hasil[1]
print(data)