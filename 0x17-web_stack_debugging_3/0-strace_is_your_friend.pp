# Attach strace to the Apache process
exec { 'strace_apache':
  command => 'strace -p <pid>',
  path    => '/usr/bin',
}

# Use tmux to run strace in one window and curl in another
exec { 'tmux_apache':
  command => 'tmux new-session -d -s "Apache" "strace -p <pid>" "curl -I <url>"',
  path    => '/usr/bin',
}

# Fix the issue
exec { 'fix_apache':
  command => 'fix-command',
  path    => '/usr/bin',
  onlyif  => 'strace -p <pid> | grep <issue>',
}

# Restart Apache
service { 'apache':
  ensure => 'restarted',
}
