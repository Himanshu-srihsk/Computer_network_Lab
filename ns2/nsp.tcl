

set ns [new Simulator]
set nf [open out.nam w]
$ns namtrace-all $nf
set tf [open out.tr w]
$ns trace-all $tf
proc finish {} {
global ns nf tf
$ns flush-trace
close $nf
close $tf 
exec nam out.nam &
exec awk -f packet_drop.awk out.tr &
exec awk -f throughput.awk out.tr > out.gr
#exec xgraph out.gr
exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]

$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n0 1Mb 10ms DropTail

$ns queue-limit $n0 $n1 2
$ns queue-limit $n1 $n2 3
$ns queue-limit $n2 $n0 3

set tcp0 [new Agent/TCP]
$ns attach-agent $n0 $tcp0
set sink0 [new Agent/TCPSink]
$ns attach-agent $n1 $sink0
set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0

set tcp1 [new Agent/TCP]
$ns attach-agent $n1 $tcp1
set sink1 [new Agent/TCPSink]
$ns attach-agent $n2 $sink1
set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1

set tcp2 [new Agent/TCP]
$ns attach-agent $n2 $tcp2
set sink2 [new Agent/TCPSink]
$ns attach-agent $n0 $sink2
set ftp2 [new Application/FTP]
$ftp2 attach-agent $tcp2

$ns connect $tcp0 $sink0
#scheduling  ..
$ns at 0.1 "$ftp0 start"
$ns at 10.0 "$ftp0 stop"
$ns connect $tcp1 $sink1
$ns at 0.1 "$ftp1 start"
$ns at 10.0 "$ftp1 stop"
$ns connect $tcp2 $sink2
$ns at 0.1 "$ftp2 start"
$ns at 10.0 "$ftp2 stop"
$ns at 10.1 "finish"
$ns run

