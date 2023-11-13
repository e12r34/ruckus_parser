from elasticsearch import Elasticsearch
import json, pytz
from datetime import datetime
print("initialization")
username="admin"
passw="admin123"
print("Connecting to Elasticsearch")
es = Elasticsearch("https://10.12.9.80:9200", basic_auth=(username, passw), verify_certs=False)
index_format_date=datetime.now().strftime("%Y.%m.%d")

output={"agent.name": "Lenovo-03", "timestamp": "Aug 14 07:32:06", "host": "Kominfo-Pusat", "source": "Core", "event_code": "347", "event_name": "apHealthAirtimeUtilizationFlag", "apMac": "58:FB:96:19:2B:80", "apName": "AP GU2 Depan Ruang Ukir", "currentValue": "77", "configuredThreshold": "50", "radio": "5GHz", "fwVersion": "6.1.0.0.9240", "model": "R850", "zoneUUID": "a62be396-3911-49a6-9dbb-9a5bba36953d", "zoneName": "Gedung Utama", "timeZone": "WIB-7", "apLocation": "Ged. Utama", "apGps": "", "apIpAddress": "10.101.12.18", "apIpv6Address": "", "apGroupUUID": "3ef60251-bb2d-4f69-9af1-8cb8e76e576e", "domainId": "8b2081d5-9662-40d9-a3db-2a3cf4dde3f7", "serialNumber": "922102001100", "domainName": "Administration Domain", "idealEventVersion": "3.5.1", "apDescription": ""}
index_name=f"custom-ruckus-data-{index_format_date}"
print("Ingesting data")
baca=open("keluaran.json","r").readlines()
for i in baca:
    print(i)
    sub=i.replace("\n","")
    data=json.loads(sub)
        # Parse the existing timestamp string
    timestamp = datetime.strptime(data["timestamp"], "%b %d %H:%M:%S")

    # Update the year to the current year
    current_year = datetime.now().year
    timestamp = timestamp.replace(year=current_year)

    # Convert to UTC and format for Elasticsearch
    utc_timestamp = timestamp.astimezone(pytz.utc)
    formatted_timestamp = utc_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    # Update the timestamp in the data
    data["timestamp"] = formatted_timestamp

    # Add the @timestamp field with the current UTC time
    data["@timestamp"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    res = es.index(index=index_name,document=data)

print("Complete")