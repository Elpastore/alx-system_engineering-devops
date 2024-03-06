# Fixes of apache in php file settings

exec{ 'fix-wordpres':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
