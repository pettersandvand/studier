#!/bin/bash

if [ "$#" -ne 2 ]; then # print error message if invalid number of arguments
    echo "Illegal number of parameters"
    echo "run the script by writing in the console, './filemover.sh currentFilepath newDirectory'"
else
  if [ -f "$1" ] || [ -d "$1" ]; then #check if file exist in directory

      if [ -d "$2" ]; then # check if the new directory exists

          mv $1 $2 # move the file
          echo "file(s)/directory moved sucessfully"
      else # print error message on error
          echo "$2 does not exist."
          echo "write the file path again"
      fi
  else # print error message on error
      echo "$1 does not exist."
      echo "write the file path again"
  fi
fi
