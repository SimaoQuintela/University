(*Aula Coq 15/11/2023*)

(*Os marcadores (* e *) assinalam início e fim de comentário.*)

(*Toda a expressão Coq tem um dado tipo.*)
(*O comando "Check" permite saber o tipo de uma expressão.*)
Check Prop.
(*"Prop" denota o "tipo das proposições" em Coq.*)


Section Logica_Intuicionista_Proposicional.
(*As secções permitem organizar o código e são criadas com o 
comando "Section". As declarações de variáveis são locais 
às secções.*)

Variables p0 p1:Prop.
(*O comando "Variables" declara variáveis e respetivo tipo.*)

(*Notações Coq para conetivos proposicionais.*)
Check (p0 -> p1).
Check (p0 /\ p1).
Check (p0 \/ p1).
Check (p0 <-> p1).
Check ~p0.
Check False.
(*Maiúscula inicial necessária. Veja-se o resultado de "Check false"*)
Check false.

(*Provemos alguns teoremas do fragmento implicacional.*)

Theorem enfraquecimento: p0-> (p1 -> p0).
(*
O comando "Theorem" permite conjecturar que uma dada proposição 
é demonstrável. No caso, e recorrendo a sequentes, corresponde a 
conjecturar que o sequente " => p0->(p1->p0)" é derivável ou, 
na terminologia Coq, o "goal" (ou seja a proposição do 
lado direito do sequente, que na "janela de goals" é visível abaixo do traço) 
pode ser provado sem hipóteses adicionais 
(note-se que, na janela de goals, acima do traço aparecem apenas as declarações iniciais),
o que reflete o facto do lado esquerdo do sequente ser vazio. 
O nome atribuído à conjectura (e à prova a construir), no caso, 
foi "enfraquecimento".*)

Proof.
(*O comando "Proof" marca o início da prova, 
que será agora construída interactivamente.*)

intro x. 
(*A tática "intro", no caso, corresponde à aplicação da regra de 
introdução da implicação, sendo "x" a designação para a hipótese obtida. 
Note-se a evolução no estado da prova/sequente: o novo goal passa a ser "p1->p0", 
mas no contexto da hipótese adicional "x:p0", ou seja, o sequente a derivar 
passa a ser "x:p0 => p1->p0".*)

intro y.
(*O estado da prova evolui para o sequente: "x:p0,y:p1 => p0".*)

exact x.
(*No caso, a tática "exact" indica que o goal a provar é uma das hipóteses ("x"),
correspondendo ao facto do novo sequente ser um axioma, 
o que permite concluir a prova.*)

Qed.
(*O comando "Qed" marca o final da prova.*)

(*Veja-se a representação da prova construída para o teorema anterior ou, 
por outras palavras, o lambda-termo extraído da prova através da correspondência 
Curry-Howard.*)
Print enfraquecimento.
(*Escrito numa notação mais próxima da usual: "lambda x^p0 y^p1.x".*)

Theorem modus_ponens: p0-> (p0->p1) -> p1.
Proof.
intros. 
(*Aplica repetidamente a tática intro, 
criando nomes para as hipóteses geradas.*)

apply H0.
(*A tática "apply" usa a hipótese indicada ("H0")
para provar o goal em causa ("p1"), o que, no caso, 
corresponde a uma inferência de eliminação da implicação, 
com "H0" como premissa principal.*)

assumption.
(*A tática "assumption" sugere que a proposição a provar 
é já uma das hipóteses, sem especificar qual.*)

Qed.

Print modus_ponens.

(*Provemos alguns teoremas envolvendo a conjunção.*)

Lemma intro_conj : p0 -> p1 -> p0 /\ p1.
(*O comando "Lemma" constitui uma alternativa para
conjecturar proposições.*)

Proof.

intros x y.
(*Em aplicações sucessivas de introduções, 
é possível fixar nomes para as hipóteses geradas.*)
 
split.
(*No caso, a tática "split" corresponde à introdução da conjunção *) 

auto.
(*A tática "auto" procura construir a prova em questão automaticamente 
(embora de forma muito limitada).*) 

auto.
Qed.

Print intro_conj.
(*O termo extraído da prova corresponde a um lambda-termo numa certa extensão do
Cálculo-lambda.*)
Check conj.

Lemma comutatividade_conj: p0 /\ p1 -> p1 /\ p0.
Proof.
intro x.
elim x.
(*Neste caso, a tática "elim" produzirá  um efeito semelhante 
ao da aplicação de inferencias eliminação para obter cada um dos 
componentes da conjunção. Tal torna-se mais evidente após aplicação
da tática que se segue. 
*)
intros.
(*De facto, em Coq, a conjunção é definida 
indutivamente (observável com: "Print and") 
e "elim" aplica-se genericamente a tais definições. 
Uma alternativa à tática "elim" é a tática "destruct", também 
ela aplicável no contexto de defições indutivas.*) 

(*destruct x.*)

split.
auto.
auto.
Qed.

Print and.

(* Um teorema envolvendo a negação.*)

Lemma neg_contrad :~(p0/\~p0).
Proof.

