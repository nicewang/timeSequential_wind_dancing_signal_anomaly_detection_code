#!/bin/bash

txt_type="txt"
path_in=""
path_in_sep="/"
path_out_ini="pic_test/"
jpg_suffix=".jpg"

function scandir() {

    for file in $(ls $1)
    do
        d=$1
        if [ ${file##*.} = $txt_type ]
        then
            path_in=${d##*/}${path_in_sep}${file}
            path_out=${path_out_ini}${path_in%.*}
            path_out=${path_out}${jpg_suffix}
            echo $path_in
            echo $path_out
            python onePoint_wave_batchPics.py ${path_in} ${path_out}
        fi

    done

}

for file in ./*
do

    if test -d $file
    then
        scandir $file
    fi

    if test -f $file
    then
         if [ ${file##*.} = $txt_type ]
         then
             path_in=${file##*/}
             path_out=${path_out_ini}${path_in%.*}
             path_out=${path_out}${jpg_suffix}
             echo $path_in
             echo $path_out
             python onePoint_wava_batchPics.py ${path_in} ${path_out}
         fi
    fi
done
