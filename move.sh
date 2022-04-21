#!/bin/sh
#array=(`ls -F | grep -v / | egrep -v "java|cc|md|sh|py|package-lock"`) # list only files
array=(`ls -F | grep -v / | egrep "java|cc|py"`) # list only files
for filename in "${array[@]}"
do
    echo ${filename}
    #echo ${filename}
    dir=`echo ${filename} | cut -d'.' -f1`
    #ext=`echo ${filename} | cut -d'.' -f2`
    #echo ${dir} ${ext}
    #if [ -z ${ext} ]; then
	#echo ${dir}
    #fi
    echo "Move ${filename} => ${dir}"
    mkdir -p ${dir}
    git mv ./${filename} ./${dir}

done
