#!/usr/bin/python3

import os
import sys

sys.path.insert(0, os.path.join(os.environ['CHARM_DIR'], 'lib'))

import charmhelpers.fetch as fetch
import charmhelpers.core.hookenv as hookenv
import charmhelpers.core.host as host
import flask_utils as utils

hooks = hookenv.Hooks()
log = hookenv.log

@hooks.hook('install')
def install():
    fetch.apt_install(['python3-flask'])

@hooks.hook('upgrade-charm')
@hooks.hook('config-changed')
def config_changed():
    utils.setup_flask()

@hooks.hook('flask-master-relation-changed')
def flask_slave_relation_changed():
    utils.setup_flask()

@hooks.hook('start')
def start():
    host.service_start(utils.FLASK_SERVICE)

@hooks.hook('stop')
def stop():
    host.service_stop(utils.FLASK_SERVICE)

@hooks.hook('flask-master-relation-broken')
@hooks.hook('flask-master-relation-departed')
@hooks.hook('flask-master-relation-joined')
def noop():
    pass

if __name__ == "__main__":
    # execute a hook based on the name the program is called by
    hooks.execute(sys.argv)
