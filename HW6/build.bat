ECHO OFF
REM Comments ('remarks') in batch files start with REM.  Everything after REM is ignored.
REM You may need to change the path of the COMPILER_LOC variable on your system

REM set COMPILER_LOC="C:\Program Files\Java\jdk1.8.0_331\bin"

del HW6.class

REM %COMPILER_LOC%\javac HW6.java
ECHO ON
javac HW6.java

