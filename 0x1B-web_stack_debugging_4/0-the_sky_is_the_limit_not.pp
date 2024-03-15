# Setting up the amount of traffic that Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'setting_up_nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
