#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x5ef0d68e

# Compiled with Coconut version 3.0.4-post_dev17

# Coconut Header: -------------------------------------------------------------

import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.0.4-post_dev17', '3', True)
_coconut_cached__coconut__ = _coconut_sys.modules.get('__coconut__')
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules['_coconut_cached__coconut__'] = _coconut_cached__coconut__
        del _coconut_sys.modules['__coconut__']
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == '__coconut__':
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == '__coconut__':
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and '__coconut_cache__' in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != '__coconut_cache__':
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

import urllib  #1 (line in Coconut source)
import csv  #2 (line in Coconut source)
from warnings import warn  #3 (line in Coconut source)
from collections import defaultdict  #4 (line in Coconut source)

import requests  #6 (line in Coconut source)
import pypokedex  #7 (line in Coconut source)
from bs4 import BeautifulSoup  #8 (line in Coconut source)
from tqdm import tqdm  #9 (line in Coconut source)
from clize import run  #10 (line in Coconut source)


get_entries = (_coconut_base_compose(requests.get, (_coconut.operator.attrgetter("text"), 0, False), (_coconut_complex_partial(BeautifulSoup, {1: "html.parser"}, 2, ()), 0, False), (_coconut.operator.attrgetter("body"), 0, False), (_coconut.operator.methodcaller("find_all", class_="pokedex_entry"), 0, False)))  #13 (line in Coconut source)


name_formatters = (ident, "{}-incarnate".format, "{}-single-strike".format, _coconut.operator.methodcaller("replace", "-f", "-female"), _coconut.operator.methodcaller("replace", "-m", "-male"), _coconut_base_compose(_coconut.operator.methodcaller("split", "-", 1), (_coconut.operator.itemgetter((0)), 0, False)))  #22 (line in Coconut source)

def get_mons(url):  #31 (line in Coconut source)
    for entry in tqdm(get_entries(url)):  #32 (line in Coconut source)
        name = ((((urllib.parse.unquote)((entry).get("data-name"))).replace(" ", "-")).lower())  #33 (line in Coconut source)
        for formatter in name_formatters:  #40 (line in Coconut source)
            formatted_name = formatter(name)  #41 (line in Coconut source)
            try:  #42 (line in Coconut source)
                yield pypokedex.get(name=formatted_name)  #43 (line in Coconut source)
            except pypokedex.exceptions.PyPokedexHTTPError:  #44 (line in Coconut source)
                pass  #45 (line in Coconut source)
            else:  #46 (line in Coconut source)
                break  #47 (line in Coconut source)
        else:  #48 (line in Coconut source)
            warn("failed to find pokemon {_coconut_format_0}".format(_coconut_format_0=(name)))  #49 (line in Coconut source)



class Nature(_coconut.collections.namedtuple("Nature", ('multiplier', 'identifier'))):  #52 (line in Coconut source)
    __slots__ = ()  #52 (line in Coconut source)
    _coconut_is_data = True  #52 (line in Coconut source)
    __match_args__ = ('multiplier', 'identifier')  #52 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #52 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #52 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #52 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #52 (line in Coconut source)
    def __eq__(self, other):  #52 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #52 (line in Coconut source)
    def __hash__(self):  #52 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #52 (line in Coconut source)
    @_coconut_tco  #52 (line in Coconut source)
    def apply(self, stat):  #52 (line in Coconut source)
        return _coconut_tail_call(int, stat * self.multiplier)  #53 (line in Coconut source)

    def __str__(self):  #54 (line in Coconut source)
        return self.identifier  #54 (line in Coconut source)


_coconut_call_set_names(Nature)  #56 (line in Coconut source)
Helpful = Nature(1.1, "+")  #56 (line in Coconut source)
Harmful = Nature(0.9, "-")  #57 (line in Coconut source)
Neutral = Nature(1, "=")  #58 (line in Coconut source)

important_natures = (Helpful, Neutral)  #60 (line in Coconut source)


