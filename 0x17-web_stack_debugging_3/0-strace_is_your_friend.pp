# Attach strace to the Apache process then
# Fix the issue of the error

exec { 'fix_apache':
  command => "bash -c 'sed -i 's/phpp/php/g' /var/www/html/wp-settings.php' ; service apache2 restart",
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
