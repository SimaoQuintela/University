%%%-------------------------------------------------------------------
%%% @author simao
%%% @copyright (C) 2023, <COMPANY>
%%% @doc
%%%
%%% @end
%%% Created : 05. May 2023 10:25
%%%-------------------------------------------------------------------
-module(ex1).
-author("simao").

% netstat -p tcp -an | grep nome_do_socket
% ou
% nc localhost nome_do_socket

%% API
-export([room/1, acceptor/2, server/1, start/1, stop/1]).

start(Port) -> spawn(fun() -> server(Port) end).

stop(Server) -> Server ! stop.

server(Port) ->
  {ok, LSock} = gen_tcp:listen(Port, [{packet, line}, {reuseaddr, true}]),
  Room = spawn(fun()-> room([]) end),
  spawn(fun() -> acceptor(LSock, Room) end),
  receive stop -> ok end.

acceptor(LSock, Room) ->
  {ok, Sock} = gen_tcp:accept(LSock),
  spawn(fun() -> acceptor(LSock, Room) end),
  Room ! {enter, self()},
  user(Sock, Room).

room(Pids) ->
  receive
    {enter, Pid} ->
      io:format("user entered~p~n", [Pid]),
      room([Pid | Pids]);
    {line, Data} = Msg ->
      io:format("received ~p~n", [Data]),
      [Pid ! Msg || Pid <- Pids],
      room(Pids);
    {leave, Pid} ->
      io:format("user left~n", []),
      room(Pids -- [Pid])
  end.

user(Sock, Room) ->
  receive
    {line, Data} ->
      gen_tcp:send(Sock, Data),
      user(Sock, Room);
    {tcp, _, Data} ->
      Room ! {line, Data},
      user(Sock, Room);
    {tcp_closed, _} ->
      Room ! {leave, self()};
    {tcp_error, _, _} ->
      Room ! {leave, self()}
  end.
