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
$access{'not'} || &error($text{'ntfcs_notallowed'});

$whatfailed=$text{'sntfcs_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'main_config'});
$cfile=&read_file_lines($config{'main_config'});


if (!$in{'summary'}) { &error(&text('sntfcs_missing', "generic summary")) }
$tmp=&find_name('generic_summary', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "generic_summary", $in{'summary'});
} else {
 push(@{$cfile}, join('=', "generic_summary", $in{'summary'}));
}

if (!$in{'pager'}) { &error(&text('sntfcs_missing', "pager")) }
$tmp=&find_name('admin_pager', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "admin_pager", $in{'pager'});
} else {
 push(@{$cfile}, join('=', "admin_pager", $in{'pager'}));
}


if (!$in{'email'}) { &error(&text('sntfcs_missing', "admin email address")) }
$tmp=&find_name('admin_email', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "admin_email", $in{'email'});
} else {
 push(@{$cfile}, join('=', "admin_email", $in{'email'}));
}




&flush_file_lines();
&redirect("edit_notifications.cgi");

### END of save_notifications.cgi ###.
