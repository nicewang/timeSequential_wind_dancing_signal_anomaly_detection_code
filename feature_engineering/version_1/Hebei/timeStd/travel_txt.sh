#!/bin/bash

txt_type="txt"
path_in=""
path_out_ini="pic_test/"
jpg_suffix=".jpg"
for file in ./*
do

	if test -f $file
	then 
		if [ ${file##*.} = $txt_type ]
		then
			path_in=${file##*/}
			path_out=${path_out_ini}${path_in%.*}
			path_out=${path_out}${jpg_suffix}	
			echo $path_in
			echo $path_out
			python getOnePointData.py ${path_in} ${path_out}
		fi
	fi

done
