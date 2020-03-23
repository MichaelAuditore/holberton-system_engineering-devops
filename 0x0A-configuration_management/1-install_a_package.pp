# Install package puppet-lint with puppet version must be 2.1.1
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
