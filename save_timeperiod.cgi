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

#    Created 12.01.2000


#######################
#    Configuration    #
#######################

require './netsaint-lib.pl';

$whatfailed=$text{'stimeperiod_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});

@timeperiods=&find_struct('timeperiod', \@conf);

$timeperiod=0;
foreach $t (@timeperiods) {
 if ($t->{'value'} eq $in{'name'}) { $timeperiod=$t; last; }
}

if ($timeperiod) {
 if ($in{'delete'}) {
  $access{'timeperioddelete'} || &error($text{'stimeperiod_notallowed_delete'});
 } else {
  $access{'timeperiodedit'} || &error($text{'stimeperiod_notallowed_edit'});
 }
} else {
 if ($in{'new'}) {
  $access{'timeperiodcreate'} || &error($text{'stimeperiod_notallowed_create'});
 }
}

if ($timeperiod && $in{'new'}) {
 # The host already exists and we try to create another one with its name
 &error(&text("stimeperiod_already_exists", $in{'name'}));
}


$in{'timeperiodalias'} || &error($text{'shost_noalias'});

@weekdays=("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday");

foreach $d (@weekdays) {
 chomp $in{$d};
 @{$d}=split(/\s+/, $in{$d});
 foreach $wd (@{$d}) {
  if ($wd !~ /^\d{1,2}:\d{1,2}-\d{1,2}:\d{1,2}$/) {
   &error(&text('stimeperiod_invalid', $wd));
  }
 }
}


$cfile=&read_file_lines($config{'host_config'});


if ($timeperiod) {
 # the timeperiod exists, we change it

 $cfile->[$timeperiod->{'line'}]=join('=',
                                      "timeperiod[$timeperiod->{'value'}]",
                                      join(';',
                                           $in{'timeperiodalias'},
                                           join(',', @sunday),
                                           join(',', @monday),
                                           join(',', @tuesday),
                                           join(',', @wednesday),
                                           join(',', @thursday),
                                           join(',', @friday),
                                           join(',', @saturday),
                                           )
                                      );
} else {
 push(@{$cfile}, join('=',
                      "timeperiod[$in{'name'}]",
                      join(';',
                           $in{'timeperiodalias'},
                           join(',', @sunday),
                           join(',', @monday),
                           join(',', @tuesday),
                           join(',', @wednesday),
                           join(',', @thursday),
                           join(',', @friday),
                           join(',', @saturday),
                           )
                       )
      );
}


&flush_file_lines();
&redirect("edit_timeperiod.cgi?name=$in{'name'}");

### END of save_timeperiod.cgi ###.
