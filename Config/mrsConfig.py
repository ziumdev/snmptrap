mrsHost = '211.9.3.50'
mrsPort = 9201

ersHost = '211.9.3.50'
ersPort = 9201 # MRS port : 9102, ERS port : 9202, simulater port : 8888

mrsClientCd = 'SMT'
mrsSiteCd = 'PA1'
sendSystemCd = 'DIE'
headerTypeCd = '001'
disasterCode = 'DIE'

space = ' ' * 10
traceId = '                        '

bodyJson = {
  "StatEvet":{
    "uSvcOutbId": "GST-ZIUM-000TAG002",
    "statEvetId": "GST-ZIUM-000TAG002E01",
    "statEvetNm": "영상장치",
    "statEvetGdCd": "99",    # trap의 경보발생레벨의 값에 0를 붙일것.
    "procSt": "2",  # 1이 아닌 다른 메시지로..
    "outbPosCnt" : 0,
    "outbPosNm": "취사장 옆 자재 창고",
    "statEvetCntn": "일산화탄소 가스 농도 초과",
    "statEvetOutbDtm": "",
    "statEvetItemCnt": 1,
    "statEvetItem": [{"key": "DATA",  "value": "co"}],
    "cpxRelEvetOutbSeqnCnt" : 0
  }
}
trapOidList = {
  'alarmOccurs':  '1.3.6.1.4.1.30960.2.2.1.1.0',
  'alarmNum':     '1.3.6.1.4.1.30960.2.2.1.2.0',
  'alarmLevel':   '1.3.6.1.4.1.30960.2.2.1.3.0',
  'alarmVal':     '1.3.6.1.4.1.30960.2.2.1.4.0',
  'alarmChar':    '1.3.6.1.4.1.30960.2.2.1.5.0',
  'alarmCpoint':  '1.3.6.1.4.1.30960.2.2.1.6.0',
  'alarmAbove':   '1.3.6.1.4.1.30960.2.2.1.7.0',
  'alarmTime':    '1.3.6.1.4.1.30960.2.2.1.8.0',
  'alarmUnit':    '1.3.6.1.4.1.30960.2.2.1.9.0',
  'alarmDesc':    '1.3.6.1.4.1.30960.2.2.1.10.0',
  'alarmValDesc': '1.3.6.1.4.1.30960.2.2.1.11.0',
  'alarmRate':    '1.3.6.1.4.1.30960.2.2.1.12.0',
  'alarmMeasureFormat': '1.3.6.1.4.1.30960.2.2.1.13.0',
 }

location = [{
  'y': '37.761419193645686',
  'x': '126.78460836410522',
  'z': '0'
}]