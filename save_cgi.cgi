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


$whatfailed=$text{'scgi_error'};
require './netsaint-lib.pl';
$access{'cgi'} || &error($text{'cgi_notallowed'});

@conf=&parse_config($config{'cgi_config'});
$cfile=&read_file_lines($config{'cgi_config'});


if (!$in{'mainconfig'}) { &error($text{'scgi_nomainfile'}) }
$tmp=&find_name('main_config_file', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "main_config_file", $in{'mainconfig'});
} else {
 push(@{$cfile}, join('=', "main_config_file", $in{'mainconfig'}));
}

if (!$in{'physicalhtmlpath'}) { &error(&text('scgi_inv_dir', $in{'physicalhtmlpath'}, "physical HTML path")) }
$tmp=&find_name('physical_html_path', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "physical_html_path", $in{'physicalhtmlpath'});
} else {
 push(@{$cfile}, join('=', "physical_html_path", $in{'physicalhtmlpath'}));
}

if (!$in{'urlhtmlpath'}) { &error(&text('scgi_inv_dir', $in{'urlhtmlpath'}, "URL HTML path")) }
$tmp=&find_name('url_html_path', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "url_html_path", $in{'urlhtmlpath'});
} else {
 push(@{$cfile}, join('=', "url_html_path", $in{'urlhtmlpath'}));
}


if (!$in{'urlcgibinpath'}) { &error(&text('scgi_inv_dir', $in{'urlcgibinpath'}, "URL CGI path")) }
$tmp=&find_name('url_cgibin_path', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "url_cgibin_path", $in{'urlcgibinpath'});
} else {
 push(@{$cfile}, join('=', "url_cgibin_path", $in{'urlcgibinpath'}));
}

if ($in{'suppalwin'} !~ /^[01]$/ ) { &error(&text('scgi_invalid', $in{'suppalwin'}, $text{'scgi_suppalwin'}, $text{'scgi_0or1'})) }
$tmp=&find_name('suppress_alert_window', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "suppress_alert_window", $in{'suppalwin'});
} else {
 push(@{$cfile}, join('=', "suppress_alert_window", $in{'suppalwin'}));
}

if ($in{'refreshrate'} !~ /^\d+$/) { &error(&text('scgi_invalid', $in{'refreshrate'}, $text{'scgi_refresh_rate'}, $text{'scgi_number'})) }
$tmp=&find_name('refresh_rate', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "refresh_rate", $in{'refreshrate'});
} else {
 push(@{$cfile}, join('=', "refresh_rate", $in{'refreshrate'}));
}

if ($in{'tablefgcolor'} !~ /^#[0123456789abcdefABCDEF]{6}$/) { &error(&text('scgi_invalid', $in{'tablefgcolor'}, $text{'scgi_table_fg_color'}, $text{'scgi_hexcolor'})) }
$tmp=&find_name('html_table_fg_color', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "html_table_fg_color", $in{'tablefgcolor'});
} else {
 push(@{$cfile}, join('=', "html_table_fg_color", $in{'tablefgcolor'}));
}

if ($in{'tablebgcolor'} !~ /^#[0123456789abcdefABCDEF]{6}$/) { &error(&text('scgi_invalid', $in{'tablebgcolor'}, $text{'scgi_table_bg_color'}, $text{'scgi_hexcolor'})) }
$tmp=&find_name('html_table_bg_color', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "html_table_bg_color", $in{'tablebgcolor'});
} else {
 push(@{$cfile}, join('=', "html_table_bg_color", $in{'tablebgcolor'}));
}

if ($in{'tablebgevencolor'} !~ /^#[0123456789abcdefABCDEF]{6}$/) { &error(&text('scgi_invalid', $in{'tablebgevencolor'}, $text{'scgi_table_bg_even_color'}, $text{'scgi_hexcolor'})) }
$tmp=&find_name('html_table_bg_even_color', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "html_table_bg_even_color", $in{'tablebgevencolor'});
} else {
 push(@{$cfile}, join('=', "html_table_bg_even_color", $in{'tablebgevencolor'}));
}

if ($in{'tablebgoddcolor'} !~ /^#[0123456789abcdefABCDEF]{6}$/) { &error(&text('scgi_invalid', $in{'tablebgoddcolor'}, $text{'scgi_table_bg_odd_color'}, $text{'scgi_hexcolor'})) }
$tmp=&find_name('html_table_bg_odd_color', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "html_table_bg_odd_color", $in{'tablebgoddcolor'});
} else {
 push(@{$cfile}, join('=', "html_table_bg_odd_color", $in{'tablebgoddcolor'}));
}



&flush_file_lines();
&redirect("edit_cgi.cgi");

### END of save_cgi.cgi ###.