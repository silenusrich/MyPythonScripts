import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.reaise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
