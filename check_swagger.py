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
        paths = [p for p in d.get('paths', {}) if 'ai-model' in p]
        print('AI model paths:', paths)
    except:
        print('Could not parse swagger')
else:
    print('Swagger not available')
