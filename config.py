header_raw = '''Host: api.pandalive.co.kr
Accept: application/json, text/plain, */*
X-Device-Info: {"t":"webMobile","v":"1.0","ui":0}
Accept-Language: zh-CN,zh-Hans;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Origin: https://m.pandalive.co.kr
Content-Length: 0
Connection: keep-alive
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1
Referer: https://m.pandalive.co.kr/
Cookie: _ga_NGSHFJTQS1=GS1.1.1696982891.3.1.1696984196.0.0.0; _ga_PNYVGEQX89=GS1.1.1696982891.3.1.1696984196.0.0.0; _ga_W91XDLC3YE=GS1.1.1696982891.3.1.1696984196.60.0.0; _ga_ZJ51R4C39H=GS1.3.1696982892.3.1.1696984079.60.0.0; partner=login_n; _ga=GA1.1.1953062576.1696952110; _gid=GA1.3.1421150491.1696952114; _ga_0J8HGTPY46=GS1.1.1696982891.3.1.1696984064.0.0.0; 3be3f8e358abbf54cec643229de77fc9e4f3f0bbc9b171580d45d13aaa374c16=9WOD1JFu13r%2FhUJso3Q%2Biap8kD2sUMMRvrtA9J0xUZkEiB8SU7u3bfgK0S1egn1mtEqC0ik2SvGnfwl94RKgekx10waSC99rKfKXtOPqYMsjD70PVZ5cJhpI%2FOYbH1bhLwqehOKd%2FYVavDtKDpvzMSDWWn8%2Fd06iHigrM3tzm9UJY3nvfruq3%2B7h%2BCb4dEf8; userLoginIdx=13339740; userLoginSaveID=WjJjd056QTU%3D; userLoginSaveYN=Y; userLoginYN=Y; sessKey=6e318479ede4a4f23544c40a816e80fb421dfadcdece1c80c0eefb5667265108; _gcl_au=1.1.1624971422.1696952110'''


def header_to_json(header_string):
    header_lines = header_string.strip().split('\n')
    header_dict = {}
    for line in header_lines:
        key, value = line.split(': ', 1)
        header_dict[key] = value
    return header_dict
