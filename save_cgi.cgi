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
$access{'cgi'} || &error($text{'cgi_notallowed'});

$whatfailed=$text{'scgi_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'cgi_config'});
$cfile=&read_file_lines($config{'cgi_config'});


if (!$in{'mainconfig'}) { &error(&text('scgi_nofile', "main config")) }
if (!-e $in{'mainconfig'}) { &error(&text('scgi_notfound', $in{'mainconfig'})) };
$tmp=&find_name('main_config_file', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "main_config_file", $in{'mainconfig'});
} else {
 push(@{$cfile}, join('=', "main_config_file", $in{'mainconfig'}));
}



&flush_file_lines();
&redirect("edit_cgi.cgi");

### END of save_cgi.cgi ###.
