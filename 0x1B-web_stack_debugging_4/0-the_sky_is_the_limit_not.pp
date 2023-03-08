exec { '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }

class { '::apache':
mpm_module => 'event',
}

class { '::apache::mod::mpm_event':
max_request_workers => 500,
}

class { '::apache::mod::reqtimeout':
reqtimeout_connect => '10',
reqtimeout_header => '20',
reqtimeout_body => '30',
}

class { '::apache::mod::status':
allow_from => '127.0.0.1 ::1',
}

class { '::firewall':
ensure => 'running',
}

firewall { 'allow http':
port   => 80,
proto  => 'tcp',
action => 'accept',
}

file { '/etc/security/limits.d/99-limits.conf':
ensure  => 'file',
owner   => 'root',
group   => 'root',
mode    => '0644',
content => "root hard nofile 40000\nroot soft nofile 40000\n",
}

package { 'apache2-utils':
ensure => installed,
}

service { 'apache2':
ensure => running,
}

exec { 'run_apache_bench':
command => 'ab -n 2000 -c 100 http://localhost/',
path    => ['/bin', '/usr/bin'],
timeout => 300,
logoutput => true,
onlyif  => 'which ab',
}
