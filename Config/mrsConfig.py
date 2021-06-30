mrsHost = '192.168.11.100'  # 현재 미사용
mrsPort = 9201  # 현재 미사용

ersHost = '192.168.11.100'
ersPort = 9201 # MRS port : 9102, ERS port : 9202, simulater port : 8888

mrsClientCd = 'SMT'
mrsSiteCd = 'PA1'
sendSystemCd = 'SIM'
headerTypeCd = '001'

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

location = {
  'x': 126.78460836410522,
  'y': 37.761419193645686,
  'z': 0
}