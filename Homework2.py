# Top = open('Top_Part.html').read()
# index = open('index.html').read()
# Bottom = open('Bottom.html').read()
# about = open('about.html').read()
# full = Top + index + Bottom
# # open ('Docs/finalone.html', 'w+').write(full)

# new_about_file = top + about + bottom
# open('about_new.html', 'w+').write(new_about_file)

top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

index = open('content/index.html').read()
contact = open('content/contact.html').read()
about = open('content/about.html').read()

full = top + index + bottom
open('docs/index.html', 'w+').write(full)

new_about_file = top + about + bottom
open('docs/about.html', 'w+').write(new_about_file)

new_contact_file = top + contact + bottom
open('docs/contact.html', 'w+').write(new_contact_file)