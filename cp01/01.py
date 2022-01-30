import sys

print(sys.platform)
print(sys.version)
print('1. Hello {0}'.format(sys.platform))
print('1.1 Hello python {ver}'.format(ver=sys.version))
print(f'2. Hello {sys.platform}')
print('3. Hello %s' % sys.platform)
