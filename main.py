import socket
example='''Aug 14 07:32:06 Kominfo-Pusat Core: @@347,apHealthAirtimeUtilizationFlag,"apMac"="58:FB:96:19:2B:80","apName"="AP GU2 Depan Ruang Ukir","currentValue"="77","configuredThreshold"="50","radio"="5GHz","fwVersion"="6.1.0.0.9240","model"="R850","zoneUUID"="a62be396-3911-49a6-9dbb-9a5bba36953d","zoneName"="Gedung Utama","timeZone"="WIB-7","apLocation"="Ged. Utama","apGps"="","apIpAddress"="10.101.12.18","apIpv6Address"="","apGroupUUID"="3ef60251-bb2d-4f69-9af1-8cb8e76e576e","domainId"="8b2081d5-9662-40d9-a3db-2a3cf4dde3f7","serialNumber"="922102001100","domainName"="Administration Domain","idealEventVersion"="3.5.1","apDescription"=""'''

# print(example)
output=[]
output_file=open("output.json","w")
a=open("example.txt","r").readlines()
for lines in a:
    example=lines.replace("\n","")
    if example!="":
        terpisah1=example.split(" ")
        pemisah=0
        for i in range(len(terpisah1)):
            if terpisah1[i].count(":")==1:
                pemisah=i
                
        terpisah2=example.split(" ",pemisah)
        jam=terpisah2[0]+" "+terpisah2[1]+" "+terpisah2[2]
        # print(jam)
        terpisah3=terpisah2[pemisah].split(" ",1)[1]

        data={'agent.name':socket.gethostname()}
        terpisah4=terpisah3.split(",")
        if "@@3001" in terpisah4:
            data['status.code']=terpisah4[0].split("@@")[1]
            data['status']=terpisah4[1]
            data['message']=terpisah4[2]
        else:
            for i in terpisah4:
                sub=i.replace('"','').split("=")
                if len(sub)>1:
                    data[sub[0]]=str(sub[1])
                else:
                    if "@@" in i:
                        data['status.code']=i.split("@@")[1]
                    elif "ap" in i:
                        data['status']=i
        output.append(data)
    # break
        output_file.write(str(data).replace("'",'"')+"\n")
# print(output)