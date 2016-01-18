#!/bin/sh -e
wget https://gforge.inria.fr/frs/download.php/file/35201/coqprime_par.zip
unzip coqprime_par.zip
( cd coqprime && make clean && make examples/PocklingtonRefl.vo )
