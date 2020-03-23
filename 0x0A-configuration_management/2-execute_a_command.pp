# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => 'usr/bin',
  return  => '[0,1]',
}
