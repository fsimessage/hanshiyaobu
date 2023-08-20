import requests
import json
import time
import random
import hashlib

import cpca
from datetime import datetime
from easygoogletranslate import EasyGoogleTranslateOne
import random

class DB:

    def __init__(self):
        self.WECHAT_URL = 'https://api.weixin.qq.com/'
        # 在小程序网页开发管理开发设置里面设置，这个是有效预警小程序的
        self.APP_ID = 'wx30942e801d1cdf59'
        self.APP_SECRET = '8d27712085c062b2b9cefdfdfe094bcb'
        self.ENV = 'feizhouyujing-9g0o9zeu39e328ab'  # 云环境ID云数据库

    def get_access_token(self):
        '''
        获取小程序token
        '''
        url = '{0}cgi-bin/token?grant_type=client_credential&appid={1}&secret={2}'.format(self.WECHAT_URL,
                                                                                          self.APP_ID,
                                                                                          self.APP_SECRET)
        response = requests.get(url)
        result = response.json()
        print(result)
        return result['access_token']

    def access_database(self, accessToken, action, query):
        """
        数据库增删改查操作
        :param accessToken: 访问令牌
        :param action: 操作指令，添加、修改或删除
        :param query: 查询语句
        :return: 响应结果的JSON
        """
        url = f'{self.WECHAT_URL}tcb/{action}?access_token={accessToken}'
        data = {
            "env": self.ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        return response.json()


def get_token():
    respon = requests.get(
        f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={"wxf63dab6abc2027ac"}&secret={"11c7d8db9840bf6f6926cc69b28dd86e"}')
    content = respon.content
    content = content.decode('utf-8')
    data = json.loads(content)
    token = data.get("access_token")
    if token:
        return token


def uniformMessage_send(weapp_template_msg):
    """统一服务消息"""
    token = get_token()
    if not token:
        return False
    url = "https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token=" + token
    if weapp_template_msg:
        response = requests.post(url, json=weapp_template_msg)
        content = response.content.decode('utf-8')
        data = json.loads(content)
        print(data)
def write_json(data):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "hanshiyaobu.txt")
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(data)
    except Exception as e:
        print(f"发生错误：{str(e)}")



def UserAgent():
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36']
    UserAgent = {'User-Agent': random.choice(user_agent_list)}
    return UserAgent

def sendwxmessage(message):
    ####企业微信消息应用ID
    AgentId = '1000003'
    Secret = 'ysZKeQh_Czx8QO5bFpex8A-zJBm_JLjW0yD4p_d9SlQ'
    CompanyId = 'ww53c0e8c78ee4b0de'

    r = requests.post(
        f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CompanyId}&corpsecret={Secret}').json()
    ACCESS_TOKEN = r["access_token"]
    data = {
        "touser": "@all",
        "msgtype": "text",
        "agentid": f"{AgentId}",
        "text": {"content": f"{message}"}
    }
    data = json.dumps(data)
    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={ACCESS_TOKEN}',
                      data=data)

def translate_text(translator, text):
    """
    使用翻译器进行翻译，处理网络错误
    :param translator: 翻译器对象
    :param text: 要翻译的文本
    :return: 翻译结果或错误信息
    """
    try:
        result = translator.translate(text)
        print(f"翻译结果是：{result}")
       
        return result
    except Exception as e:
        print(f"翻译发生错误：{e}")
        return "翻译错误"    
def translationBD(content):
    salt = str(random.randint(0, 50))
    appid = '20211001000961920'
    secretKey = 'nTKWD8mKt5PJTHRaaPTh'
    sign = appid + content + salt + secretKey
    sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()

    head = {
        'q': f'{content}',
        'from': 'kor',
        'to': 'zh',
        'appid': f'{appid}',
        'salt': f'{salt}',
        'sign': f'{sign}'
    }

    response = requests.get('http://api.fanyi.baidu.com/api/trans/vip/translate', head)
    return response.json()['trans_result'][0]['dst']  
def translationBDE(content):
    salt = str(random.randint(0, 50))
    appid = '20211001000961920'
    secretKey = 'nTKWD8mKt5PJTHRaaPTh'
    sign = appid + content + salt + secretKey
    sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()

    head = {
        'q': f'{content}',
        'from': 'en',
        'to': 'zh',
        'appid': f'{appid}',
        'salt': f'{salt}',
        'sign': f'{sign}'
    }

    response = requests.get('http://api.fanyi.baidu.com/api/trans/vip/translate', head)
    return response.json()['trans_result'][0]['dst']                   
