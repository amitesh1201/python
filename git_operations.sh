#!/bin/bash

while getopts "f:m:p" opt
do
   case $opt in
     f) file_name=$OPTARG
     ;;
     m) msg=$OPTARG
     ;;
     p) push_file="push"     
     ;;
   esac      
done   

git_input(){
  echo "$file_name"	
  echo "$msg"
  echo "$push_file"
  git add $file_name && git commit -m "$msg" && git $push_file

}

git_input
