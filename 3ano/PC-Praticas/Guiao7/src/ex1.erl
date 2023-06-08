%%%-------------------------------------------------------------------
%%% @author simao
%%% @copyright (C) 2023, <COMPANY>
%%% @doc
%%%
%%% @end
%%% Created : 24. Apr 2023 10:27
%%%-------------------------------------------------------------------
-module(ex1).
-author("simao").

-export([enqueue/2, dequeue/1, test/0]).

create() -> {[], []}.

enqueue({In, Out}, Item) -> {[Item | In], Out}.

reverse(L) -> reverse(L, []).
reverse([], A) -> A;
reverse([H|T], A) -> reverse(T, [H|A]).

dequeue({[], []}) -> empty;
dequeue({In, [Item | T]}) -> {{In, T}, Item};
dequeue({In, []}) -> dequeue({[], reverse(In)}).

test() ->
  Q1 = create(),
  Q2 = enqueue(Q1, 1),
  Q3 = enqueue(Q2, 2),
  Q4 = enqueue(Q3, 3),
  Q5 = enqueue(Q4, 4),
  Q6 = enqueue(Q5, 5),
  {Q7, 1} = dequeue(Q6),
  {Q8, 2} = dequeue(Q7),
  {Q9, 3} = dequeue(Q8),
  {Q10, 4} = dequeue(Q9),
  {Q11, 5} = dequeue(Q10),
  empty = dequeue(Q11),
  ok.

