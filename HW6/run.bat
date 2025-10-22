ECHO OFF
REM Comments ('remarks') in batch files start with REM.  Everything after REM is ignored.
REM You may need to change the path of the JRE_LOC variable on your system

REM set JRE_LOC="C:\Program Files\Java\jdk1.8.0_331\bin"

del message.encrypted COPY_message.txt smile.encrypted COPY_smile.png riddle.jpg

java HW6 encrypt .\message.txt .\message.encrypted
java HW6 decrypt .\message.encrypted .\COPY_message.txt

java HW6 encrypt .\smile.png .\smile.encrypted
java HW6 decrypt .\smile.encrypted .\COPY_smile.png

java HW6 decrypt .\riddle.encrypted .\riddle.jpg
