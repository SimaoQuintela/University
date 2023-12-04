(* Estudo para o mini-teste *)

Section Logica_Proposicional.
Variables p0 p1: Prop.

(* 
Theorem enfraquecimento: p0-> (p1 -> p0).
Theorem modus_ponens: p0-> (p0->p1) -> p1.
Lemma intro_conj : p0 -> p1 -> p0 /\ p1.
*)

Theorem enfraquecimento: p0 -> (p1 -> p0).
Proof.
intro.
intro.
apply H.
Qed.

Theorem modus_ponens: p0 -> (p0->p1) -> p1.
Proof.
intro.
intro.
apply H0.
apply H.
Qed.

Theorem intro_conj : p0 -> p1 -> p0 /\ p1.
Proof.
intro.
intro.
split.
apply H.
apply H0.
Qed.

Lemma comutatividade_conj: p0 /\ p1 -> p1 /\ p0.
Proof.
intro.
split.
destruct H.
apply H0.
apply H.
Qed.



Lemma neg_contrad :~(p0/\~p0).
Proof.
intro.
apply H.
destruct H.
apply H.
Qed.


Lemma conj_implica_disj :  p0/\p1 -> p1 \/ p0.
Proof.
intro x.
right.
destruct x.
apply H.
Qed.


Lemma disj_comut : p0\/p1 -> p1 \/ p0.
Proof.
intro.
elim H.
intro.
right.
apply H0.
intro.
left.
apply H0.
Qed.


Lemma disj_comut_2 : p0\/p1 <-> p1 \/ p0.
Proof.
split.
intro.
destruct H.
right.
apply H.
left.
apply H.
intro.
destruct H.
right.
apply H.
left.
apply H.
Qed.

End Logica_Proposicional.

(* Lógica Clássica *)
Require Import Classical.
Section Logica_Classica.
Variable p:Prop.
Check NNPP.

Lemma red_ao_abs: forall p:Prop, (~p->False)->p.
Proof.
intro.
intro.
apply NNPP.
intro.
apply H.
assumption.
Qed.

Lemma dupla_neg: forall p:Prop, ~ ~ p -> p.
Proof.
intro c.
intro.
apply NNPP.
apply H.
Qed.

(* Lemma terceiro_excluido: p \/~p. *)

End Logica_Classica.


(* Quantificadores *)
Section Quantificadores.

Variable D: Set.
Variable c: D.
Variable f: D -> D.
Variable R: D -> D -> Prop.
Variable P: D -> Prop.
Variable Q: D -> Prop.

Lemma hip_univ_1 : (forall x, R x x) ->  R c c.
intro.
specialize H with c.
apply H.
Qed.

Lemma hip_univ_2 : (forall x y, R x y) -> R (f c) c.
Proof.
intro.
specialize H with (f c) c.
apply H.
Qed.

Lemma exist_distrib_disj: (exists x, P x \/ Q x) <-> (exists x, P x) \/ (exists x, Q x).
Proof.
split.
intro.
(* => *)
destruct H.
destruct H.
left;exists x;apply H.
right;exists x;apply H.
(* <= *)
intro.
destruct H.
destruct H.
exists x;left;apply H.
destruct H.
exists x; right; apply H.
Qed.

Lemma univ_distrib_conj: (forall x, (P x /\ Q x)) <-> (forall x, P x) /\ (forall x, Q x).
Proof.
split.
(* => *)
intro.
split.
apply H.
apply H.
(* <= *)
intro.
split.
apply H.
apply H.
Qed.

End Quantificadores.

 


