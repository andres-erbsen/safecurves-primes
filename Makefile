COQ_ARGS := -R coqprime/examples Coqprime -R coqprime/num Coqprime -R coqprime/elliptic Coqprime -R coqprime/PrimalityTest Coqprime -R coqprime/Z Coqprime -R coqprime/List Coqprime -R coqprime/N Coqprime -R coqprime/Tactic Coqprime
MOD_NAME := Crypto
SRC_DIR  := src
MODULES  := Proof/

VS       := $(MODULES:%=src/%/*.v)

.PHONY: coq clean install
.DEFAULT_GOAL: coq

coq: Makefile.coq
	$(MAKE) -f Makefile.coq

Makefile.coq: Makefile $(VS)
	coq_makefile -R $(SRC_DIR) $(MOD_NAME) $(COQ_ARGS) $(VS) -o Makefile.coq

clean: Makefile.coq
	$(MAKE) -f Makefile.coq clean
	rm -f Makefile.coq
