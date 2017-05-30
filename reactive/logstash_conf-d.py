from charms.reactive import when, when_not, set_state, hook, when_any
from charmhelpers.core.hookenv import log, status_set, config, service_name
from charmhelpers.core import hookenv
from charms.reactive.helpers import data_changed
import os


@when_not('logstash-conf.d.installed')
def install_logstash_conf_d():
    set_state('logstash-conf_d.installed')


@when_any('host-system.available', 'host-system.connected')
def started():
    write_config()
    status_set('active', 'Ready')
    set_state('logstash-conf_d.started')


@when('config.changed')
def write_config():
    config = hookenv.config()
    if data_changed('config', config['config']):
        log("Writing config")
        app_name = hookenv.service_name()
        if config['config']:
            with open('/etc/logstash/conf.d/{}.conf'.format(app_name), 'w') as conf_file:
                conf_file.write(str(config['config']))
        else:
            try:
                os.remove('/etc/logstash/conf.d/{}.conf'.format(app_name))
            except FileNotFoundError:
                pass


@hook('stop')
def stopped():
    app_name = hookenv.service_name()
    log("{} is stopping. Deleting conf file.".format(app_name))
    try:
        os.remove('/etc/logstash/conf.d/{}.conf'.format(app_name))
    except FileNotFoundError:
        pass
