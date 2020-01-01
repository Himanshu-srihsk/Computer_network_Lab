#Himanshu
#packetdrop
#!/Usr/bin/awk
BEGIN{
total_drop = 0;
}
{
if($1 == "d" ){
total_drop+=1;
}
}
END{
printf("Total No. of Packets Dropped = %d\n", total_drop);
}
