body = open('data/11725393.xml', 'rt').read().split('<body>')[1].split('</body>')[0]
splits = body.split('</')
tags = [ s.split('>', 1)[0] for s in splits[1:] ]
print(tags)

text = ''
for tag in tags:
    #print(text.split(f'<{tag}>', 1))
    #text += body.split(f'<{tag}>', 1)[0].split(f'</{tag}>', 1)[0]
    pass

#print(body.split(f'<sec'))

with open('text/11725393.xml', 'w') as f:
    f.write(text)
