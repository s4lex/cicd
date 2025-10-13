#!/usr/bin/env python
import os
import sys
import django
from django.test.utils import get_runner
from django.conf import settings

def run_tests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'cicd.settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['core.tests'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    run_tests()