
#*******************************************************************************/
# 
#       UPDATE_SH
# 
#       @brief
# 
#       @author   Yukang Chen  @date  2012-06-11 23:42:38
# 
#       COPYRIGHT (C) 2011, Nextop INC., ALL RIGHTS RESERVED.
# 
# ******************************************************************************/

#!/bin/sh

do_commit() {
    cmd="git commit -a -m\"$log\""
    echo $cmd
    git add .;
    git commit -a -m"$log"
    git push;
}

while [ $# -gt 0 ]
do
  case $1 in
    -commit |-u) shift; log=$1; do_commit; exit 0;;
  esac
  shift
done
