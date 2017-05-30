# Overview

This charm will manage a individual custom config file for logstash.
This will allow you to use the logstash charm with custom configurations.

# Usage

juju deploy logstash-conf-d logstash-output-file

juju add-relation logstash logstash-output-file

juju config logstash-output-file config="output { fiele { path=> '/var/log/myfile '}}"

This will result in a config file named /etc/logstash/conf.d/logstash-output-file.conf


# Configuration

The content of the 'config' field is directly written in the config file.
No templating or syntax check is performed. It must be a valid logstash configuration.


https://github.com/tbaumann/charm-logstash-conf-d
