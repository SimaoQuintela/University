%%%-------------------------------------------------------------------
%%% @author simao
%%% @copyright (C) 2023, <COMPANY>
%%% @doc
%%%
%%% @end
%%% Created : 07. May 2023 23:41
%%%-------------------------------------------------------------------
-module(lobbys).
-author("simao").

% ficheiro de treino com vários clientes a fazer pedidos ao servidor

%% API
-export([start/1, server/1]).

start(Port) -> spawn(fun()->server(Port) end).

server(Port) ->
  {ok, LSock} = gen_tcp:listen(Port, [binary, {packet, line}, {reuseaddr, true}]),
  Rooms = spawn(fun() -> rooms(#{}, #{}) end),
  spawn(fun() -> acceptor(LSock, Rooms) end),
  receive
    stop -> ok
  end.

acceptor(LSock, Rooms) ->
  Res = gen_tcp:accept(LSock),
  case Res of
    {error, Output} -> io:fwrite("Error: ~p", Output);
    {ok, Socket} ->
      spawn(fun() -> acceptor(LSock, Rooms) end),
      Rooms ! {newPlayer, self()},
      client(Socket, Rooms)
  end.


% a estrutura Rooms tá mal feita
rooms(Users, Rooms) ->
  receive
    {newPlayer, PidPlayer} ->
      NewUsers = maps:put(PidPlayer, "NoName", Users),
      NewRooms = maps:put(PidPlayer, "Hall", Rooms),
      io:format("New Player: Name- ~p,  Room- ~p ~n", ["NoName", "Hall"]),
      rooms(NewUsers, NewRooms);
    {changeUsername, PidPlayer, NewUsername} ->
      NewUsers = maps:update(PidPlayer, NewUsername, Users),
      io:format("Changed Username to: ~p~n", [NewUsername]),
      rooms(NewUsers, Rooms);
    {createRoom, PidPlayer, RoomName} ->
      NewRooms = maps:put(PidPlayer, RoomName, Rooms),
      io:format("Created room: ~p~n", [RoomName]),
      rooms(Users, NewRooms);
    {showRoom, PidPlayer, RoomName} ->
      PeopleIn = maps:get(PidPlayer, Rooms),
      Message = RoomName ++ ": " ++ PeopleIn,
      PidPlayer ! {broadcast, Message},
      rooms(Users, Rooms)

  end.

client(Socket, Rooms) ->
  receive
    {broadcast, ListOfPeople} ->
      gen_tcp:send(Socket, ListOfPeople),
      client(Socket, Rooms);
    {tcp, _, Data} ->
      case re:split(Data, " ") of
        [<<"changeUser">>, NewUsername] ->
          Username = string:trim(binary_to_list(NewUsername), trailing),
          Rooms ! {changeUsername, self(), Username},
          client(Socket, Rooms);
        [<<"createRoom">>, RoomName] ->
          NewRoomName = string:trim(binary_to_list(RoomName), trailing),
          Rooms ! {createRoom, self(), NewRoomName},
          client(Socket, Rooms);
        [<<"showRoom">>, RoomName] ->
          NewRoomName = string:trim(binary_to_list(RoomName), trailing),
          Rooms ! {showRoom, self(), NewRoomName},
          client(Socket, Rooms)
      end

  end.



%handlePlayer(Level) ->
%  receive
%    {joinLobby, Level} ->
%      io:format("Encontrei um jogador com o mesmo nível que eu~n")
%  end.

%  receive
%    {registPlayer, {Name, Level}} ->
%      Q1 = spawn(fun()->handlePlayer(Level) end),
%      server(maps:put(Name, {Q1, Level}, Players))
%  end.
