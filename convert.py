#!/usr/bin/env python3
import sys, re, math, glob

two_ints = lambda t: (int(t[0]), int(t[1]))
parse_factor = lambda f: two_ints(f.split('^')) if '^' in f else (int(f), 1)
numeric = lambda s: [int(x) for x in re.findall(r'\d+', s)]

print ("(* Proofs by Daniel J. Bernstein and Tanja Lange. SafeCurves: choosing safe curves for elliptic-curve cryptography. https://safecurves.cr.yp.to, accessed 17 January 2016. *) ")
print ("Require Import PocklingtonRefl.\nLocal Open Scope positive_scope.\nSet Virtual Machine.\n\nCreate HintDb primes discriminated.\nHint Resolve prime2.")
for file in sorted(glob.glob('safecurves.cr.yp.to/proof/*.html'), key=numeric):
    if numeric(file) == [2]:
        continue
    with open(file) as f:
        htmlproof = f.read()
    n = re.findall(r'n = (\d+)', htmlproof)[0]
    b = re.findall(r'b = (\d+)', htmlproof)[0]

    factors = [] # list string
    givens = [] # list string
    raw_factors = re.findall(r'\(([\d\s\^\*\+]+)\)\^2 \> n.', htmlproof)[0].split('*')
    for (p, alpha) in sorted(map(parse_factor, raw_factors), key=lambda t: t[0]**t[1], reverse=True):
        factors.append("(%d, %d)" % (p, alpha))
        givens.append("Proof_certif _ prime%d" % p)

    cnt6 = '::' + '\n' + 6*' '
    print ("""
Lemma prime{n} : prime {n}.
Proof.
  apply (Pocklington_refl
    (SPock_certif {n} {b}
    ( {factors}::nil))
    ( {givens}::nil)).
  exact_no_check (refl_equal true).
Qed.
Hint Resolve prime{n} : primes.""".format(n=n, b=b, factors=cnt6.join(factors), givens=cnt6.join(givens)))

for file in ['safecurves.cr.yp.to/twist.html', 'safecurves.cr.yp.to/base.html', 'safecurves.cr.yp.to/field.html']:
    with open(file) as f:
        print ("\n(* Primes mentioned in <https://{file}>: *)".format(file=file))
        for p in set(re.findall(r'>\s?= (2\^.*)', f.read())):
            print ("""
Lemma prime{s} : prime ({p}).
Proof.
  auto with primes.
Qed.""".format(s='_'.join(re.findall(r'[+\d]+', p)).replace('_2_','_').replace('+_','p'), p=p))
