%%%-------------------------------------------------------------------
%%% @author simao
%%% @copyright (C) 2023, <COMPANY>
%%% @doc
%%%
%%% @end
%%% Created : 28. Apr 2023 10:20
%%%-------------------------------------------------------------------
-module(login_manager).
-author("simao").

%% API
-export([start/0, create_account/2, close_account/2, login/2, logout/1, online/0]).

start() ->
  register(?MODULE, spawn(fun() -> loop(#{}) end)).

rpc(Request) ->
  ?MODULE ! {Request, self()},
  receive {Res, ?MODULE} -> Res end.

create_account(User, Pass) -> rpc({create_account, User, Pass}).
close_account(User, Pass) -> rpc({close_account, User, Pass}).
login(User, Pass) -> rpc({login, User, Pass}).
logout(User) -> rpc({logout, User}).
online() -> rpc(online).

handle({create_account, User, Pass}, Map) ->
  case maps:find(User, Map) of
    error ->
      {ok, Map#{User => {Pass, false}}};
    _ ->
      {user_exists, Map}
  end;

handle({close_account, User, Pass}, Map) ->
  case maps:find(User, Map) of
    {ok, {Pass, _}} ->
      {ok, maps:remove(User, Map)};
    _ ->
      {invalid, Map}
  end;

handle({login, User, Pass}, Map) ->
  case maps:find(User, Map) of
    {ok, {Pass, _}} ->
      {ok, Map#{User := {Pass, true}}};
    _ ->
      {invalid, Map}
  end;

% falta fazer o logout !!!!!!X

handle(online, Map) ->
  Res = [ User || {User, {_, true}} <- maps:to_list(Map)],
  {Res, Map}.


loop(Map) ->
  receive {Request, From} ->
    {Res, NextState} = handle(Request, Map),
    From ! {Res, ?MODULE},
    loop(NextState)
  end.

%loop(Map) ->
%  receive
%  {{create_account, User, Pass}, From} ->
%      case maps:find(User, Map) of
%        error ->
%          From ! {ok,?MODULE},
%          loop(Map#{User => {Pass, false}});
%        _ ->
%          From ! {user_exists, ?MODULE},
%          loop(Map)
%      end;
%    {{close_account, User, Pass}, From} ->
%      case maps:find(User, Map) of
%        {ok, {Pass, _}} ->
%          From ! {ok, ?MODULE},
%          loop(maps:remove(User, Map));
%        _ ->
%          From ! {invalid, ?MODULE},
%          loop(Map)
%      end
%  end.


%  create_account(User, Pass) ->
%  ?MODULE ! {create_account, User, Pass, self()},
%  receive
%    {Res, ?MODULE} -> Res
%  end.

%close_account(User, Pass) ->
%  ?MODULE ! {close_account, User, Pass, self()},
%  receive
%    {Res, ?MODULE} -> Res
% end.
