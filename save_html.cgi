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
$access{'html'} || &error($text{'html_notallowed'});

$whatfailed=$text{'shtml_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'main_config'});
$cfile=&read_file_lines($config{'main_config'});


if ($in{'autohtml'} !~ /^[01]$/) {
 &error(&text('shtml_invalid', $in{'autohtml'}, 'automatic html generation', '0 or 1')) }
$tmp=&find_name('auto_generate_html', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "auto_generate_html", $in{'autohtml'});
} else {
 push(@{$cfile}, join('=', "auto_generate_html", $in{'autohtml'}));
}


if (!$in{'physicalhtmlpath'}) { &error(&text('shtml_inv_dir'), $in{'physicalhtmlpath'}, "physical HTML path") }
if (!-d $in{'physicalhtmlpath'}) { &error(&text('shtml_inv_dir', $in{'physicalhtmlpath'}, "physical HTML path")) };
$tmp=&find_name('physical_html_path', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "physical_html_path", $in{'physicalhtmlpath'});
} else {
 push(@{$cfile}, join('=', "physical_html_path", $in{'physicalhtmlpath'}));
}

if (!$in{'urlhtmlpath'}) { &error(&text('shtml_inv_dir', $in{'urlhtmlpath'}, "URL HTML path")) }
$tmp=&find_name('url_html_path', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "url_html_path", $in{'urlhtmlpath'});
} else {
 push(@{$cfile}, join('=', "url_html_path", $in{'urlhtmlpath'}));
}


if (!$in{'urlcgibinpath'}) { &error(&text('shtml_inv_dir', $in{'urlcgibinpath'}, "URL CGI path")) }
$tmp=&find_name('url_cgibin_path', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "url_cgibin_path", $in{'urlcgibinpath'});
} else {
 push(@{$cfile}, join('=', "url_cgibin_path", $in{'urlcgibinpath'}));
}


&flush_file_lines();
&redirect("edit_html.cgi");

### END of save_html.cgi ###.
