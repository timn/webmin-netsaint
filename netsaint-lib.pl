
#    NetSaint Configuration Webmin Module
#    Copyright (C) 1999-2000 by Tim Niemueller, Stephen Nodvin, LinuxTel Associates
#    Written by Tim Niemueller <tim@niemueller.de> - http://www.niemueller.de
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    Created: 21.12.1999


do '../web-lib.pl';

$|=1;
&init_config("netsaint");
%access = &get_module_acl();

(-e $config{'main_config'}) || &error(&text('index_merr', $config{'main_config'}, "/config.cgi?$module_name"));
(-e $config{'host_config'}) || &error(&text('index_herr', $config{'host_config'}, "/config.cgi?$module_name"));
(-e $config{'cgi_config'}) || &error(&text('index_cerr', $config{'cgi_config'}, "/config.cgi?$module_name"));

&ReadParse();

# parse_config(configfile)
# Parse one of the config files
# configfile is the path to the configuration file

sub parse_config {
 local(@conf, @lines, $i);
 
 open(CF, $_[0]);
  @lines=<CF>;
 close(CF);
 
 for (my $i; $i<@lines; $i++) {
  local(%directive, $name, $value, @values);
  next if ($lines[$i] =~ /^#/);
  chomp $lines[$i];
  next if (!$lines[$i] || ($lines[$i] =~ /^\s+$/));
  
  ($name, $value)=split('=', $lines[$i], 2);
  @values=split(';', $value);
  
  $directive{'name'}=$name;
  $directive{'values'}=\@values;
  $directive{'line'}=$i;
  
  push(@conf, \%directive);
 }

return @conf; 
}

sub find_name {
 local($conf, $line);
 $conf=$_[1];
 
 foreach $line (@{$conf}) {
  if ($line->{'name'} eq "$_[0]") { return $line }
 }

return undef;
}

sub find_struct {
 local($conf, $line, $name, @rv);
 $name=$_[0];
 $conf=$_[1];

 foreach $line (@{$conf}) {
  if ($line->{'name'} =~ /^${name}\[/) {
   local $tstr=$line->{'name'};
   $line->{'name'}=substr($tstr, 0, index($tstr, '['));
   $line->{'value'}=substr($tstr, index($tstr, '[')+1, (length($tstr)-index($tstr, '[')-2));
   next if (!$line->{'value'});
   push(@rv, $line);
  }
 }

return @rv;
}

$version="0.79.1";
### END.