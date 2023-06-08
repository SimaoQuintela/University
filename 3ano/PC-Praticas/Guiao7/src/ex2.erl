%%%-------------------------------------------------------------------
%%% @author simao
%%% @copyright (C) 2023, <COMPANY>
%%% @doc
%%%
%%% @end
%%% Created : 24. Apr 2023 18:09
%%%-------------------------------------------------------------------
-module(ex2).
-author("simao").

-export([create/0, enqueue/3, dequeue/1, test/0]).

create() -> [].

enqueue([], Item, Priority) -> [{Item, Priority}];
enqueue([{Item, PriorityItem}|T], ItemInsert, PriorityInsert) ->
  if
    PriorityInsert >= PriorityItem ->
      [{ItemInsert, PriorityInsert} | [{Item, PriorityItem} | T]];
    true ->
      [ {Item, PriorityItem} | enqueue(T, ItemInsert, PriorityInsert)]
  end.

aux([], _) -> [];
aux([{I, P}|T], {Item, Priority}) ->
  if
    P < Priority ->
      [{I,P} | T];
    true ->
      [{Item, Priority} | aux(T, {I, P})]
  end.

dequeue([]) -> empty;
dequeue([{Item, Priority} | T]) -> aux(T, {Item, Priority}).

test() ->
  Q = create(),
  Q1 = enqueue(Q, 1, 7),
  Q2 = enqueue(Q1, 2, 8),
  Q3 = enqueue(Q2, 3, 9),
  Q4 = enqueue(Q3, 4, 10),
  Q5 = enqueue(Q4, 5, 10),
  Q6 = dequeue(Q5),
  Q7 = lists:map(fun({A,_}) -> A end, Q6),
  Q7.

