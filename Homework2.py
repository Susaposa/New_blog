Top = open('Top Part.html').read()
index = open('index.html').read()
Bottom = open('Bottom.html').read()
full = Top + index + Bottom
open ('finalone.html', 'w+').write(full)
