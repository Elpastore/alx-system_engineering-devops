#!/usr/bin/env bash
# ssh configuraiton using puppet

file { 'ect/ssh/ssh_config':
  ensure  => present,
  content => "
	
	#SSH client configuration
	host*
	IdentyFile ~/.ssh/school
	PasswordAuthentication no",
}
