#!/bin/csh
#
# use current working directory for input and output - defaults is 
# to use the users home directory
#$ -cwd
#
# name this job
#$ -N tensLearning
#
# send stdout and stderror to this file
#$ -o outputs/task-$TASK_ID.out
#$ -j y
#

#see where the job is being run
hostname

echo $SGE_TASK_ID

# print date and time
date

AppManToyPrototype $SGE_TASK_ID

