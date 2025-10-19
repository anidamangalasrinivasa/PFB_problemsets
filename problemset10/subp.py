#!/usr/bin/env python3
import subprocess as subp

output=subp.check_output('ls -l | grep .py',shell=True)
status=subp.check_call('ls -l | grep .py', shell=True)

if status==0:
    output2=subp.check_call('pwd', shell=True)
else:
    print('run was unsuccesful')