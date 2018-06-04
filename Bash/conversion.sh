#!/bin/bash

DIR=~/Documents/GitHub/Alura/Bash/imagens-livros 
PNGDIR=$DIR/png

convert_image() {
    if [ ! -d $PNGDIR ]
    then
        echo "Creating folder /png"
        mkdir $PNGDIR
    fi

    for i in $DIR/*.jpg
    do
        local file=$(basename $i)
        local filename="${file%.*}"
        echo "Converting image $filename"
        convert $DIR/$filename.jpg $PNGDIR/$filename.png
    done
}

# ---------- ---------- Begin ---------- ---------- #
if [ $1 == 'clean' ]
then
    rm -v $PNGDIR/*.png
    rmdir $PNGDIR
    rm log.txt
else
    convert_image 2>log.txt
    if [ $? -eq 0 ]
    then
        echo "Conversion Successful"
    else
        echo "Conversion failed"
    fi
fi

#filename=$(basename -- "$fullfile")
#extension="${filename##*.}"
#filename="${filename%.*}"

#filename="${fullfile##*/}"