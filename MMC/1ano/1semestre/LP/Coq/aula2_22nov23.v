(* Aula 2 - 22 de novembro de 2023 *)

Section Logica_Proposicional.
Variable D:Set.
Variable c: D.
Variable f: D -> D.
Variable R : D -> D -> Prop.
Variables P Q : D -> Prop.


Lemma hip_univ_1 : (forall x, R x x) ->  R c c.
Proof.
intro H.
specialize H with c.
assumption.
Qed.

Lemma hip_univ_2 : (forall x y, R x y) -> R (f c) c.
Proof.
intro H.
specialize H with (f c) c.
assumption.
Qed.

Lemma hip_univ_3: (forall x y, R x y) -> R (f c) c.
Proof.
intro H.
apply H.
Qed.

Lemma hip_univ_r: ((forall x, P x -> R x x) /\ P c) -> R c c.
Proof.
intro H.
destruct H as [H1 H2]. (*H1 é o forall ... , H2 é o P c*)
apply H1.
assumption.
Qed.

Lemma exist_distrib_disj: (exists x, P x \/ Q x) <-> (exists x, P x) \/ (exists x, Q x).
Proof.
split;intro.

(* => *)
destruct H.
destruct H.
left.
exists x.
assumption.
right;exists x;assumption.

(* <= *)
destruct H.
destruct H.
exists x. left. assumption.
destruct H.
exists x;right;assumption.
Qed.

Lemma univ_distrib_conj: (forall x, (P x /\ Q x)) <-> (forall x, P x) /\ (forall x, Q x).
split;intro.

(* => *)
split.
intro.
apply H.




