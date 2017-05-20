#!/bin/bash

copy_num=1000  #numbers of coppies

cd /disk/Alteon/bin/

cp sp1 koby
while true
do
for (( i=2; i<=$copy_num; i++ ))
do
d=$[i-1]
cp sp$d sp$i
echo "cp sp$d sp$i"
done
i=$[i-1]
result=`diff -s sp1 sp$i`
echo $result
if [ "$result"  = "Files sp1 and sp$i are identical" ]
then
   final_result="PASS"
else
   final_result="FAIL"
fi
echo "removing sp files , please wait"
rm sp*
cp koby sp1
echo "Test $final_result"
if [ "$final_result" = "FAIL" ]
then
   break
fi
done 
