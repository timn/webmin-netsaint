#!/usr/bin/perl

#    NetSaint Configuration Webmin Module
#    Copyright (C) 1999 by Tim Niemueller, Stephen Nodvin, LinuxTel Associates
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

#    Created 29.12.1999


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';
$access{'files'} || &error($text{'efiles_notallowed'});

$whatfailed=$text{'sfiles_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'main_config'});
$cfile=&read_file_lines($config{'main_config'});


if (!$in{'log'}) { &error(&text('sfiles_nofile', "log")) }
$tmp=&find_name('log_file', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "log_file", $in{'log'});
} else {
 push(@{$cfile}, join('=', "log_file", $in{'log'}));
}


if (!$in{'hostcfg'}) { &error(&text('sfiles_nofile'), "host configuration") }
$tmp=&find_name('cfg_file', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "cfg_file", $in{'hostcfg'});
} else {
 push(@{$cfile}, join('=', "cfg_file", $in{'hostcfg'}));
}


if (!$in{'status'}) { &error(&text('sfiles_nofile'), "status") }
$tmp=&find_name('status_file', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "status_file", $in{'status'});
} else {
 push(@{$cfile}, join('=', "status_file", $in{'status'}));
}


if (!$in{'temp'}) { &error(&text('sfiles_nofile'), "temp") }
$tmp=&find_name('temp_file', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "temp_file", $in{'temp'});
} else {
 push(@{$cfile}, join('=', "temp_file", $in{'temp'}));
}

if (!$in{'comm'}) { &error(&text('sfiles_nofile'), "command") }
$tmp=&find_name('command_file', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "command_file", $in{'comm'});
} else {
 push(@{$cfile}, join('=', "command_file", $in{'comm'}));
}

&flush_file_lines();
&redirect("edit_files.cgi");

### END of save_files.cgi ###.
