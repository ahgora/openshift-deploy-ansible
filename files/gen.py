import socket

hosts = {
    'arb',
    'bro',
    'bro2',
    'bro3',
    'bro4',
    'bro5',
    'bro6',
    'cache',
    'cache1',
    'pw2',
    'pw6',
    'pw8',
    'reps',
    'reps2',
}
domain = 'ahgora.com.br'
tpl = '''
address=/{0}.{1}/{2}
address=/{0}/{2}
'''

if __name__ == '__main__':
    for h in hosts:
        ip = socket.gethostbyname('{0}.{1}'.format(h, domain))
        content = tpl.format(h, domain, ip)
        with open('ahgora-{0}.conf'.format(h), 'w') as conf:
            print('Gerando %s' % h)
            conf.write(content)
