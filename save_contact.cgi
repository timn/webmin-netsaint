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

$whatfailed=$text{'scontact_error'};
(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

@conf=&parse_config($config{'host_config'});

@contacts=&find_struct('contact', \@conf);

$contact=0;
foreach $c (@contacts) {
 if ($c->{'value'} eq $in{'name'}) { $contact=$c; last; }
}

if ($contact) {
 if ($in{'delete'}) {
  $access{'contactdelete'} || &error($text{'scontact_notallowed_delete'});
 } else {
  $access{'contactedit'} || &error($text{'scontact_notallowed_edit'});
 }
} else {
 if ($in{'new'}) {
  $access{'contactcreate'} || &error($text{'scontact_notallowed_create'});
 }
}

if ($contact && $in{'new'}) {
 # The host already exists and we try to create another one with its name
 &error(&text("scontact_already_exists", $in{'name'}));
}

$in{'alias'} || &error(&text('scontact_missing', 'contact alias'));
$in{'email'} || &error(&text('scontact_missing', 'contact email'));

if ($in{'notservrec'} !~ /^[01]$/) {
 &error(&text('scontact_invalid', $in{'notserv'}, 'notification on service recovery'))
}
if ($in{'nothostrec'} !~ /^[01]$/) {
 &error(&text('scontact_invalid', $in{'nothostrec'}, 'notification on host recovery'))
}
if ($in{'notservcrit'} !~ /^[01]$/) {
 &error(&text('scontact_invalid', $in{'notservcrit'}, 'notification on critical service'))
}
if ($in{'nothostdown'} !~ /^[01]$/) {
 &error(&text('scontact_invalid', $in{'nothostdown'}, 'notification on host down'))
}
if ($in{'notservwarn'} !~ /^[01]$/) {
 &error(&text('scontact_invalid', $in{'notservwarn'}, 'service warning'))
}
if ($in{'nothostunre'} !~ /^[01]$/) {
 &error(&text('scontact_invalid', $in{'nothostunre'}, 'notification on host unreachable'))
}

@commands=&find_struct('command', \@conf);

@servcomms=split(/\0/, $in{'servcomm'});
@hostcomms=split(/\0/, $in{'hostcomm'});

$cfile=&read_file_lines($config{'host_config'});

if ($contact) {
 # the hostgroup exists, we change it
 if ($in{'delete'}) {
   # we delete an existing contact
   splice(@{$cfile}, $contact->{'line'}, 1);
   &flush_file_lines();
   @conf=&parse_config($config{'host_config'});
 } else {

 $cfile->[$contact->{'line'}]=join('=',
                                   "contact[$contact->{'value'}]",
                                   join(';',
                                        $in{'alias'},
                                        $in{'svcperiod'},
                                        $in{'hostperiod'},
                                        $in{'notservrec'},
                                        $in{'notservcrit'},
                                        $in{'notservwarn'},
                                        $in{'nothostrec'},
                                        $in{'nothostdown'},
                                        $in{'nothostunre'},
                                        join(',', @servcomms),
                                        join(',', @hostcomms),
                                        $in{'email'},
                                        $in{'pager'}
                                        )
                                );
 }
} else {
 if ($in{'delete'}) {
  &error(&text({'scontact_notfound'}, $in{'name'}));
 } else {
 push(@{$cfile}, join('=',
                      "contact[$in{'name'}]",
                      join(';',
                           $in{'alias'},
                           $in{'svcperiod'},
                           $in{'hostperiod'},
                           $in{'notservrec'},
                           $in{'notservcrit'},
                           $in{'notservwarn'},
                           $in{'nothostrec'},
                           $in{'nothostdown'},
                           $in{'nothostunre'},
                           join(',', @servcomms),
                           join(',', @hostcomms),
                           $in{'email'},
                           $in{'pager'}
                           )
                      )
      );
 }
}

@cgroups=&find_struct('contactgroup', \@conf);

if ($in{'delete'} && $contact) {
  foreach $c (@cgroups) {
    local(@lg);
    @lg=split(/,/, $c->{'values'}->[1]);

    if (&indexof($contact->{'value'}, @lg) >= 0) {
      splice(@lg, &indexof($contact->{'value'}, @lg), 1);

      $cfile->[$c->{'line'}]=join('=',
                                  "contactgroup[$c->{'value'}]",
                                  join(';',
                                       $c->{'values'}->[0],
                                       join(',', @lg)
                                       )
                                  );
    }
  }
}


&flush_file_lines();
if ($in{'delete'}) {
  &redirect("list_contacts.cgi");
} else {
  &redirect("edit_contact.cgi?name=$in{'name'}");
}

### END of save_contact.cgi ###.
