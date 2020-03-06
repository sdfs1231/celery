import requests
from requests import exceptions
import http.cookiejar as cookielib
import os
import re
# 一个session代表一次连接
doubanSession = requests.session()

#生成coockiefile
coockiefile = 'doubanCookies.txt'
# if not os.path.isfile(coockiefile):
#     with open(coockiefile,'w') as f:
#         pass
#save cookie

doubanSession.cookies = cookielib.LWPCookieJar(filename='doubanCookies.txt')



userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"

header = {
    "origin": "https://accounts.douban.com",
    "Refer":"https://accounts.douban.com/passport/login",
    'User-Agent': userAgent,
}



def damaiLogin(account,password):
    print('开始登陆豆瓣网...')

    postUrl = 'https://accounts.douban.com/j/mobile/login/basic'
    testUrl = 'https://accounts.xxx.com'
    postData  = {
        "name":account,
        "password":password
    }
    try:
        responseRes = doubanSession.post(testUrl,data=postData,headers=header,timeout=5)
        print(responseRes.raise_for_status())
    except Exception as e:
        print(e)

    # print(f"text = {responseRes.text}")

def isLoginStatus():
    validateUrl = "https://www.douban.com/doumail/"
    try:
        responseRes = doubanSession.post(validateUrl,headers=header,timeout=5)
    except Exception:
        print('验证登陆出现问题 请检查')
        return False

    if '没有访问权限' in responseRes.text :
        return False
    else:
        return True



# 失败：没有访问权限 <head> <title>
#
if __name__ == '__main__':
    print('正在验证是否已登陆...')
    try:
        doubanSession.cookies.load(filename='doubanCookies.txt')
    except FileNotFoundError:
        print('cookiefile not found prepare coockie file...')
        doubanSession.cookies = cookielib.LWPCookieJar(filename=coockiefile)
        print(f"保存cook: {coockiefile}")
        doubanSession.cookies.save()

    isLogin = isLoginStatus()
    print(f'登陆状态: {isLogin}')
    i = 0
    while not isLogin and i<5:

        print(f'正在重新登陆 {i+1}/5')
        damaiLogin('18681511862','lfh626994')
        isLogin = isLoginStatus()
        i+= 1
    if isLogin:
        print('登陆成功')
    else:
        print('已超过最大重试，请重启程序后再试')

    pattern = re.compile(r'(\w+) (\w+)')