intro x.
(*Neste caso, "intro" corresponde a uma inferência de 
introdução da negação.*)

destruct x as [y z].
(*Num "destruct" sobre uma conjunção é possível indicar
os nomes para as duas novas hipóteses resultantes.*)

elim z.
(*Neste caso, "elim" corresponde a uma inferência de 
eliminação da negação, com z como premissa principal. 
A tática "contradiction", que procura uma contradição 
entre as hipóteses, concluiria de imediato a prova.*)

assumption.
Qed.

(*Alguns teoremas envolvendo a disjunção.*)

Lemma conj_implica_disj :  p0/\p1 -> p1 \/ p0.
Proof.

intro x.
left.
(*Corresponde à introdução da disjunção via primeira componente.*)

destruct x.
assumption.
Qed.

Lemma disj_comut : p0\/p1 -> p1 \/ p0.
Proof.
intro x.

elim x.
(*Neste caso, a aplicação da tática "elim" produzirá um efeito 
semelhante ao de uma inferencia de eliminação da disjunção 
com a hipótese "x" como premissa principal. Também a disjunção 
é definida indutivamente em Coq (observável com: "Print or").
Novamente, uma alternativa à tática "elim" é a tática "destruct".*) 

intro.

right.
(*Corresponde à introdução da disjunção via segunda componente.*)

assumption.

intro;left;assumption.
(* ";" permite sequenciar táticas *)

Qed.

(*Alguns teoremas envolvendo a equivalência.*)

Lemma disj_comut_2 :p0\/p1 <-> p1 \/ p0.
Proof.

split.
(*Neste caso, "split" tem efeito semelhante a uma inferência de 
introdução da equivalência -atingido exatamente com "split;intro".*)

apply disj_comut.
(*O Coq permite a utilização de proposições já provadas 
(nos mesmos moldes que hipóteses) e note-se 
que o goal atual corresponde ao lema anterior "disj_comut".*)

intro x.
elim x.
intro;right;assumption.

intro;left;assumption.
(*Reproduz exatamente a prova do lema anterior. De facto, 
o lema anterior pode ser generalizado para proposições arbitrárias 
("forall A B:Prop, A\/B -> B \/ A") e utilizado para provar as duas 
direções da equivalência.*) 

Qed.

Lemma equivalencia_implica_implicacao :(p0<->p1 )-> p1 ->p0.
Proof.
intro x.
intro y.

apply x.
(*Neste caso, "apply" corresponde a uma inferência de eliminação 
da equivalência, com "x" como premissa principal.*)

assumption.
Qed.

(*O teorema caracterizador do absurdo.*)

Lemma absurdo : False -> p0.
Proof.
intro x.

elim x.
(*Neste caso, "elim" corresponde a uma inferência de 
eliminação do absurdo, com a hipóse "x" como premissa. 
Também o absurdo é definido indutivamente em Coq. 
Executando "Print False" observa-se que "False" é um tipo indutivo 
para o qual não há "construtores"(regras de introdução).
A tática "contradiction" também concluiria a prova.*)

Qed.

Print False.

End Logica_Intuicionista_Proposicional.

Section Logica_Classica.
(*O Coq baseia-se em lógica intuicionista. No entanto,
é possível assumir princípios equivalentes à 
regra de redução ao absurdo, modificando a base para lógica clássica, 
através da importação da biblioteca "Classical", como se segue.*)

Require Import Classical.

(* Um dos princípios clássicos disponíveis é a "lei da dupla negação", 
designada "NNPP", cujo tipo é "forall A : Prop, ~ ~ A -> A".*)  

Check NNPP.

(*A lei da dupla negação é equivalente ao princípio da redução ao absurdo.*)

Lemma red_ao_abs: forall p:Prop, (~p->False)->p.
Proof.
intro p.
intro x.

apply NNPP.
(*Note-se a aplicação da lei da dupla negação.*)

intro y.
apply x.
assumption.
Qed.

Lemma dupla_neg: forall p:Prop, ~ ~ p -> p.
Proof.
intro p.
intro x.

apply red_ao_abs.
(*Note-se a aplicação da lei da redução ao absurdo.*)

intro y.
apply x.
assumption.
Qed.


Variable p:Prop.

(*Também o princípio do terceiro excluído é equivalente 
à dupla negação (e à redução ao absurdo).*)

Lemma terceiro_excluido: p\/~p.
Proof.

apply NNPP.
(*Note-se a aplicação da lei da dupla negação.*)

intro x.

assert (y:~p).
(*A tática "assert" permite "afirmar" uma dada proposição 
(no caso "~p"), acrescentando-a como hipótese 
(no caso com o nome "y") e 
simultaneamente como uma nova goal a provar.*)

intro z.
apply x.
left;assumption.
apply x.
right;assumption.
Qed.

Lemma terceiro_excl_implica_dupla_neg: ~~p ->p.
Proof.
intro x.

destruct terceiro_excluido.
(*Note-se a aplicação da lei do terceiro excluído.*)

assumption.
contradiction.
Qed.

End Logica_Classica.