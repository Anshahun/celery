enable_utc = False
#timezone = 'Europe/London'
abc = 'bcd'
test_API = 'aadad'
broker_url='redis://127.0.0.1:6379'
result_backend='redis://127.0.0.1:6379'
imports = ['proj.tasks',]
accept_content=['pickle','json']
main='proj'
#A configuration setting will be censored if the name contains any of these sub-strings:
#API, TOKEN, KEY, SECRET, PASS, SIGNATURE, DATABASE