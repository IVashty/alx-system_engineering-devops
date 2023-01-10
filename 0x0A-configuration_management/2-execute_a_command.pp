# kill a process
exec { 'pkill_killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin/:/sbin:/bin:/usr/sbin'],
}
