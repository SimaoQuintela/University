(*RESOLUCAO DE EXERCICIOS *)

Theorem logica: (~p0 \/ p1) -> (p0 -> p1).
Proof.
intro.
intro.
elim H.
intro.
contradiction.
intro.
trivial.
Qed.

