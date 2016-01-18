# Checking the SafeCurves primes in Coq

The scripts here download and verify the [SafeCurves primes](https://safecurves.cr.yp.to/primeproofs.html) using [CoqPrime](http://coqprime.gforge.inria.fr/) and expose the facts as a Coq library.

## Examples

	Definition prime' p := 1<p /\ (forall n, 1<n<p -> ~(n|p)).

	Lemma prime2_255_19 : prime (2^255 - 19).
	Proof.
	  (* omitted *)
	Qed.

	Lemma prime2_521_1 : prime (2^521 - 1).
	Proof.
	  (* omitted *)
	Qed.

## Dependencies

- Coq 8.4
- Python 3
- sh
- wget

## Usage

	./do.sh
	cat src/Proof/Primes.v
