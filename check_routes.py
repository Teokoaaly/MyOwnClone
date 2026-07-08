#!/usr/bin/env python3
import subprocess
import json

result = subprocess.run(
    ['curl', '-s', 'http://127.0.0.1:5001/console/api/swagger.json'],
    capture_output=True, text=True
)

if result.returncode == 0:
    try:
        d = json.loads(result.stdout)
        paths = list(d.get('paths', {}).keys())
        print('Total routes:', len(paths))
        for p in paths[:30]:
            print(p)
    except Exception as e:
        print('Error:', e)
else:
    print('Swagger not available')
