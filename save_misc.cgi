#!/usr/bin/perl

#    NetSaint Configuration Webmin Module
#    Copyright (C) 1999/2000 by Tim Niemueller, Stephen Nodvin, LinuxTel Associates
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

#    Created 09.01.2000


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';
$access{'misc'} || &error($text{'misc_notallowed'});

$whatfailed=$text{'smisc_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'main_config'});
$cfile=&read_file_lines($config{'main_config'});


if ($in{'sleeptime'} !~ /^\d+$/ ) { &error(&text('smisc_invalid', $in{'sleeptime'}, "Sleep time", "integer")) }
$tmp=&find_name('sleep_time', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "sleep_time", $in{'sleeptime'});
} else {
 push(@{$cfile}, join('=', "sleep_time", $in{'sleeptime'}));
}


if ($in{'intervallength'} !~ /^\d+$/ ) {
 &error(&text('smisc_invalid', $in{'intervallength'}, "Interval length", "integer"))
}
$tmp=&find_name('interval_length', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "interval_length", $in{'intervallength'});
} else {
 push(@{$cfile}, join('=', "interval_length", $in{'intervallength'}));
}


if ($in{'aggressivechecks'} !~ /^[01]$/) {
 &error(&text('smisc_invalid', $in{'aggressivechecks'}, 'aggressive host checking', '0 or 1')) }
$tmp=&find_name('use_agressive_host_checking', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "use_agressive_host_checking", $in{'aggressivechecks'});
} else {
 push(@{$cfile}, join('=', "use_agressive_host_checking", $in{'aggressivechecks'}));
}



&flush_file_lines();
&redirect("edit_misc.cgi");

### END of save_misc.cgi ###.
