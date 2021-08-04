import datetime, time

mobileAPIServerHost = 'http://110.10.130.51:5002'
mobileAPIServerURL = '/Emergency/EventStatus/EventStatusSave'

param = {
    "EventId": datetime.datetime.today().strftime('%Y%m%d%H%M%S%f')[:-3],
    "EventDateTime": str(time.time()),
    "Regiment": "RG-280",
    "MissionType": "MT-02",
    "EquipID": "ESE",
    "EventType": "EVT-04",
    "ObjectType": "OBT-05",
    "EventRemark": "EE-02",
    "Status": "EVS-01",
    "ActionStartDate": str(time.time()),
    "ActionEndDate": "",
    "ActionContents": "",
    "ResultContents": "",
    "GroupCode": "EE-02",
    "IsSendOk": "N"
}