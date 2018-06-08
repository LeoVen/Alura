#!/bin/bash

DIR=~/Documents/GitHub/Alura/Bash/imagens-novos-livros
total=0

convert_image_rec() {

    local SDIR=$1

    for i in $SDIR/*
    do

        if [ -d $i ]
        then
            convert_image_rec $i
        else
            local file=$(basename $i)
            local filename="${file%.*}"

            echo "Converting image $filename"

            convert $SDIR/$filename.jpg $SDIR/$filename.png

            let "total=total+1"
        fi
    done

}

if [ $1 == 'clean' ]
then
    echo "Deleting all .png files"
    find $DIR -type f -name '*.png' -delete

    echo "Deleting log file"
    rm log.txt
else
    convert_image_rec $DIR 2>log.txt
    if [ $? -eq 0 ]
    then
        echo "Conversion Successful"
        echo "Total conversions: $total"
    else
        echo "Conversion failed"
    fi
fi

