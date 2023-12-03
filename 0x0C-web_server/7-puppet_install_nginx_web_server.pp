# A manifest for nginx web server configuration

exec { 'apt_update':
  command => 'apt-get update',
  path    => ['/usr/bin', '/usr/sbin'],
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt_update'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  mode    => '0664',
  require => Package['nginx'],
}

$redirect_rule = '\n\tlocation /redirect_me {\n\
        \treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\
        }'
exec { 'redirect_me':
  command => "sudo sed -i '/server_name _;/a \\ ${redirect_rule}' /etc/nginx/sites-available/default",
  path    => '/usr/bin:/bin',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
