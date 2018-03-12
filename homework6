#!/bin/python
'''homework6'''
# pylint: disable= invalid-name

import sys
import logging
from distutils.sysconfig import get_python_lib
import subprocess
import json
from os import popen
import yaml


logging.basicConfig(format='%(asctime)s %(message)s',
                    level=logging.DEBUG,
                    filename='script.log')
logging.debug('Start logging')

info = {"pyversion": sys.version[:5:],
        "virtenv": sys.base_exec_prefix,
        "sitepackges": get_python_lib(),
        "pyexecute": sys.executable,
        "installpack": popen("pip list --format=legacy", "r").readlines(),
        "path": subprocess.check_output("env | grep ^PATH",
                                        shell=True).decode('utf-8').rstrip('\n'),
        "piplocation": subprocess.check_output("pip --version",
                                               shell=True).decode('utf-8').rstrip('\n')}
logging.debug('Created info list')


def to_json():
    '''out to json'''
    f = open("out.json", "w")
    j = json.dumps(info)
    f.write(j)
    f.close()
    logging.debug('Write json file')
    return 1


def to_yaml():
    '''out yo yml'''
    y = open("out.yaml", "w")
    yaml.dump(info, y, allow_unicode=True)
    y.close()
    logging.debug('Write yaml file')
    return 1


to_json()
to_yaml()

