import time
import sys
from datetime import datetime

ttttt=0.7

def end():
	print('\n没想到...你真的...NB!!!')

def level_1():
	money=[25,50,100,300,500]
	four=4
	mn=[]
	while 0<=four:
		print('你还有'+'\033[35m'+str(four+3)+'\033[0m'+'次抽奖机会!\n\n')
		right=input('是/否(y/n)继续抽奖:')
		if right=='y':
			print('\n\n正在抽奖...')
			time.sleep(ttttt)
			print('你抽到了'+'\033[32m'+str(money[four])+'\033[0m'+'元!')
			mn.append(money[four])
			print('累积'+'\033[36m'+str(sum(mn))+'\033[0m'+'元!')
		if right=='n':
			nr='再考虑考虑?'
			zero=1
			while zero<=10:
				print(nr*zero)
				time.sleep(ttttt)
				zero+=1
			sys.exit(1)
		four-=1

def level_2():
	money=975
	give=[2.5,5]
	times=2
	req=1
	mn=[975]
	while 0<=req:
		print('你还有'+'\033[35m'+str(req+1)+'\033[0m'+'次抽奖机会!\n\n')
		right=input('是/否(y/n)继续抽奖:')
		if right=='y':
			print('\n\n正在抽奖...')
			time.sleep(ttttt)
			print('你抽到了'+'\033[32m'+str(give[req])+'\033[0m'+'元!')
			print('你真幸运!拼多多为你助力翻倍 ==> 获得'+'\033[32m'+str(give[req]*times)+'\033[0m'+'元!')
			mn.append(give[req]*times)
			print('累积'+'\033[36m'+str(sum(mn))+'\033[0m'+'元!')
		if right=='n':
			nr='再考虑考虑?'
			zero=1
			while zero<=10:
				print(nr*zero)
				time.sleep(ttttt)
				zero+=1
			sys.exit(1)
		req-=1

def level_3():
	print('抽奖次数用完!拼多多为你助力,送你3次机会!')
	print('你还有'+'\033[35m'+str(3)+'\033[0m'+'次抽奖机会!\n\n')
	right=input('是/否(y/n)继续抽奖:')
	if right=='y':
		print('\n\n正在抽奖...')
		time.sleep(ttttt)
		print('你抽到了'+'\033[32m'+str(1)+'\033[0m'+'元!')
		print('你真幸运!拼多多为你助力翻8倍 ==> 获得'+'\033[32m'+str(8)+'\033[0m'+'元!')
		print('累积'+'\033[36m'+str(990+8)+'\033[0m'+'元!')
	if right=='n':
			nr='再考虑考虑?'
			zero=1
			while zero<=10:
				print(nr*zero)
				time.sleep(ttttt)
				zero+=1
			sys.exit(1)
	print('你还有'+'\033[35m'+str(2)+'\033[0m'+'次抽奖机会!\n\n')
	rigt=input('是/否(y/n)继续抽奖:')
	if rigt=='y':
		print('\n\n正在抽奖...')
		time.sleep(ttttt)
		print('你抽到了'+'\033[32m'+str(100)+'\033[0m'+'枚硬币!')
		print('你真幸运!拼多多为你助力翻10倍 ==> 获得'+'\033[32m'+str(1000)+'\033[0m'+'枚硬币!')
		print('1000枚硬币可兑换为1元!\n累积'+'\033[36m'+str(990+8+1)+'\033[0m'+'元!')
		print('你还有'+'\033[35m'+str(1)+'\033[0m'+'次抽奖机会!\n\n')
	if rigt=='n':
			nr='再考虑考虑?'
			zero=1
			while zero<=10:
				print(nr*zero)
				time.sleep(ttttt)
				zero+=1
			sys.exit(1)

def level_4():
	money=999
	coin=990
	rigt=input('是/否(y/n)继续抽奖:')
	if rigt=='y':
		print('\n\n正在抽奖...')
		time.sleep(ttttt)
		print('你抽到了'+'\033[32m'+str(99)+'\033[0m'+'枚硬币!')
		print('你真幸运!拼多多为你助力翻10倍 ==> 获得'+'\033[32m'+str(990)+'\033[0m'+'枚硬币!')
		print('1000枚硬币可兑换为1元!\n你还剩'+'\033[36m'+str(10)+'\033[0m'+'枚硬币!')
		print('你还有'+'\033[35m'+str(0)+'\033[0m'+'次抽奖机会!\n\n')
	if rigt=='n':
			nr='再考虑考虑?'
			zero=1
			while zero<=10:
				print(nr*zero)
				time.sleep(ttttt)
				zero+=1
			sys.exit(1)

def can(al):
	times=1
	coin=[1]
	res=[]
	while True:
		if sum(res)>=al:
			print('\n\033[31m恭喜你成功提现!!\033[0m')
			end()
			sys.exit(1)
		else:
			gl=1.5/times
			res.append(gl)
			remain=10-sum(res)
			print('\n\n请邀请微信用户助力继续抽奖吧!')
			r=input('是/否(y/n)已助力:')
			if r=='y':
				print('\n\n正在抽奖...')
				time.sleep(ttttt)
				print('你抽到了'+'\033[32m'+str(gl)+'\033[0m'+'枚硬币!')
				print('还剩'+'\033[35m'+str(remain)+'\033[0m'+'枚硬币即可提现1000元!')
			if r=='n':
				nr='再考虑考虑?'
				zero=1
				while zero<=10:
					print(nr*zero)
					time.sleep(ttttt)
					zero+=1
				sys.exit(1)
		times+=1
print('拼多多送你\033[31m现金红包\033[0m啦!\n\n')
time.sleep(ttttt)
mode=input('请选择打款方式:\n1. 微信支付\n2. 支付宝支付\n:')
def chck(mode):
	if mode=='1':
		return '微信'
	else:
		return '支付宝'
print('\n=======================================\n你最幸运!抽到了\033[32m'+chck(mode)+'打款1000元\033[0m(有机会)!\n=======================================\n')
time.sleep(ttttt)
print('\n===============================\n你是\033[35m新用户\033[0m,抽奖次数加2\n')
time.sleep(ttttt)
print('你\033[35m周围的用户\033[0m抽中过奖,抽奖次数加3\n')
time.sleep(ttttt)
print('你在\033[35m幸运星期'+str(datetime.today().weekday()+1)+'\033[0m抽奖,抽奖次数加2\n===============================\n')
time.sleep(ttttt)
level_1()
level_2()
level_3()
level_4()
can(10)