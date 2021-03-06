# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import argparse
import subprocess

from gerritlib import gerrit as _gerrit


def main():
    parser = argparse.ArgumentParser(
        description='Run scripts on gerrit events.')
    parser.add_argument("--key-file", help="SSH private key file.")
    args = parser.parse_args()
    hostname = 'review.openstack.org'
    username = 'tripleo-cd-bot'
    gerrit = _gerrit.Gerrit(
        hostname, username, keyfile=args.key_file)
    gerrit.startWatching()
    while True:
        event = gerrit.getEvent()
        if event.get('type') != 'change-merged':
            continue
        returncode = subprocess.call('./' + event.get('type'))
        if returncode:
            print("Event hook failed: (%d)" % returncode)
