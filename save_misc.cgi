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

require './netsaint-lib.pl';
$access{'misc'} || &error($text{'misc_notallowed'});

$whatfailed=$text{'smisc_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'main_config'});
@hostconf=&parse_config($config{'host_config'});
$cfile=&read_file_lines($config{'main_config'});


if ($in{'sleeptime'} !~ /^\d+$/ ) { &error(&text('smisc_invalid', $in{'sleeptime'}, "Sleep time", "integer")) }
$tmp=&find_name('sleep_time', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "sleep_time", $in{'sleeptime'});
} else {
 push(@{$cfile}, join('=', "sleep_time", $in{'sleeptime'}));
}


if ($in{'useil'}) {
  if ($in{'intervallength'} !~ /^\d+$/ ) {
   &error(&text('smisc_invalid', $in{'intervallength'}, "Interval length", "integer"))
  }
  $tmp=&find_name('interval_length', \@conf);
  if ($tmp) {
   $cfile->[$tmp->{'line'}]=join('=', "interval_length", $in{'intervallength'});
  } else {
   push(@{$cfile}, join('=', "interval_length", $in{'intervallength'}));
  }
}

if ($in{'progmode'} !~ /^[as]$/) {
 &error(&text('smisc_invalid', $in{'progmode'}, $text{'smisc_err_progmode'}, $text{'smisc_err_progmode2'})) }
$tmp=&find_name('program_mode', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "program_mode", $in{'progmode'});
} else {
 push(@{$cfile}, join('=', "program_mode", $in{'progmode'}));
}


if ($in{'aggressivechecks'} !~ /^[01]$/) {
 &error(&text('smisc_invalid', $in{'aggressivechecks'}, 'aggressive host checking', '0 or 1')) }
$tmp=&find_name('use_agressive_host_checking', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "use_agressive_host_checking", $in{'aggressivechecks'});
} else {
 push(@{$cfile}, join('=', "use_agressive_host_checking", $in{'aggressivechecks'}));
}

if ($in{'intchkdelmeth'} !~ /^[dns]$/) {
 &error(&text('smisc_invalid', $in{'intchkdelmeth'}, $text{'smisc_err_inv_icdm'}, $text{'smisc_err_inv_icdm2'})) }
$tmp=&find_name('inter_check_delay_method', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "inter_check_delay_method", $in{'intchkdelmeth'});
} else {
 push(@{$cfile}, join('=', "inter_check_delay_method", $in{'intchkdelmeth'}));
}

if (! $in{'servintleavsmart'}) {
 if ($in{'servintleavfact'} !~ /^\d+$/) {
   &error(&text('smisc_invalid', $in{'servintleavfact'}, $text{'smisc_err_inv_scilf'}, $text{'smisc_err_inv_scilf2'})) }
 }
$tmp=&find_name('service_interleave_factor', \@conf);
if ($tmp) {
 if ($in{'servintleavsmart'}) {
  $cfile->[$tmp->{'line'}]=join('=', "service_interleave_factor", "s");
 } else {
  $cfile->[$tmp->{'line'}]=join('=', "service_interleave_factor", $in{'servintleavfact'});
 }
} else {
 if ($in{'servintleavsmart'}) {
  push(@{$cfile}, join('=', "service_interleave_factor", "s"));
 } else {
  push(@{$cfile}, join('=', "service_interleave_factor", $in{'servintleavfact'}));
 }
}


if ($in{'maxconcchk'} !~ /^\d+$/ ) {
 &error(&text('smisc_invalid', $in{'maxconcchk'}, $text{'smisc_err_inv_maxconcchk'}, $text{'smisc_err_inv_maxconcchk2'}))
}
$tmp=&find_name('max_concurrent_checks', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "max_concurrent_checks", $in{'maxconcchk'});
} else {
 push(@{$cfile}, join('=', "max_concurrent_checks", $in{'maxconcchk'}));
}


if ($in{'servreapfreq'} !~ /^\d+$/ ) {
 &error(&text('smisc_invalid', $in{'servreapfreq'}, $text{'smisc_err_inv_servreapfreq'}, $text{'smisc_err_inv_servreapfreq2'}))
}
$tmp=&find_name('service_reaper_frequency', \@conf);
if ($tmp) {
 $cfile->[$tmp->{'line'}]=join('=', "service_reaper_frequency", $in{'servreapfreq'});
} else {
 push(@{$cfile}, join('=', "service_reaper_frequency", $in{'servreapfreq'}));
}


@commands=&find_struct('command', \@hostconf);
$foundserveh=0;
$foundhosteh=0;

foreach $c (@commands) {
 if ($c->{'value'} eq $in{'globhosteh'}) { $foundhosteh++ }
 if ($c->{'value'} eq $in{'globserveh'}) { $foundserveh++ }
}

if (!$foundserveh && $in{'globserveh'}) {
 &error($text{'smisc_err_globserveh'});
}

if (!$foundhosteh && $in{'globhosteh'}) {
 &error($text{'smisc_err_globhosteh'});
}

$tmp=&find_name('global_host_event_handler', \@conf);
if ($in{'globhosteh'}) {
  if ($tmp) {
   $cfile->[$tmp->{'line'}]=join('=', "global_host_event_handler", $in{'globhosteh'});
  } else {
   push(@{$cfile}, join('=', "global_host_event_handler", $in{'globhosteh'}));
  }
}


$tmp=&find_name('global_service_event_handler', \@conf);
if ($in{'globserveh'}) {
  if ($tmp) {
   $cfile->[$tmp->{'line'}]=join('=', "global_service_event_handler", $in{'globserveh'});
  } else {
   push(@{$cfile}, join('=', "global_service_event_handler", $in{'globserveh'}));
  }
}


&flush_file_lines();
&redirect("edit_misc.cgi");

### END of save_misc.cgi ###.
