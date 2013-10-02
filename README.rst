===================
gerrit-client-hooks
===================

Run shell commands on gerrit events.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/gerrit-client-hooks

Usage
-----

* Install it

* Create a file called change-merged, make that executable.

* Run gerrit-hook --key-file <path-to-your-ssh-keyfile>

* change-merged will be run whenever gerrit reports a commit.

* Events are dispatched serially, so change-merged doesn't have
  to handle reentrancy.
