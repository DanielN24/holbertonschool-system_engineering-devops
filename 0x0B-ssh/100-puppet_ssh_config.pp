file { 'password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  content   => '    IdentityFile ~/.ssh/holberton',
}

exec { 'ident':
  path   => '/etc/ssh/ssh_config',
  content   => '    PasswordAuthentication no',
}
