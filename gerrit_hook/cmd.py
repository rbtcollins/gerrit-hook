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

import subprocess

from gerritlib import gerrit as _gerrit

def main():
    hostname='review.openstack.org'
    username='tripleo-cd-bot'
    hook_script = 'echo'
    gerrit = _gerrit.Gerrit(
        hostname, username, keyfile='../tripleo-cd/tripleo-cd-bot')
    gerrit.startWatching()
    while True:
        event = gerrit.getEvent()
        if event.get('type') != 'change-merged':
            continue
        subprocess.check_call(hook_script)