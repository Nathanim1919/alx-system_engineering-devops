# Set up my client SSH configuration file
file { '/root/.ssh/config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => '# My school server configuration
Host 100.25.197.89
  HostName 100.25.197.89
  User ubuntu
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
'
}
