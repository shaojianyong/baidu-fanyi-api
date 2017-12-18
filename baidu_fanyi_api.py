import json
from urllib import request
from urllib.parse import urlencode


params = {
    'from': 'en',
    'to': 'zh',
    'query': 'Good morning!'
    }

post_data = urlencode(params, encoding='utf8').encode('utf8')

req = request.Request('http://fanyi.baidu.com/v2transapi', post_data, {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Content-Length': len(post_data)
    })
rsp = request.urlopen(req)
res = rsp.read().decode('utf8')
obj = json.loads(res)


'''
{'trans_result': {'from': 'en', 'to': 'zh', 'domain': 'all', 'type': 2, 'status': 0,
'data': [{'dst': '早上好!', 'prefixWrap': 0, 'src': 'Good morning!', 'relation': [],
    'result': [[0, '早上好!', ['0|13'], [], ['0|13'], ['0|10']]]}],
'phonetic': [{'src_str': '早', 'trg_str': 'zǎo'}, {'src_str': '上', 'trg_str': 'shang'},
    {'src_str': '好', 'trg_str': 'hǎo'}, {'src_str': '!', 'trg_str': ' '}],
'keywords': [{'means': ['早安，你好', '再会'], 
'''
print(obj['trans_result']['data'][0])
rsp.close()
