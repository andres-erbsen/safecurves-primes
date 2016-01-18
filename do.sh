#!/bin/sh -e
./coqprime.sh
./safecurves.sh
./convert.py > src/Proof/Primes.v
make
