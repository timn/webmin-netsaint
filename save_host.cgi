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

$whatfailed=$text{'shost_error'};

@conf=&parse_config($config{'host_config'});
@cgiconf=&parse_config($config{'cgi_config'});

@hosts=&find_struct('host', \@conf);
@cgihosts=&find_struct('hostextinfo', \@cgiconf);

$host=0;
foreach $h (@hosts) {
 if ($h->{'value'} eq $in{'name'}) { $host=$h; last; }
}

$cgihost=0;
foreach $h (@cgihosts) {
 if ($h->{'value'} eq $in{'name'}) { $cgihost=$h; last; }
}


if ($host) {
 if ($in{'delete'}) {
  $access{'hostdelete'} || &error($text{'shost_notallowed_delete'});
 } else {
  $access{'hostedit'} || &error($text{'shost_notallowed_edit'});
 }
} else {
 if ($in{'new'}) {
  $access{'hostcreate'} || &error($text{'shost_notallowed_create'});
 }
}

if ($host && $in{'new'}) {
 # The host already exists and we try to create another one with its name
 &error(&text("shost_already_exists", $in{'name'}));
}


$in{'hostalias'} || &error($text{'shost_noalias'});
$in{'address'} || &error($text{'shost_noaddress'});

if ($in{'maxattempts'} !~ /^\d+$/) {
 &error($text{'shost_maxattempts_err'});
}


$foundhost=0;
foreach $h (@hosts) {
 if ($h->{'value'} eq $in{'parenthost'}) { $foundhost++ }
}
if (!$foundhost && $in{'parenthost'}) {
 &error($text{'shost_parenthost_err'});
}



@commands=&find_struct('command', \@conf);
$foundchkc=0;
$foundeh=0;

foreach $c (@commands) {
 if ($c->{'value'} eq $in{'checkcommand'}) { $foundchkc++ }
 if ($c->{'value'} eq $in{'eventhandler'}) { $foundeh++ }
}

if (!$foundchkc && $in{'checkcommand'}) {
 &error($text{'shost_checkcommand_err'});
}

if (!$foundeh && $in{'eventhandler'}) {
 &error($text{'shost_eventhandler_err'});
}



@groups=split(/\0/, $in{'groups'});

if (!scalar(@groups)) {
 &error($text{'shost_nogroup'});
}





@periods=&find_struct('timeperiod', \@conf);
$found=0;
foreach $p (@periods) {
 if ($p->{'value'} eq $in{'notperiod'}) {
  $found++;
 }
}
if (!$found && $in{'notperiod'}) {
 &error($text{'shost_notperiod_err'});
}


if ($in{'notinterval'} !~ /^\d+$/) {
 &error($text{'shost_interval_err'});
}

if ($in{'notrecovery'} !~ /^[01]$/) {
 &error(&text('shost_invalid', $in{'notrecovery'}, 'recovery notification', '0 or 1'))
}
if ($in{'notdown'} !~ /^[01]$/) {
 &error(&text('shost_invalid', $in{'notdown'}, 'down notification', '0 or 1'))
}
if ($in{'notunreachable'} !~ /^[01]$/) {
 &error(&text('shost_invalid', $in{'notunreachable'}, 'unreachable notification', '0 or 1'))
}


$cfile=&read_file_lines($config{'host_config'});
$cgifile=&read_file_lines($config{'cgi_config'});


