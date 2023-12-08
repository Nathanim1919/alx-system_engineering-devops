# Install Nginx
class { 'nginx':
 ensure => present,
}

# Define a custom fact to get the hostname
fact { 'server_hostname':
 setcode => 'hostname',
}

# Configure Nginx with the custom HTTP header
class { 'nginx::config':
 custom_http_header => 'X-Served-By',
 header_value       => $::server_hostname,
}

# Restart Nginx to apply the changes
service { 'nginx':
 ensure => running,
 enable => true,
 subscribe => Class['nginx::config'],
}
