#!bin/bash
track $1 $2
label=""
logfile="./logfile.txt"

function track {
  makeCheckLogfile # make or check if logfile exist
  if  [ "$1" == "start" ]; then #run start function if input == start
    start $1 $2

  elif [ "$1" == "stop" ]; then #run stop function if input == stop
    stop

  elif [ "$1" == "status" ]; then #run status function if input == status
    status

  elif  [ "$1" == "log" ]; then
    log


  else ## if the parameter is unknown, give the user instructions on how to use the program
    echo "'$1' is a unknown parameter"
    echo "Right way to use program is:
          track start [label]---------Start time tracker a label
          track stop------------------Stop time tracker
          track status----------------Check status of current tracking"
  fi

}



function makeCheckLogfile {
  if ! [ -f "$logfile" ]; then
    touch $logfile
  fi
}

function start {
  echo nest step
  if ! [ "$#" == 2 ]; then
    echo "Error: $# arguemnts where given, but 2 is needed. Please use (start [label])"
  else
    if [ -z "$label" ]; then
      label=$2
      timestamp=$(date +"%T %F") # formatign the timestamp
      echo "START $timestamp" >> $logfile
      echo "LABEL ${label}" >> $logfile

    else
      echo "there is already a running task, please stop thatone before starting a new one"
    fi
  fi
}

function stop {
  if [ -z "$label" ]; then # checks if label variable is empty
    echo "There is no task that is running at the moment"
  else
    timestamp=$(date +"%T %F") # formating the timestamp
    echo "END $timestamp" >> $logfile
    echo "" >> $logfile
    label="" # to make lable avalable for next task
  fi
}

function status {
  if [ -z "$label" ]; then
    echo "No task is running"
  else
    echo "Task ${label} is running"
  fi
}

function log {
  input=$logfile
  startTime=""
  lablename=""
  endTime=""

  while IFS= read -r line
  do
    stLaEn="$(echo "$line" | cut -d " " -f1)"  # holds value for START LABEL END
    if [ "$stLaEn" == "START" ]; then
      startTime="$(echo "$line" | cut -d " " -f2-3)"
    elif [ "$stLaEn" == "LABEL" ]; then
      lablename="$(echo "$line" | cut -d " " -f2)"
    elif [ "$stLaEn" == "END" ]; then
      endTime="$(echo "$line" | cut -d " " -f2-3)"
      StartSec=$(date -u -d "$startTime" +"%s")
      FinalSec=$(date -u -d "$endTime" +"%s")
      TimeDiff=$(($FinalSec - $StartSec))
      echo $TimeDiff
      if [[ $TimeDiff -gt 86400 ]]; then #check if the diff is greater than 24h, if it is it cant use normal H:M:S formating
 # this is because i want to have the extra 0 on sub 10 hour tasks.
        diffHours=$(( $TimeDiff / 60 / 60 ))
        # Minutes
        TimeDiff=$(( $TimeDiff - ($diffHours * 60 * 60) ))
        diffMins=$(( $TimeDiff / 60 ))
        # Seconds
        diffSeconds=$(( $TimeDiff - ($diffMins * 60) ))
        printf "Task ${lablename}: ${diffHours}:"
        date -u -d "$TimeDiff " +"%M:%S"
      else

        printf "Task ${lablename}: "
        date -u -d "0 $TimeDiff sec" +"%H:%M:%S"
      fi
      startTime=""
      lablename=""
      endTime=""
    fi


  done < "$input"
}
