#!/usr/bin/env python3
filepath = '/opt/myownclone/current/MyOwnClone/src/lib/nav-admin.ts'

with open(filepath, 'r') as f:
    content = f.read()

# Fix the broken ia-modelos entry
old = 'href: \ /admin/ia-modelos\\,'
new = 'href: "/admin/ia-modelos",'

old2 = 'label: \AI Models\\,'
new2 = 'label: "AI Models",'

old3 = 'iconKey: \ia-modelos\\,'
new3 = 'iconKey: "ia-modelos",'

old4 = 'tooltip: \Manage AI models and assignments\\,'
new4 = 'tooltip: "Manage AI models and assignments",'

old5 = 'section: \platform\\,'
new5 = 'section: "platform",'

content = content.replace(old, new)
content = content.replace(old2, new2)
content = content.replace(old3, new3)
content = content.replace(old4, new4)
content = content.replace(old5, new5)

with open(filepath, 'w') as f:
    f.write(content)

print('NAV FIXED')
