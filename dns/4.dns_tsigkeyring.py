#coding:utf-8

import dns.query
import dns.tsigkeyring
import dns.update
import sys

keyring = dns.tsigkeyring.from_text({
    'host-example.' : 'XXXXXXXXXXXXXXXXXXXXXX=='
})

update = dns.update.Update('dyn.test.example', keyring=keyring)
update.replace('host', 300, 'a', sys.argv[1])

response = dns.query.tcp(update, '10.0.0.1')