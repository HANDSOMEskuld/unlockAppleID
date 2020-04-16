from selenium import webdriver
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import base64
import time 
#from selenium.webdriver import ChromeOptions
chrome_options=Options()
chrome_options.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument('window-size=1920x1080') #指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
#chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
#chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
chrome_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')
#option = ChromeOptions()
#option.add_experimental_option('excludeSwitches', ['enable-automation'])
print('请确保已安装最新版Chrome浏览器和对应chromedriver')
print("正在配置必要文件……")
#driver =webdriver.Chrome()
driver =webdriver.Chrome(chrome_options=chrome_options)#不显示Chrome
#driver.set_window_position(20,40)
#driver.set_window_size(1100,700)
url="https://iforgot.apple.com/"
day1=b'M='#base64码生日信息
sn1301=b'M'#base64码答案1
lx1361=b'M'#base64码答案2
fm1421=b'M'#base64码答案3
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
email=input("请输入要解锁的邮箱：")
print("将要解锁邮箱：",email)
password=input("请输入对应的密码：")
print("密码为：",password)
print("正在连接Apple服务器……")
driver.get(url)
#print(driver.page_source)
#page 1 email
print("正在发送邮箱……")
driver.find_element_by_xpath('/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/global-v2/div/idms-flow/div/forgot-password/div/div/div[1]/idms-step/div/div/div/div[2]/div/div[1]/div/div/idms-textbox/idms-error-wrapper/div/div/input').send_keys(email)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/global-v2/div/idms-flow/div/forgot-password/div/div/div[1]/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button').click()
#page 2 type
#type=WebDriverWait(driver,30).until(driver.find_element_by_xpath('//*[@id="optionquestions"]'))
#type.click()
print("正在选择解锁方式……")
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="optionquestions"]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/sa/idms-flow/div/section/iforgot-nav/div/div/div[1]/div/div/button[2]').click()
#page 3 day
print("正在验证信息1……")
driver.implicitly_wait(30)
driver.find_element_by_xpath('/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/sa/idms-flow/div/section/div/birthday/div[2]/div/masked-date/idms-error-wrapper/div/div/input').send_keys(base64.b64decode(day1).decode())
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/sa/idms-flow/div/section/iforgot-nav/div/div/div[1]/div/div/button[2]').click()
#page 4 questiones
print("正在验证信息2……")
driver.implicitly_wait(3)

#三个验证问题会随机出现2个，需自行浏览器F12查看每个问题输入框的id，每个问题的id都是固定的
	#sn130
try:
	driver.find_element_by_xpath('//*[@id="130"]').send_keys(base64.b64decode(sn1301).decode())
except:
	print("nosn130（此类信息仅可出现一次）")
	

	#lx136
try:
	driver.find_element_by_xpath('//*[@id="136"]').send_keys(base64.b64decode(lx1361).decode())
except:
	print("nolx136（此类信息仅可出现一次）")

	
	#fm142
try:
	driver.find_element_by_xpath('//*[@id="142"]').send_keys(base64.b64decode(fm1421).decode())
except:
	print("nofm142（此类信息仅可出现一次）")

time.sleep(1)	
driver.find_element_by_xpath('/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/sa/idms-flow/div/section/iforgot-nav/div/div/div[1]/div/div/button[2]').click()
#page 5 unlock
print("正在验证信息3……")
driver.implicitly_wait(30)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/sa/idms-flow/div/section/div/web-reset-options/div[2]/div[2]/div/button').click()
#page 6 password
print("正在输入密码……")
driver.implicitly_wait(30)
driver.find_element_by_xpath('/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/sa/idms-flow/div/section/div/web-current-password/div[2]/div[1]/idms-textbox/idms-error-wrapper/div/div/input').send_keys(password)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/sa/idms-flow/div/section/iforgot-nav/div/div/div[1]/div/div/button[2]').click()
#page 7 success
driver.implicitly_wait(5)
try:
	driver.find_element_by_xpath('/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/sa/idms-flow/div/section/div/unlock-success/div[2]/div/button')
	print("已成功解锁！")
except:
	print("密码错误！")
driver.quit()
