#!/usr/bin/perl

#    NetSaint Configuration Webmin Module
#    Copyright (C) 1999-2000 by Tim Niemueller, Stephen Nodvin, LinuxTel Associates
#    Written by Tim Niemueller <tim@niemueller.de> - http://www.niemueller.de

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    This module inherited from the Webmin Module Template 0.75.1 by tn

#    Created 09.04.2000

$whatfailed=$text{'sauth_error'};
require './netsaint-lib.pl';
$access{'cgi'} || &error($text{'cgi_notallowed'});


@conf=&parse_config($config{'cgi_config'});
$cfile=&read_file_lines($config{'cgi_config'});


if ($in{'useauth'} !~ /^[01]$/ ) { &error(&text('sauth_invalid', $in{'useauth'}, $text{'sauth_useauth'}, $text{'sauth_0or1'})) }
$tmp=&find_name('use_authentication', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "use_authentication", $in{'useauth'});
} else {
 push(@{$cfile}, join('=', "use_authentication", $in{'useauth'}));
}

$tmp=&find_name('default_user_name', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "default_user_name", $in{'defaultuser'});
} else {
 push(@{$cfile}, join('=', "default_user_name", $in{'defaultuser'}));
}


%directives=('sysinfo'  => 'system_information',
             'confinf'  => 'configuration_information',
             'syscomm'  => 'system_commands',
             'hosts'    => 'all_hosts',
             'hostcomm' => 'all_host_commands',
             'serv'     => 'all_services',
             'servcomm' => 'all_service_commands');

for (keys %directives) {
 if (! $in{$_}) { &error(&text('sauth_invalid2', $text{"sauth_$_"})) }
 $tmp=&find_name("authorized_for_$directives{$_}", \@conf);
 $in{$_} =~ s/\s+/,/g;
 if ($tmp) {
  $cfile->[$tmp->{'line'}]=join('=', "authorized_for_$directives{$_}", $in{$_});
 } else {
  push(@{$cfile}, join('=', "authorized_for_$directives{$_}", $in{$_}));
 }
}


&flush_file_lines();
&redirect("edit_auth.cgi");

### END of save_auth.cgi ###.