def main(collectionName):

    
    
    
    while True:
        try:
            dir_path = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(dir_path, "hanshiyaobu.txt")
            print(file_path)
            web_data = json.loads(open(file_path, 'r', encoding='utf_8_sig').read())
            for weblist in web_data["cities"][0:1]:
                print(time.asctime(time.localtime(time.time())))
                print('正在检索', weblist["name"], '页面更新')
                url = weblist["url"]
                response = requests.get(url, headers=UserAgent(),timeout=(55,55)).content
                soup = BeautifulSoup(response, 'html.parser', from_encoding='utf-8')
                title = soup.select(weblist["titleslect"])[0].get_text()
                print(weblist["name"] +"新的网页内容是" + title)
                print(weblist["name"] +"旧的网页内容是" + weblist["title"])      
                if title != weblist["title"] :    # 开关       
                    try:
                        try:
                            nation = soup.select(weblist["nationslect"])[0].get_text()
                        except IndexError:
                            nation = "未获取到国家信息"
                            print(nation)
                        
                        if nation:
                            # 进行翻译
                            print(nation)
                            
                            nation_translation = translationBD(nation)
                            print("国家是：" + nation_translation)
                        else:
                            nation = "None"
                            print("国家变量为空")
                        
                        # 获取产品信息
                        try:
                            product = soup.select(weblist["productslect"])[0].get_text()
                        except IndexError:
                            product = "未获取到产品信息"
                            print(product)
                        
                        if product:
                            product_translation = translationBD(product)
                            print("产品是：" + product_translation)

                        else:
                            product = "None"
                            print("产品变量为空")
                        
                        # 获取英文产品信息
                        try:
                            enproduct = soup.select(weblist["enproductslect"])[0].get_text()
                        except IndexError:
                            enproduct = "NONE"
                        
                        if enproduct:
                            enproduct_translation = translationBDE(enproduct)
                            print("英文产品是：" + enproduct_translation)

                        else:
                            enproduct_translation = "英文产品变量为空"
                            print("英文产品变量为空")
                        
                        # 获取内容信息
                        try:
                            content = soup.select(weblist["contentslect"])[0].get_text()
                        except IndexError:
                            content = "未获取到内容信息"
                        
                        if content:
                            content_translation = translationBD(content)
                            print("内容是：" + content_translation)

                        else:
                            content_translation = "内容变量为空"
                            print("内容变量为空")
                        try:
                            baozhidate = soup.select(weblist["baozhidateslect"])[0].get_text()
                        except IndexError:
                            baozhidate = ""
                            print(baozhidate)
                        if baozhidate:
                            baozhidate="；保质期："+baozhidate
                            print(baozhidate)

                        else:
                            baozhidate = ""
                        
                        
                        # 获取公司信息
                        try:
                            company = soup.select(weblist["companyslect"])[0].get_text()
                        except IndexError:
                            company = "未获取到公司信息"
                        
                        if company:
                            company_translation = translationBDE(company)

                            print("公司是：" + company_translation)

                            
                            # 对公司名称进行地址解析
        
                            address = "中国"            
                            try:
                                ret = cpca.transform_text_with_addrs(company_translation, pos_sensitive=True)
                                address = f"{ret.loc[0, '省']}{ret.loc[0, '市']}"
                                print("地址是：" + address)
                            except:
                                address = "中国"
                                pass
                        else:
                            company_translation = "公司变量为空"
                            print("公司变量为空")
                        
                    except Exception as e:
                        print("发生异常：", e)
                        
                # 省略其他翻译逻辑
                    current_datetime = datetime.now()

                    # 将日期时间格式化为指定格式
                    formatted_date = current_datetime.strftime('%Y-%m-%d')

                    # 输出格式化后的日期
                    print(formatted_date)
                    current_timestamp = int(time.time())
                    print("Current Timestamp:", current_timestamp)
                    Orgincontent = nation + product + content
                    from easygoogletranslate import EasyGoogleTranslate

                    translator = EasyGoogleTranslate(
                        source_language='ko',
                        target_language='zh-CN',
                        timeout=10
                    )
                    Orgincontenttranslate = translator.translate(Orgincontent)

                    print(Orgincontenttranslate) 
                     
                    foodsafetitle = "韩国通报我国产的"+ content_translation +"的"+ product_translation +"（通报号：无）"
                    new_data = [{               
                        "sectionCode": "yjhzh",
                        "sectionName": "预警和召回",
                        "prodCateCode": "015",
                        "countryRegionCode": "410",
                        "unqualifiedCauseCode": "006",
                        "unqualifiedItemCode": "",
                        "infoTitle": foodsafetitle,
                        "infoType": "1",
                        "prodCateName": "产品分类/其他植物源性食品类",
                        "countryRegionName": "韩国",
                        "circularNumber": "",
                        "sourceArea": nation_translation,
                        "localAddress": address,
                        "enterprise": company,
                        "productName": "产品名称:"+product_translation+"；不合格原因:"+content_translation+ baozhidate,
                        "publishOrg": "食药部",
                        "brand": "/",
                        "unqualifiedItemName": "品质",
                        "unqualifiedCauseName": "不合格原因/污染物",
                        "measure": "境外通报",
                        "sourceAddress": "https://impfood.mfds.go.kr/CFCEE01F01",
                        "sourcePublTime": formatted_date,
                        "Current Timestamp":current_timestamp, 
                        "Orgincontent":Orgincontenttranslate+"产品名称英文翻译："+enproduct_translation,
                        "content": ""

                    }]

                    new_data = "{data:%s}" % new_data
                    print(new_data)
                    db = DB()
                    accessToken = db.get_access_token()  # 获取访问令牌
                    query = f"db.collection('{collectionName}').add({new_data})"  # 添加数据语句
                    result = db.access_database(accessToken, "databaseadd", query)
                    print('插入数据：')
                    print(result)
                    print("成功添加数据")
                    weblist["title"] = title
                    weblist["nation"] = nation
                    weblist["product"] = product
                    weblist["enproduct"] = enproduct
                    weblist["content"] = content
                    weblist["company"] = company
                    

                    print("有更新内容是" + weblist["title"])
                    jsondata = json.dumps(web_data, ensure_ascii=False)  # 序列化简化
                    print('已打包json')
                    write_json(jsondata)
                    print('已写入json文件')
                    print('发送消息')
                    urlnotice = "http://wxpusher.zjiecode.com/api/send/message/?appToken=AT_zNMq0y9vMvgbelbxmTqwd7xCYb7mDFJT&content="+ weblist["name"] + weblist["title"] + Orgincontenttranslate +"&uid=UID_Yfd6ZRU7rWQVCcFYXAus5IfNGQsP&url=http%3a%2f%2fwxpusher.zjiecode.com"
                    requests.get(urlnotice)
                    print('已发送微信')
                    # message = "韩国通报" + title + "（通报号：无）/国家地区：韩国/发布机构：食药部/企业：/采取措施：境外通报/" + "网址：" + weblist["url"]

                    # sendwxmessage(message)
                    # print(message)
                

        except Exception as e:
            print(f"程序异常,错误:{e}")
            print('发送消息')
            urlnotice = "http://wxpusher.zjiecode.com/api/send/message/?appToken=AT_zNMq0y9vMvgbelbxmTqwd7xCYb7mDFJT&content="+ weblist["name"] +"出现错误!"+"&uid=UID_Yfd6ZRU7rWQVCcFYXAus5IfNGQsP&url=http%3a%2f%2fwxpusher.zjiecode.com"
            requests.get(urlnotice)
            print('已发送微信')
        time.sleep(45)  # 暂停60秒后继续下一轮

if __name__ == '__main__':
    try:
        main('test')
    except Exception as e:
        print(f"程序异常,错误:{e}")
        traceback.print_exc()
    














# from easygoogletranslate import EasyGoogleTranslate

# translator = EasyGoogleTranslate(
#     source_language='ko',
#     target_language='zh-CN',
#     timeout=10
# )
# result = translator.translate('소브산 부적합[결과 : 0.0148g/kg 검출/ 규격: 불검출]')

# print(result) 
# # Output: Dies ist ein Beispiel.