if ($host) {

 if ($in{'delete'}) {
   # we delete an existing host
   splice(@{$cfile}, $host->{'line'}, 1);
   &flush_file_lines();
   @conf=&parse_config($config{'host_config'});
   if ($cgihost) {
     splice(@{$cgifile}, $cgihost->{'line'}, 1);
     &flush_file_lines();
     @cgiconf=&parse_config($config{'cgi_config'});
   }
 } else {
   # the host exists, we change it
   local $ph = $in{'parenthost'} ? $in{'parenthost'} : "";
   local $hcc = $in{'checkcommand'} ? $in{'checkcommand'} : "";
   local $eh = $in{'eventhandler'} ? $in{'eventhandler'} : "";

   $cfile->[$host->{'line'}]=join('=',
                                  "host[$host->{'value'}]",
                                  join(';',
                                       $in{'hostalias'},
                                       $in{'address'},
                                       $ph,
                                       $hcc,
                                       $in{'maxattempts'},
                                       $in{'notinterval'},
                                       $in{'notperiod'},
                                       $in{'notrecovery'},
                                       $in{'notdown'},
                                       $in{'notunreachable'},
                                       $eh
                                       )
                                  );
 }
} else {
 if ($in{'delete'}) {
  &error(&text({'shost_notfound'}, $in{'name'}));
 } else {
 push(@{$cfile}, join('=',
                      "host[$in{'name'}]",
                      join(';',
                           $in{'hostalias'},
                           $in{'address'},
                           $ph,
                           $hcc,
                           $in{'maxattempts'},
                           $in{'notinterval'},
                           $in{'notperiod'},
                           $in{'notrecovery'},
                           $in{'notdown'},
                           $in{'notunreachable'},
                           $eh
                           )
                      )
      );
 }
}

if ($cgihost) {

 if ($in{'delete'}) {
   # we delete an existing host
   splice(@{$cgifile}, $cgihost->{'line'}, 1);
   &flush_file_lines();
   @cgiconf=&parse_config($config{'cgi_config'});
 } else {
   # the host exists, we change it
   $cgifile->[$cgihost->{'line'}]=join('=',
                                       "hostextinfo[$cgihost->{'value'}]",
                                       join(';',
                                            $in{'notesurl'},
                                            $in{'imageicon'},
                                            $in{'imagevrml'},
                                            $in{'imagegd'},
                                            $in{'alttag'}
                                            )
                                       );
 }
} else {
 if (!$in{'delete'}) {
   push(@{$cgifile}, join('=',
                        "hostextinfo[$in{'name'}]",
                        join(';',
                             $in{'notesurl'},
                             $in{'imageicon'},
                             $in{'imagevrml'},
                             $in{'imagegd'},
                             $in{'alttag'}
                             )
                        )
      );
 }
}




local @hostgroups=&find_struct('hostgroup', \@conf);

if ($in{'delete'} && $host) {
  foreach $g (@hostgroups) {
    local(@lg);
    @lg=split(/,/, $g->{'values'}->[2]);

    if (&indexof($host->{'value'}, @lg) >= 0) {
      splice(@lg, &indexof($host->{'value'}, @lg), 1);
    }

    # we principally write to the file, although if there are no changes,
    # this is easier and takes not much time, because this is a
    # RAM-only operation (because auf read_file_line/flush... functions
     $cfile->[$g->{'line'}]=join('=',
                                  "hostgroup[$g->{'value'}]",
                                  join(';',
                                       $g->{'values'}->[0],
                                       $g->{'values'}->[1],
                                       join(',', @lg)
                                       )
                                  );

  }
} else {

foreach $g (@hostgroups) {
 local(@lg);

 @lg=split(/,/, $g->{'values'}->[2]);

 if (&indexof($in{'name'}, @lg) < 0) {
  if (&indexof($g->{'value'}, @groups) >= 0) {
   # the group is selected but the host not yet in this hostgroup
   push(@lg, $in{'name'});
  } # otherwise the group is not selected and the host is not in the hostgroup
 } else {
  if (&indexof($g->{'value'}, @groups) < 0) {
   # the host is in the hostgroup, but no longer selected,
   # so we remove the host from the hostgroup
   splice(@lg, &indexof($in{'name'}, @lg), 1);
  } # otherwise the group is selected and the host already member of the hostrgroup
 }

  # we principally write to the file, although if there are no changes,
  # this is easier and takes not much time, because this is a
  # RAM-only operation (because auf read_file_line/flush... functions
   $cfile->[$g->{'line'}]=join('=',
                                "hostgroup[$g->{'value'}]",
                                join(';',
                                     $g->{'values'}->[0],
                                     $g->{'values'}->[1],
                                     join(',', @lg)
                                     )
                                );

}
} # end else (no delete)

&flush_file_lines();
if ($in{'delete'}) {
  &redirect("list_hosts.cgi");
} else {
  &redirect("edit_host.cgi?name=$in{'name'}");
}

### END of save_host.cgi ###.