class Stage(_coconut.collections.namedtuple("Stage", ('stat_stage', 'stat_modifier'))):  #66 (line in Coconut source)
    __slots__ = ()  #66 (line in Coconut source)
    _coconut_is_data = True  #66 (line in Coconut source)
    __match_args__ = ('stat_stage', 'stat_modifier')  #66 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #66 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #66 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #66 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #66 (line in Coconut source)
    def __eq__(self, other):  #66 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #66 (line in Coconut source)
    def __hash__(self):  #66 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #66 (line in Coconut source)
    def __new__(_coconut_cls, _coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #66 (line in Coconut source)
        _coconut_match_check_6 = False  #66 (line in Coconut source)
        _coconut_match_set_name_stat_modifier = _coconut_sentinel  #66 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #66 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #66 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #66 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "stat_stage" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat_modifier" in _coconut_match_kwargs)) <= 1):  #66 (line in Coconut source)
            _coconut_match_temp_10 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("stat_stage")  #66 (line in Coconut source)
            _coconut_match_temp_15 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat_modifier") if "stat_modifier" in _coconut_match_kwargs else 1  #66 (line in Coconut source)
            _coconut_match_temp_11 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #66 (line in Coconut source)
            _coconut_match_set_name_stat_modifier = _coconut_match_temp_15  #66 (line in Coconut source)
            if not _coconut_match_kwargs:  #66 (line in Coconut source)
                _coconut_match_check_6 = True  #66 (line in Coconut source)
        if _coconut_match_check_6:  #66 (line in Coconut source)
            _coconut_match_check_6 = False  #66 (line in Coconut source)
            if not _coconut_match_check_6:  #66 (line in Coconut source)
                _coconut_match_set_name_stat_stage = _coconut_sentinel  #66 (line in Coconut source)
                if (_coconut_match_temp_11) and (_coconut.isinstance(_coconut_match_temp_10, int)) and (_coconut.len(_coconut_match_temp_10) >= 1):  #66 (line in Coconut source)
                    _coconut_match_set_name_stat_stage = _coconut_match_temp_10[0]  #66 (line in Coconut source)
                    _coconut_match_temp_12 = _coconut.len(_coconut_match_temp_10) <= _coconut.max(1, _coconut.len(_coconut_match_temp_10.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_10, "_coconut_data_defaults", {}) and _coconut_match_temp_10[i] == _coconut.getattr(_coconut_match_temp_10, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_10.__match_args__))) if _coconut.hasattr(_coconut_match_temp_10, "__match_args__") else _coconut.len(_coconut_match_temp_10) == 1  # type: ignore  #66 (line in Coconut source)
                    if _coconut_match_temp_12:  #66 (line in Coconut source)
                        _coconut_match_check_6 = True  #66 (line in Coconut source)
                if _coconut_match_check_6:  #66 (line in Coconut source)
                    if _coconut_match_set_name_stat_stage is not _coconut_sentinel:  #66 (line in Coconut source)
                        stat_stage = _coconut_match_set_name_stat_stage  #66 (line in Coconut source)

            if not _coconut_match_check_6:  #66 (line in Coconut source)
                if (not _coconut_match_temp_11) and (_coconut.isinstance(_coconut_match_temp_10, int)):  #66 (line in Coconut source)
                    _coconut_match_check_6 = True  #66 (line in Coconut source)
                if _coconut_match_check_6:  #66 (line in Coconut source)
                    _coconut_match_check_6 = False  #66 (line in Coconut source)
                    if not _coconut_match_check_6:  #66 (line in Coconut source)
                        _coconut_match_set_name_stat_stage = _coconut_sentinel  #66 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_10) in _coconut_self_match_types:  #66 (line in Coconut source)
                            _coconut_match_set_name_stat_stage = _coconut_match_temp_10  #66 (line in Coconut source)
                            _coconut_match_check_6 = True  #66 (line in Coconut source)
                        if _coconut_match_check_6:  #66 (line in Coconut source)
                            if _coconut_match_set_name_stat_stage is not _coconut_sentinel:  #66 (line in Coconut source)
                                stat_stage = _coconut_match_set_name_stat_stage  #66 (line in Coconut source)

                    if not _coconut_match_check_6:  #66 (line in Coconut source)
                        _coconut_match_set_name_stat_stage = _coconut_sentinel  #66 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_10) in _coconut_self_match_types:  #66 (line in Coconut source)
                            _coconut_match_temp_13 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #66 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_13, _coconut.tuple):  #66 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #66 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_13) < 1:  #66 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_13),))  #66 (line in Coconut source)
                            _coconut_match_temp_14 = _coconut.getattr(_coconut_match_temp_10, _coconut_match_temp_13[0], _coconut_sentinel)  #66 (line in Coconut source)
                            if _coconut_match_temp_14 is not _coconut_sentinel:  #66 (line in Coconut source)
                                _coconut_match_set_name_stat_stage = _coconut_match_temp_14  #66 (line in Coconut source)
                                _coconut_match_check_6 = True  #66 (line in Coconut source)
                        if _coconut_match_check_6:  #66 (line in Coconut source)
                            if _coconut_match_set_name_stat_stage is not _coconut_sentinel:  #66 (line in Coconut source)
                                stat_stage = _coconut_match_set_name_stat_stage  #66 (line in Coconut source)




        if _coconut_match_check_6:  #66 (line in Coconut source)
            if _coconut_match_set_name_stat_modifier is not _coconut_sentinel:  #66 (line in Coconut source)
                stat_modifier = _coconut_match_set_name_stat_modifier  #66 (line in Coconut source)

        if not _coconut_match_check_6:  #66 (line in Coconut source)
            raise _coconut_FunctionMatchError('data Stage(int(stat_stage), stat_modifier=1):', _coconut_match_args)  #66 (line in Coconut source)

        return _coconut.tuple.__new__(_coconut_cls, (stat_stage, stat_modifier))  #66 (line in Coconut source)
    @_coconut_tco  #66 (line in Coconut source)
    @_coconut_mark_as_match  #66 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #66 (line in Coconut source)
        _coconut_match_check_0 = False  #66 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #66 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #66 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #66 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #66 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #66 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #66 (line in Coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #66 (line in Coconut source)
            _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #66 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_0  #66 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_1  #66 (line in Coconut source)
            if not _coconut_match_kwargs:  #66 (line in Coconut source)
                _coconut_match_check_0 = True  #66 (line in Coconut source)
        if _coconut_match_check_0:  #66 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #66 (line in Coconut source)
                self = _coconut_match_set_name_self  #66 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #66 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #66 (line in Coconut source)
        if _coconut_match_check_0 and not (self.stat_modifier != 1):  #66 (line in Coconut source)
            _coconut_match_check_0 = False  #66 (line in Coconut source)
        if not _coconut_match_check_0:  #66 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def apply(self, stat if self.stat_modifier != 1) =', _coconut_match_args)  #66 (line in Coconut source)

        return _coconut_tail_call((int), self._replace(stat_modifier=1).apply(stat) * self.stat_modifier)  #68 (line in Coconut source)

    try:  #69 (line in Coconut source)
        _coconut_addpattern_0 = _coconut_addpattern(apply)  # type: ignore  #69 (line in Coconut source)
    except _coconut.NameError:  #69 (line in Coconut source)
        _coconut_addpattern_0 = lambda f: f  #69 (line in Coconut source)
    @_coconut_addpattern_0  #69 (line in Coconut source)
    @_coconut_mark_as_match  #69 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #69 (line in Coconut source)
        _coconut_match_check_1 = False  #69 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #69 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #69 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #69 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #69 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #69 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #69 (line in Coconut source)
            _coconut_match_temp_2 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #69 (line in Coconut source)
            _coconut_match_temp_3 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #69 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_2  #69 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_3  #69 (line in Coconut source)
            if not _coconut_match_kwargs:  #69 (line in Coconut source)
                _coconut_match_check_1 = True  #69 (line in Coconut source)
        if _coconut_match_check_1:  #69 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #69 (line in Coconut source)
                self = _coconut_match_set_name_self  #69 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #69 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #69 (line in Coconut source)
        if _coconut_match_check_1 and not (self.stat_stage > 0):  #69 (line in Coconut source)
            _coconut_match_check_1 = False  #69 (line in Coconut source)
        if not _coconut_match_check_1:  #69 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def apply(self, stat if self.stat_stage > 0) =', _coconut_match_args)  #69 (line in Coconut source)

        return stat * (2 + self.stat_stage) // 2  #70 (line in Coconut source)

    try:  #71 (line in Coconut source)
        _coconut_addpattern_1 = _coconut_addpattern(apply)  # type: ignore  #71 (line in Coconut source)
    except _coconut.NameError:  #71 (line in Coconut source)
        _coconut_addpattern_1 = lambda f: f  #71 (line in Coconut source)
    @_coconut_addpattern_1  #71 (line in Coconut source)
    @_coconut_mark_as_match  #71 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #71 (line in Coconut source)
        _coconut_match_check_2 = False  #71 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #71 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #71 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #71 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #71 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #71 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #71 (line in Coconut source)
            _coconut_match_temp_4 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #71 (line in Coconut source)
            _coconut_match_temp_5 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #71 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_4  #71 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_5  #71 (line in Coconut source)
            if not _coconut_match_kwargs:  #71 (line in Coconut source)
                _coconut_match_check_2 = True  #71 (line in Coconut source)
        if _coconut_match_check_2:  #71 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #71 (line in Coconut source)
                self = _coconut_match_set_name_self  #71 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #71 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #71 (line in Coconut source)
        if _coconut_match_check_2 and not (self.stat_stage < 0):  #71 (line in Coconut source)
            _coconut_match_check_2 = False  #71 (line in Coconut source)
        if not _coconut_match_check_2:  #71 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def apply(self, stat if self.stat_stage < 0) =', _coconut_match_args)  #71 (line in Coconut source)

        return stat * 2 // (2 - self.stat_stage)  #72 (line in Coconut source)

    try:  #73 (line in Coconut source)
        _coconut_addpattern_2 = _coconut_addpattern(apply)  # type: ignore  #73 (line in Coconut source)
    except _coconut.NameError:  #73 (line in Coconut source)
        _coconut_addpattern_2 = lambda f: f  #73 (line in Coconut source)
    @_coconut_addpattern_2  #73 (line in Coconut source)
    @_coconut_mark_as_match  #73 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #73 (line in Coconut source)
        _coconut_match_check_3 = False  #73 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #73 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #73 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #73 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #73 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #73 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #73 (line in Coconut source)
            _coconut_match_temp_6 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #73 (line in Coconut source)
            _coconut_match_temp_7 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #73 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_6  #73 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_7  #73 (line in Coconut source)
            if not _coconut_match_kwargs:  #73 (line in Coconut source)
                _coconut_match_check_3 = True  #73 (line in Coconut source)
        if _coconut_match_check_3:  #73 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #73 (line in Coconut source)
                self = _coconut_match_set_name_self  #73 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #73 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #73 (line in Coconut source)
        if _coconut_match_check_3 and not (self.stat_stage == 0):  #73 (line in Coconut source)
            _coconut_match_check_3 = False  #73 (line in Coconut source)
        if not _coconut_match_check_3:  #73 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def apply(self, stat if self.stat_stage == 0) = stat', _coconut_match_args)  #73 (line in Coconut source)

        return stat  #73 (line in Coconut source)


    def __str__(self):  #75 (line in Coconut source)
        return "{_coconut_format_0:+}".format(_coconut_format_0=(self.stat_stage)) + (" x{_coconut_format_0}".format(_coconut_format_0=(self.stat_modifier)) if self.stat_modifier != 1 else "")  #75 (line in Coconut source)


    @_coconut_mark_as_match  #77 (line in Coconut source)
    def modifier_str(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #77 (line in Coconut source)
        _coconut_match_check_4 = False  #77 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #77 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #77 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #77 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #77 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1):  #77 (line in Coconut source)
            _coconut_match_temp_8 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #77 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_8  #77 (line in Coconut source)
            if not _coconut_match_kwargs:  #77 (line in Coconut source)
                _coconut_match_check_4 = True  #77 (line in Coconut source)
        if _coconut_match_check_4:  #77 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #77 (line in Coconut source)
                self = _coconut_match_set_name_self  #77 (line in Coconut source)
        if _coconut_match_check_4 and not (self.stat_stage == 0):  #77 (line in Coconut source)
            _coconut_match_check_4 = False  #77 (line in Coconut source)
        if not _coconut_match_check_4:  #77 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def modifier_str(self if self.stat_stage == 0) = ""', _coconut_match_args)  #77 (line in Coconut source)

        return ""  #77 (line in Coconut source)

    try:  #78 (line in Coconut source)
        _coconut_addpattern_3 = _coconut_addpattern(modifier_str)  # type: ignore  #78 (line in Coconut source)
    except _coconut.NameError:  #78 (line in Coconut source)
        _coconut_addpattern_3 = lambda f: f  #78 (line in Coconut source)
    @_coconut_addpattern_3  #78 (line in Coconut source)
    @_coconut_mark_as_match  #78 (line in Coconut source)
    def modifier_str(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #78 (line in Coconut source)
        _coconut_match_check_5 = False  #78 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #78 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #78 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #78 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #78 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1):  #78 (line in Coconut source)
            _coconut_match_temp_9 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #78 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_9  #78 (line in Coconut source)
            if not _coconut_match_kwargs:  #78 (line in Coconut source)
                _coconut_match_check_5 = True  #78 (line in Coconut source)
        if _coconut_match_check_5:  #78 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #78 (line in Coconut source)
                self = _coconut_match_set_name_self  #78 (line in Coconut source)
        if not _coconut_match_check_5:  #78 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def modifier_str(self) = str(self) + " "', _coconut_match_args)  #78 (line in Coconut source)

        return str(self) + " "  #78 (line in Coconut source)


_coconut_call_set_names(Stage)  #80 (line in Coconut source)
important_stages = (Stage(-1), Stage(0), Stage(-1, stat_modifier=2), Stage(+1), Stage(+2), Stage(+1, stat_modifier=2))  #80 (line in Coconut source)


@_coconut_tco  #92 (line in Coconut source)
def calc_stat(base, stage=Stage(0), nature=Helpful, level=50, ev=252, iv=31,):  #92 (line in Coconut source)
    return _coconut_tail_call((stage.apply), (nature.apply)(((2 * base) + iv + ev // 4) * level // 100 + 5))  #92 (line in Coconut source)



class PokemonSpeed(_coconut.collections.namedtuple("PokemonSpeed", ('name', 'base_speed', 'speed_stage', 'speed_nature', 'level'))):  #106 (line in Coconut source)
    __slots__ = ()  #106 (line in Coconut source)
    _coconut_is_data = True  #106 (line in Coconut source)
    __match_args__ = ('name', 'base_speed', 'speed_stage', 'speed_nature', 'level')  #106 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #106 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #106 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #106 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #106 (line in Coconut source)
    def __eq__(self, other):  #106 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #106 (line in Coconut source)
    def __hash__(self):  #106 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #106 (line in Coconut source)
    def __new__(_coconut_cls, _coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #106 (line in Coconut source)
        _coconut_match_check_7 = False  #106 (line in Coconut source)
        _coconut_match_set_name_speed_stage = _coconut_sentinel  #106 (line in Coconut source)
        _coconut_match_set_name_speed_nature = _coconut_sentinel  #106 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #106 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #106 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #106 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 5) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "name" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "base_speed" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "speed_stage" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "speed_nature" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 4, "level" in _coconut_match_kwargs)) == 1):  #106 (line in Coconut source)
            _coconut_match_temp_16 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("name")  #106 (line in Coconut source)
            _coconut_match_temp_21 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("base_speed")  #106 (line in Coconut source)
            _coconut_match_temp_26 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("speed_stage")  #106 (line in Coconut source)
            _coconut_match_temp_27 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("speed_nature")  #106 (line in Coconut source)
            _coconut_match_temp_28 = _coconut_match_args[4] if _coconut.len(_coconut_match_args) > 4 else _coconut_match_kwargs.pop("level")  #106 (line in Coconut source)
            if ((isinstance)(_coconut_match_temp_26, Stage)) and ((isinstance)(_coconut_match_temp_27, Nature)):  #106 (line in Coconut source)
                _coconut_match_temp_17 = _coconut.getattr(str, "_coconut_is_data", False) or _coconut.isinstance(str, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in str)  # type: ignore  #106 (line in Coconut source)
                _coconut_match_temp_22 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #106 (line in Coconut source)
                _coconut_match_set_name_speed_stage = _coconut_match_temp_26  #106 (line in Coconut source)
                _coconut_match_set_name_speed_nature = _coconut_match_temp_27  #106 (line in Coconut source)
                _coconut_match_temp_29 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #106 (line in Coconut source)
                if not _coconut_match_kwargs:  #106 (line in Coconut source)
                    _coconut_match_check_7 = True  #106 (line in Coconut source)
        if _coconut_match_check_7:  #106 (line in Coconut source)
            _coconut_match_check_7 = False  #106 (line in Coconut source)
            if not _coconut_match_check_7:  #106 (line in Coconut source)
                _coconut_match_set_name_name = _coconut_sentinel  #106 (line in Coconut source)
                if (_coconut_match_temp_17) and (_coconut.isinstance(_coconut_match_temp_16, str)) and (_coconut.len(_coconut_match_temp_16) >= 1):  #106 (line in Coconut source)
                    _coconut_match_set_name_name = _coconut_match_temp_16[0]  #106 (line in Coconut source)
                    _coconut_match_temp_18 = _coconut.len(_coconut_match_temp_16) <= _coconut.max(1, _coconut.len(_coconut_match_temp_16.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_16, "_coconut_data_defaults", {}) and _coconut_match_temp_16[i] == _coconut.getattr(_coconut_match_temp_16, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_16.__match_args__))) if _coconut.hasattr(_coconut_match_temp_16, "__match_args__") else _coconut.len(_coconut_match_temp_16) == 1  # type: ignore  #106 (line in Coconut source)
                    if _coconut_match_temp_18:  #106 (line in Coconut source)
                        _coconut_match_check_7 = True  #106 (line in Coconut source)
                if _coconut_match_check_7:  #106 (line in Coconut source)
                    if _coconut_match_set_name_name is not _coconut_sentinel:  #106 (line in Coconut source)
                        name = _coconut_match_set_name_name  #106 (line in Coconut source)

            if not _coconut_match_check_7:  #106 (line in Coconut source)
                if (not _coconut_match_temp_17) and (_coconut.isinstance(_coconut_match_temp_16, str)):  #106 (line in Coconut source)
                    _coconut_match_check_7 = True  #106 (line in Coconut source)
                if _coconut_match_check_7:  #106 (line in Coconut source)
                    _coconut_match_check_7 = False  #106 (line in Coconut source)
                    if not _coconut_match_check_7:  #106 (line in Coconut source)
                        _coconut_match_set_name_name = _coconut_sentinel  #106 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_16) in _coconut_self_match_types:  #106 (line in Coconut source)
                            _coconut_match_set_name_name = _coconut_match_temp_16  #106 (line in Coconut source)
                            _coconut_match_check_7 = True  #106 (line in Coconut source)
                        if _coconut_match_check_7:  #106 (line in Coconut source)
                            if _coconut_match_set_name_name is not _coconut_sentinel:  #106 (line in Coconut source)
                                name = _coconut_match_set_name_name  #106 (line in Coconut source)

                    if not _coconut_match_check_7:  #106 (line in Coconut source)
                        _coconut_match_set_name_name = _coconut_sentinel  #106 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_16) in _coconut_self_match_types:  #106 (line in Coconut source)
                            _coconut_match_temp_19 = _coconut.getattr(str, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #106 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_19, _coconut.tuple):  #106 (line in Coconut source)
                                raise _coconut.TypeError("str.__match_args__ must be a tuple")  #106 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_19) < 1:  #106 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'str' only supports %s)" % (_coconut.len(_coconut_match_temp_19),))  #106 (line in Coconut source)
                            _coconut_match_temp_20 = _coconut.getattr(_coconut_match_temp_16, _coconut_match_temp_19[0], _coconut_sentinel)  #106 (line in Coconut source)
                            if _coconut_match_temp_20 is not _coconut_sentinel:  #106 (line in Coconut source)
                                _coconut_match_set_name_name = _coconut_match_temp_20  #106 (line in Coconut source)
                                _coconut_match_check_7 = True  #106 (line in Coconut source)
                        if _coconut_match_check_7:  #106 (line in Coconut source)
                            if _coconut_match_set_name_name is not _coconut_sentinel:  #106 (line in Coconut source)
                                name = _coconut_match_set_name_name  #106 (line in Coconut source)




        if _coconut_match_check_7:  #106 (line in Coconut source)
            _coconut_match_check_7 = False  #106 (line in Coconut source)
            if not _coconut_match_check_7:  #106 (line in Coconut source)
                _coconut_match_set_name_base_speed = _coconut_sentinel  #106 (line in Coconut source)
                if (_coconut_match_temp_22) and (_coconut.isinstance(_coconut_match_temp_21, int)) and (_coconut.len(_coconut_match_temp_21) >= 1):  #106 (line in Coconut source)
                    _coconut_match_set_name_base_speed = _coconut_match_temp_21[0]  #106 (line in Coconut source)
                    _coconut_match_temp_23 = _coconut.len(_coconut_match_temp_21) <= _coconut.max(1, _coconut.len(_coconut_match_temp_21.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_21, "_coconut_data_defaults", {}) and _coconut_match_temp_21[i] == _coconut.getattr(_coconut_match_temp_21, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_21.__match_args__))) if _coconut.hasattr(_coconut_match_temp_21, "__match_args__") else _coconut.len(_coconut_match_temp_21) == 1  # type: ignore  #106 (line in Coconut source)
                    if _coconut_match_temp_23:  #106 (line in Coconut source)
                        _coconut_match_check_7 = True  #106 (line in Coconut source)
                if _coconut_match_check_7:  #106 (line in Coconut source)
                    if _coconut_match_set_name_base_speed is not _coconut_sentinel:  #106 (line in Coconut source)
                        base_speed = _coconut_match_set_name_base_speed  #106 (line in Coconut source)

            if not _coconut_match_check_7:  #106 (line in Coconut source)
                if (not _coconut_match_temp_22) and (_coconut.isinstance(_coconut_match_temp_21, int)):  #106 (line in Coconut source)
                    _coconut_match_check_7 = True  #106 (line in Coconut source)
                if _coconut_match_check_7:  #106 (line in Coconut source)
                    _coconut_match_check_7 = False  #106 (line in Coconut source)
                    if not _coconut_match_check_7:  #106 (line in Coconut source)
                        _coconut_match_set_name_base_speed = _coconut_sentinel  #106 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_21) in _coconut_self_match_types:  #106 (line in Coconut source)
                            _coconut_match_set_name_base_speed = _coconut_match_temp_21  #106 (line in Coconut source)
                            _coconut_match_check_7 = True  #106 (line in Coconut source)
                        if _coconut_match_check_7:  #106 (line in Coconut source)
                            if _coconut_match_set_name_base_speed is not _coconut_sentinel:  #106 (line in Coconut source)
                                base_speed = _coconut_match_set_name_base_speed  #106 (line in Coconut source)

                    if not _coconut_match_check_7:  #106 (line in Coconut source)
                        _coconut_match_set_name_base_speed = _coconut_sentinel  #106 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_21) in _coconut_self_match_types:  #106 (line in Coconut source)
                            _coconut_match_temp_24 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #106 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_24, _coconut.tuple):  #106 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #106 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_24) < 1:  #106 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_24),))  #106 (line in Coconut source)
                            _coconut_match_temp_25 = _coconut.getattr(_coconut_match_temp_21, _coconut_match_temp_24[0], _coconut_sentinel)  #106 (line in Coconut source)
                            if _coconut_match_temp_25 is not _coconut_sentinel:  #106 (line in Coconut source)
                                _coconut_match_set_name_base_speed = _coconut_match_temp_25  #106 (line in Coconut source)
                                _coconut_match_check_7 = True  #106 (line in Coconut source)
                        if _coconut_match_check_7:  #106 (line in Coconut source)
                            if _coconut_match_set_name_base_speed is not _coconut_sentinel:  #106 (line in Coconut source)
                                base_speed = _coconut_match_set_name_base_speed  #106 (line in Coconut source)




        if _coconut_match_check_7:  #106 (line in Coconut source)
            _coconut_match_check_7 = False  #106 (line in Coconut source)
            if not _coconut_match_check_7:  #106 (line in Coconut source)
                _coconut_match_set_name_level = _coconut_sentinel  #106 (line in Coconut source)
                if (_coconut_match_temp_29) and (_coconut.isinstance(_coconut_match_temp_28, int)) and (_coconut.len(_coconut_match_temp_28) >= 1):  #106 (line in Coconut source)
                    _coconut_match_set_name_level = _coconut_match_temp_28[0]  #106 (line in Coconut source)
                    _coconut_match_temp_30 = _coconut.len(_coconut_match_temp_28) <= _coconut.max(1, _coconut.len(_coconut_match_temp_28.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_28, "_coconut_data_defaults", {}) and _coconut_match_temp_28[i] == _coconut.getattr(_coconut_match_temp_28, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_28.__match_args__))) if _coconut.hasattr(_coconut_match_temp_28, "__match_args__") else _coconut.len(_coconut_match_temp_28) == 1  # type: ignore  #106 (line in Coconut source)
                    if _coconut_match_temp_30:  #106 (line in Coconut source)
                        _coconut_match_check_7 = True  #106 (line in Coconut source)
                if _coconut_match_check_7:  #106 (line in Coconut source)
                    if _coconut_match_set_name_level is not _coconut_sentinel:  #106 (line in Coconut source)
                        level = _coconut_match_set_name_level  #106 (line in Coconut source)

            if not _coconut_match_check_7:  #106 (line in Coconut source)
                if (not _coconut_match_temp_29) and (_coconut.isinstance(_coconut_match_temp_28, int)):  #106 (line in Coconut source)
                    _coconut_match_check_7 = True  #106 (line in Coconut source)
                if _coconut_match_check_7:  #106 (line in Coconut source)
                    _coconut_match_check_7 = False  #106 (line in Coconut source)
                    if not _coconut_match_check_7:  #106 (line in Coconut source)
                        _coconut_match_set_name_level = _coconut_sentinel  #106 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_28) in _coconut_self_match_types:  #106 (line in Coconut source)
                            _coconut_match_set_name_level = _coconut_match_temp_28  #106 (line in Coconut source)
                            _coconut_match_check_7 = True  #106 (line in Coconut source)
                        if _coconut_match_check_7:  #106 (line in Coconut source)
                            if _coconut_match_set_name_level is not _coconut_sentinel:  #106 (line in Coconut source)
                                level = _coconut_match_set_name_level  #106 (line in Coconut source)

                    if not _coconut_match_check_7:  #106 (line in Coconut source)
                        _coconut_match_set_name_level = _coconut_sentinel  #106 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_28) in _coconut_self_match_types:  #106 (line in Coconut source)
                            _coconut_match_temp_31 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #106 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_31, _coconut.tuple):  #106 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #106 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_31) < 1:  #106 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_31),))  #106 (line in Coconut source)
                            _coconut_match_temp_32 = _coconut.getattr(_coconut_match_temp_28, _coconut_match_temp_31[0], _coconut_sentinel)  #106 (line in Coconut source)
                            if _coconut_match_temp_32 is not _coconut_sentinel:  #106 (line in Coconut source)
                                _coconut_match_set_name_level = _coconut_match_temp_32  #106 (line in Coconut source)
                                _coconut_match_check_7 = True  #106 (line in Coconut source)
                        if _coconut_match_check_7:  #106 (line in Coconut source)
                            if _coconut_match_set_name_level is not _coconut_sentinel:  #106 (line in Coconut source)
                                level = _coconut_match_set_name_level  #106 (line in Coconut source)




        if _coconut_match_check_7:  #106 (line in Coconut source)
            if _coconut_match_set_name_speed_stage is not _coconut_sentinel:  #106 (line in Coconut source)
                speed_stage = _coconut_match_set_name_speed_stage  #106 (line in Coconut source)
            if _coconut_match_set_name_speed_nature is not _coconut_sentinel:  #106 (line in Coconut source)
                speed_nature = _coconut_match_set_name_speed_nature  #106 (line in Coconut source)

        if not _coconut_match_check_7:  #106 (line in Coconut source)
            raise _coconut_FunctionMatchError('data PokemonSpeed(', _coconut_match_args)  #106 (line in Coconut source)

        return _coconut.tuple.__new__(_coconut_cls, (name, base_speed, speed_stage, speed_nature, level))  #106 (line in Coconut source)
    def __str__(self):  #106 (line in Coconut source)
        return self.speed_stage.modifier_str() + self.name + str(self.speed_nature)  #113 (line in Coconut source)

    @property  #114 (line in Coconut source)
    @_coconut_tco  #115 (line in Coconut source)
    def stat(self):  #115 (line in Coconut source)
        return _coconut_tail_call(calc_stat, self.base_speed, self.speed_stage, self.speed_nature, self.level)  #115 (line in Coconut source)


_coconut_call_set_names(PokemonSpeed)  #117 (line in Coconut source)
def get_all_speeds(url, level):  #117 (line in Coconut source)
    for mon, stage, nature in cartesian_product(get_mons(url), important_stages, important_natures):  #118 (line in Coconut source)
        yield PokemonSpeed(mon.name, mon.base_stats.speed, stage, nature, level)  #123 (line in Coconut source)



def get_outspeed_benchmarks(url, level):  #126 (line in Coconut source)
    outspeed_benchmarks = defaultdict(_coconut_partial(defaultdict, list))  # type: dict[int, dict[Stage, list[PokemonSpeed]]]  #127 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #127 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #127 (line in Coconut source)
    __annotations__["outspeed_benchmarks"] = 'dict[int, dict[Stage, list[PokemonSpeed]]]'  #127 (line in Coconut source)
    speeds = set(get_all_speeds(url, level))  #128 (line in Coconut source)
    for stage in important_stages:  #129 (line in Coconut source)
        base_speed = 1  #130 (line in Coconut source)
        unused_speeds = speeds.copy()  #131 (line in Coconut source)
        while unused_speeds:  #132 (line in Coconut source)
            check_speed = (stage.apply)(base_speed)  #133 (line in Coconut source)
            for pokemon_speed in tuple(unused_speeds):  #134 (line in Coconut source)
                if check_speed > pokemon_speed.stat:  #135 (line in Coconut source)
                    outspeed_benchmarks[base_speed][stage].append(pokemon_speed)  #136 (line in Coconut source)
                    unused_speeds.remove(pokemon_speed)  #137 (line in Coconut source)
            base_speed += 1  #138 (line in Coconut source)
    return outspeed_benchmarks  #139 (line in Coconut source)



def write_csv(filename, url, level):  #142 (line in Coconut source)
    outspeed_benchmarks = get_outspeed_benchmarks(url, level)  #143 (line in Coconut source)
    with open(filename, "w", newline="") as csvfile:  #144 (line in Coconut source)
        writer = csv.writer(csvfile)  #145 (line in Coconut source)
        writer.writerow(["Speed: \\ Stage:",] + [str(stage) for stage in important_stages])  #146 (line in Coconut source)
        for base_speed in (sorted)(outspeed_benchmarks, reverse=True):  #147 (line in Coconut source)
            row = [base_speed,]  #148 (line in Coconut source)
            for stage in important_stages:  #149 (line in Coconut source)
                pokemon_speeds = outspeed_benchmarks[base_speed][stage]  #150 (line in Coconut source)
                row.append((", ".join)((map)(str, pokemon_speeds)))  #151 (line in Coconut source)
            writer.writerow(row)  #156 (line in Coconut source)



def main(*, out="./outspeed_benchmarks.csv", url="https://www.pikalytics.com", level=50,):  #159 (line in Coconut source)
    """Write Pokemon speed tier data in csv format.

    :param out: The csv file to write the speed tier data to.
    :param url: The Pikalytics url to get Pokemon from.
    :param level: The level of the Pokemon to compute speeds at.
    """  #170 (line in Coconut source)
    write_csv(out, url, level)  #171 (line in Coconut source)



run_main = _coconut_partial(run, main)  #174 (line in Coconut source)
