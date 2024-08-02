#!/usr/bin/perl
use strict;
use warnings;

# Open the log file
open(my $fh, '<', 'logs.txt') or die "Could not open file 'logs.txt' $!";

# Process each line
while (my $line = <$fh>) {
    chomp $line;
    # Example: Print lines that contain 'ERROR'
    if ($line =~ /ERROR/) {
        print "$line\n";
    }
}

close($fh);
