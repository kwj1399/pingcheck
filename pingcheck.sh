#! /bin/bash
HOST=(
10.247.8.213
10.247.8.214
10.247.8.215
)
for i in "${HOST[@]}"
do
ping=`ping -c 1 $i|grep loss|awk '{print $6}'|awk -F "%" '{print $1}'`
if [ $ping -eq 100  ];then
echo ping $i fail
else
echo ping $i ok
fi
done
