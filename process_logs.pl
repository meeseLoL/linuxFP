#!/usr/bin/perl
#Contributors: Dann, Justin, Lloyd

use strict;
use warnings;

# Check if the log file exists
my $log_file = 'logs.txt';
if (-e $log_file) {
    open my $fh, '<', $log_file or die "Cannot open '$log_file': $!";
    
    # Initialize a counter
    my $count = 0;

    # Process each line in the file
    while (my $line = <$fh>) {
        $count++;
        # Add custom processing logic here if needed
    }

    close $fh;

    print "Total log entries: $count\n";
} else {
    print "Log file does not exist.\n";
}
