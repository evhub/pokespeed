#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xe410f685

# Compiled with Coconut version 3.0.4-post_dev17

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.0.4-post_dev17', '', True)
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and str('__coconut_cache__') in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != str('__coconut_cache__'):
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


get_entries = (_coconut_base_compose(requests.get, (_coconut.operator.attrgetter("text"), 0, False), (_coconut_complex_partial(BeautifulSoup, {1: "html.parser"}, 2, ()), 0, False), (_coconut.operator.attrgetter("body"), 0, False), (_coconut.operator.methodcaller("find_all", class_="pokedex_entry"), 0, False)))  #12 (line in Coconut source)


name_formatters = (ident, "{}-incarnate".format, "{}-single-strike".format, _coconut.operator.methodcaller("replace", "-f", "-female"), _coconut.operator.methodcaller("replace", "-m", "-male"), _coconut_base_compose(_coconut.operator.methodcaller("split", "-", 1), (_coconut.operator.itemgetter((0)), 0, False)))  #21 (line in Coconut source)

def get_mons(url):  #30 (line in Coconut source)
    for entry in tqdm(get_entries(url)):  #31 (line in Coconut source)
        name = ((((urllib.parse.unquote)((entry).get("data-name"))).replace(" ", "-")).lower())  #32 (line in Coconut source)
        for formatter in name_formatters:  #39 (line in Coconut source)
            formatted_name = formatter(name)  #40 (line in Coconut source)
            try:  #41 (line in Coconut source)
                yield pypokedex.get(name=formatted_name)  #42 (line in Coconut source)
            except pypokedex.exceptions.PyPokedexHTTPError:  #43 (line in Coconut source)
                pass  #44 (line in Coconut source)
            else:  #45 (line in Coconut source)
                break  #46 (line in Coconut source)
        else:  #47 (line in Coconut source)
            warn("failed to find pokemon {_coconut_format_0}".format(_coconut_format_0=(name)))  #48 (line in Coconut source)



class Nature(_coconut.collections.namedtuple("Nature", ('multiplier', 'identifier')), _coconut.object):  #51 (line in Coconut source)
    __slots__ = ()  #51 (line in Coconut source)
    _coconut_is_data = True  #51 (line in Coconut source)
    __match_args__ = ('multiplier', 'identifier')  #51 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #51 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #51 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #51 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #51 (line in Coconut source)
    def __eq__(self, other):  #51 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #51 (line in Coconut source)
    def __hash__(self):  #51 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #51 (line in Coconut source)
    @_coconut_tco  #51 (line in Coconut source)
    def apply(self, stat):  #51 (line in Coconut source)
        return _coconut_tail_call(int, stat * self.multiplier)  #52 (line in Coconut source)

    def __str__(self):  #53 (line in Coconut source)
        return self.identifier  #53 (line in Coconut source)


_coconut_call_set_names(Nature)  #55 (line in Coconut source)
Helpful = Nature(1.1, "+")  #55 (line in Coconut source)
Harmful = Nature(0.9, "-")  #56 (line in Coconut source)
Neutral = Nature(1, "=")  #57 (line in Coconut source)

important_natures = (Helpful, Neutral)  #59 (line in Coconut source)


class Stage(_coconut.collections.namedtuple("Stage", ('stat_stage', 'stat_modifier')), _coconut.object):  #65 (line in Coconut source)
    __slots__ = ()  #65 (line in Coconut source)
    _coconut_is_data = True  #65 (line in Coconut source)
    __match_args__ = ('stat_stage', 'stat_modifier')  #65 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #65 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #65 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #65 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #65 (line in Coconut source)
    def __eq__(self, other):  #65 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #65 (line in Coconut source)
    def __hash__(self):  #65 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #65 (line in Coconut source)
    def __new__(_coconut_cls, _coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #65 (line in Coconut source)
        _coconut_match_check_6 = False  #65 (line in Coconut source)
        _coconut_match_set_name_stat_modifier = _coconut_sentinel  #65 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #65 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #65 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #65 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "stat_stage" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat_modifier" in _coconut_match_kwargs)) <= 1):  #65 (line in Coconut source)
            _coconut_match_temp_10 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("stat_stage")  #65 (line in Coconut source)
            _coconut_match_temp_15 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat_modifier") if "stat_modifier" in _coconut_match_kwargs else 1  #65 (line in Coconut source)
            _coconut_match_temp_11 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #65 (line in Coconut source)
            _coconut_match_set_name_stat_modifier = _coconut_match_temp_15  #65 (line in Coconut source)
            if not _coconut_match_kwargs:  #65 (line in Coconut source)
                _coconut_match_check_6 = True  #65 (line in Coconut source)
        if _coconut_match_check_6:  #65 (line in Coconut source)
            _coconut_match_check_6 = False  #65 (line in Coconut source)
            if not _coconut_match_check_6:  #65 (line in Coconut source)
                _coconut_match_set_name_stat_stage = _coconut_sentinel  #65 (line in Coconut source)
                if (_coconut_match_temp_11) and (_coconut.isinstance(_coconut_match_temp_10, int)) and (_coconut.len(_coconut_match_temp_10) >= 1):  #65 (line in Coconut source)
                    _coconut_match_set_name_stat_stage = _coconut_match_temp_10[0]  #65 (line in Coconut source)
                    _coconut_match_temp_12 = _coconut.len(_coconut_match_temp_10) <= _coconut.max(1, _coconut.len(_coconut_match_temp_10.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_10, "_coconut_data_defaults", {}) and _coconut_match_temp_10[i] == _coconut.getattr(_coconut_match_temp_10, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_10.__match_args__))) if _coconut.hasattr(_coconut_match_temp_10, "__match_args__") else _coconut.len(_coconut_match_temp_10) == 1  # type: ignore  #65 (line in Coconut source)
                    if _coconut_match_temp_12:  #65 (line in Coconut source)
                        _coconut_match_check_6 = True  #65 (line in Coconut source)
                if _coconut_match_check_6:  #65 (line in Coconut source)
                    if _coconut_match_set_name_stat_stage is not _coconut_sentinel:  #65 (line in Coconut source)
                        stat_stage = _coconut_match_set_name_stat_stage  #65 (line in Coconut source)

            if not _coconut_match_check_6:  #65 (line in Coconut source)
                if (not _coconut_match_temp_11) and (_coconut.isinstance(_coconut_match_temp_10, int)):  #65 (line in Coconut source)
                    _coconut_match_check_6 = True  #65 (line in Coconut source)
                if _coconut_match_check_6:  #65 (line in Coconut source)
                    _coconut_match_check_6 = False  #65 (line in Coconut source)
                    if not _coconut_match_check_6:  #65 (line in Coconut source)
                        _coconut_match_set_name_stat_stage = _coconut_sentinel  #65 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_10) in _coconut_self_match_types:  #65 (line in Coconut source)
                            _coconut_match_set_name_stat_stage = _coconut_match_temp_10  #65 (line in Coconut source)
                            _coconut_match_check_6 = True  #65 (line in Coconut source)
                        if _coconut_match_check_6:  #65 (line in Coconut source)
                            if _coconut_match_set_name_stat_stage is not _coconut_sentinel:  #65 (line in Coconut source)
                                stat_stage = _coconut_match_set_name_stat_stage  #65 (line in Coconut source)

                    if not _coconut_match_check_6:  #65 (line in Coconut source)
                        _coconut_match_set_name_stat_stage = _coconut_sentinel  #65 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_10) in _coconut_self_match_types:  #65 (line in Coconut source)
                            _coconut_match_temp_13 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #65 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_13, _coconut.tuple):  #65 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #65 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_13) < 1:  #65 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_13),))  #65 (line in Coconut source)
                            _coconut_match_temp_14 = _coconut.getattr(_coconut_match_temp_10, _coconut_match_temp_13[0], _coconut_sentinel)  #65 (line in Coconut source)
                            if _coconut_match_temp_14 is not _coconut_sentinel:  #65 (line in Coconut source)
                                _coconut_match_set_name_stat_stage = _coconut_match_temp_14  #65 (line in Coconut source)
                                _coconut_match_check_6 = True  #65 (line in Coconut source)
                        if _coconut_match_check_6:  #65 (line in Coconut source)
                            if _coconut_match_set_name_stat_stage is not _coconut_sentinel:  #65 (line in Coconut source)
                                stat_stage = _coconut_match_set_name_stat_stage  #65 (line in Coconut source)




        if _coconut_match_check_6:  #65 (line in Coconut source)
            if _coconut_match_set_name_stat_modifier is not _coconut_sentinel:  #65 (line in Coconut source)
                stat_modifier = _coconut_match_set_name_stat_modifier  #65 (line in Coconut source)

        if not _coconut_match_check_6:  #65 (line in Coconut source)
            raise _coconut_FunctionMatchError('data Stage(int(stat_stage), stat_modifier=1):', _coconut_match_args)  #65 (line in Coconut source)

        return _coconut.tuple.__new__(_coconut_cls, (stat_stage, stat_modifier))  #65 (line in Coconut source)
    @_coconut_tco  #65 (line in Coconut source)
    @_coconut_mark_as_match  #65 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #65 (line in Coconut source)
        _coconut_match_check_0 = False  #65 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #65 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #65 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #65 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #65 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #65 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #65 (line in Coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #65 (line in Coconut source)
            _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #65 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_0  #65 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_1  #65 (line in Coconut source)
            if not _coconut_match_kwargs:  #65 (line in Coconut source)
                _coconut_match_check_0 = True  #65 (line in Coconut source)
        if _coconut_match_check_0:  #65 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #65 (line in Coconut source)
                self = _coconut_match_set_name_self  #65 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #65 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #65 (line in Coconut source)
        if _coconut_match_check_0 and not (self.stat_modifier != 1):  #65 (line in Coconut source)
            _coconut_match_check_0 = False  #65 (line in Coconut source)
        if not _coconut_match_check_0:  #65 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def apply(self, stat if self.stat_modifier != 1) =', _coconut_match_args)  #65 (line in Coconut source)

        return _coconut_tail_call((int), self._replace(stat_modifier=1).apply(stat) * self.stat_modifier)  #67 (line in Coconut source)

    try:  #68 (line in Coconut source)
        _coconut_addpattern_0 = _coconut_addpattern(apply)  # type: ignore  #68 (line in Coconut source)
    except _coconut.NameError:  #68 (line in Coconut source)
        _coconut_addpattern_0 = lambda f: f  #68 (line in Coconut source)
    @_coconut_addpattern_0  #68 (line in Coconut source)
    @_coconut_mark_as_match  #68 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #68 (line in Coconut source)
        _coconut_match_check_1 = False  #68 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #68 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #68 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #68 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #68 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #68 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #68 (line in Coconut source)
            _coconut_match_temp_2 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #68 (line in Coconut source)
            _coconut_match_temp_3 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #68 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_2  #68 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_3  #68 (line in Coconut source)
            if not _coconut_match_kwargs:  #68 (line in Coconut source)
                _coconut_match_check_1 = True  #68 (line in Coconut source)
        if _coconut_match_check_1:  #68 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #68 (line in Coconut source)
                self = _coconut_match_set_name_self  #68 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #68 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #68 (line in Coconut source)
        if _coconut_match_check_1 and not (self.stat_stage > 0):  #68 (line in Coconut source)
            _coconut_match_check_1 = False  #68 (line in Coconut source)
        if not _coconut_match_check_1:  #68 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def apply(self, stat if self.stat_stage > 0) =', _coconut_match_args)  #68 (line in Coconut source)

        return stat * (2 + self.stat_stage) // 2  #69 (line in Coconut source)

    try:  #70 (line in Coconut source)
        _coconut_addpattern_1 = _coconut_addpattern(apply)  # type: ignore  #70 (line in Coconut source)
    except _coconut.NameError:  #70 (line in Coconut source)
        _coconut_addpattern_1 = lambda f: f  #70 (line in Coconut source)
    @_coconut_addpattern_1  #70 (line in Coconut source)
    @_coconut_mark_as_match  #70 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #70 (line in Coconut source)
        _coconut_match_check_2 = False  #70 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #70 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #70 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #70 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #70 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #70 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #70 (line in Coconut source)
            _coconut_match_temp_4 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #70 (line in Coconut source)
            _coconut_match_temp_5 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #70 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_4  #70 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_5  #70 (line in Coconut source)
            if not _coconut_match_kwargs:  #70 (line in Coconut source)
                _coconut_match_check_2 = True  #70 (line in Coconut source)
        if _coconut_match_check_2:  #70 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #70 (line in Coconut source)
                self = _coconut_match_set_name_self  #70 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #70 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #70 (line in Coconut source)
        if _coconut_match_check_2 and not (self.stat_stage < 0):  #70 (line in Coconut source)
            _coconut_match_check_2 = False  #70 (line in Coconut source)
        if not _coconut_match_check_2:  #70 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def apply(self, stat if self.stat_stage < 0) =', _coconut_match_args)  #70 (line in Coconut source)

        return stat * 2 // (2 - self.stat_stage)  #71 (line in Coconut source)

    try:  #72 (line in Coconut source)
        _coconut_addpattern_2 = _coconut_addpattern(apply)  # type: ignore  #72 (line in Coconut source)
    except _coconut.NameError:  #72 (line in Coconut source)
        _coconut_addpattern_2 = lambda f: f  #72 (line in Coconut source)
    @_coconut_addpattern_2  #72 (line in Coconut source)
    @_coconut_mark_as_match  #72 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #72 (line in Coconut source)
        _coconut_match_check_3 = False  #72 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #72 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #72 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #72 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #72 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #72 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #72 (line in Coconut source)
            _coconut_match_temp_6 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #72 (line in Coconut source)
            _coconut_match_temp_7 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #72 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_6  #72 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_7  #72 (line in Coconut source)
            if not _coconut_match_kwargs:  #72 (line in Coconut source)
                _coconut_match_check_3 = True  #72 (line in Coconut source)
        if _coconut_match_check_3:  #72 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #72 (line in Coconut source)
                self = _coconut_match_set_name_self  #72 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #72 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #72 (line in Coconut source)
        if _coconut_match_check_3 and not (self.stat_stage == 0):  #72 (line in Coconut source)
            _coconut_match_check_3 = False  #72 (line in Coconut source)
        if not _coconut_match_check_3:  #72 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def apply(self, stat if self.stat_stage == 0) = stat', _coconut_match_args)  #72 (line in Coconut source)

        return stat  #72 (line in Coconut source)


    def __str__(self):  #74 (line in Coconut source)
        return "{_coconut_format_0:+}".format(_coconut_format_0=(self.stat_stage)) + (" x{_coconut_format_0}".format(_coconut_format_0=(self.stat_modifier)) if self.stat_modifier != 1 else "")  #74 (line in Coconut source)


    @_coconut_mark_as_match  #76 (line in Coconut source)
    def modifier_str(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #76 (line in Coconut source)
        _coconut_match_check_4 = False  #76 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #76 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #76 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #76 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #76 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1):  #76 (line in Coconut source)
            _coconut_match_temp_8 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #76 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_8  #76 (line in Coconut source)
            if not _coconut_match_kwargs:  #76 (line in Coconut source)
                _coconut_match_check_4 = True  #76 (line in Coconut source)
        if _coconut_match_check_4:  #76 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #76 (line in Coconut source)
                self = _coconut_match_set_name_self  #76 (line in Coconut source)
        if _coconut_match_check_4 and not (self.stat_stage == 0):  #76 (line in Coconut source)
            _coconut_match_check_4 = False  #76 (line in Coconut source)
        if not _coconut_match_check_4:  #76 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def modifier_str(self if self.stat_stage == 0) = ""', _coconut_match_args)  #76 (line in Coconut source)

        return ""  #76 (line in Coconut source)

    try:  #77 (line in Coconut source)
        _coconut_addpattern_3 = _coconut_addpattern(modifier_str)  # type: ignore  #77 (line in Coconut source)
    except _coconut.NameError:  #77 (line in Coconut source)
        _coconut_addpattern_3 = lambda f: f  #77 (line in Coconut source)
    @_coconut_addpattern_3  #77 (line in Coconut source)
    @_coconut_mark_as_match  #77 (line in Coconut source)
    def modifier_str(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #77 (line in Coconut source)
        _coconut_match_check_5 = False  #77 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #77 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #77 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #77 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #77 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1):  #77 (line in Coconut source)
            _coconut_match_temp_9 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #77 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_9  #77 (line in Coconut source)
            if not _coconut_match_kwargs:  #77 (line in Coconut source)
                _coconut_match_check_5 = True  #77 (line in Coconut source)
        if _coconut_match_check_5:  #77 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #77 (line in Coconut source)
                self = _coconut_match_set_name_self  #77 (line in Coconut source)
        if not _coconut_match_check_5:  #77 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def modifier_str(self) = str(self) + " "', _coconut_match_args)  #77 (line in Coconut source)

        return str(self) + " "  #77 (line in Coconut source)


_coconut_call_set_names(Stage)  #79 (line in Coconut source)
important_stages = (Stage(-2), Stage(-1), Stage(0), Stage(-1, stat_modifier=2), Stage(+1), Stage(+2), Stage(+1, stat_modifier=2))  #79 (line in Coconut source)


@_coconut_tco  #91 (line in Coconut source)
def calc_stat(base, stage=Stage(0), nature=Helpful, ev=252, iv=31, level=50,):  #91 (line in Coconut source)
    return _coconut_tail_call((stage.apply), (nature.apply)(((2 * base) + iv + ev // 4) * level // 100 + 5))  #91 (line in Coconut source)



class PokemonSpeed(_coconut.collections.namedtuple("PokemonSpeed", ('name', 'base_speed', 'speed_stage', 'speed_nature')), _coconut.object):  #105 (line in Coconut source)
    __slots__ = ()  #105 (line in Coconut source)
    _coconut_is_data = True  #105 (line in Coconut source)
    __match_args__ = ('name', 'base_speed', 'speed_stage', 'speed_nature')  #105 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #105 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #105 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #105 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #105 (line in Coconut source)
    def __eq__(self, other):  #105 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #105 (line in Coconut source)
    def __hash__(self):  #105 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #105 (line in Coconut source)
    def __new__(_coconut_cls, _coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #105 (line in Coconut source)
        _coconut_match_check_7 = False  #105 (line in Coconut source)
        _coconut_match_set_name_speed_stage = _coconut_sentinel  #105 (line in Coconut source)
        _coconut_match_set_name_speed_nature = _coconut_sentinel  #105 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #105 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #105 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #105 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 4) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "name" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "base_speed" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "speed_stage" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "speed_nature" in _coconut_match_kwargs)) == 1):  #105 (line in Coconut source)
            _coconut_match_temp_16 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("name")  #105 (line in Coconut source)
            _coconut_match_temp_21 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("base_speed")  #105 (line in Coconut source)
            _coconut_match_temp_26 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("speed_stage")  #105 (line in Coconut source)
            _coconut_match_temp_27 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("speed_nature")  #105 (line in Coconut source)
            if ((isinstance)(_coconut_match_temp_26, Stage)) and ((isinstance)(_coconut_match_temp_27, Nature)):  #105 (line in Coconut source)
                _coconut_match_temp_17 = _coconut.getattr(str, "_coconut_is_data", False) or _coconut.isinstance(str, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in str)  # type: ignore  #105 (line in Coconut source)
                _coconut_match_temp_22 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #105 (line in Coconut source)
                _coconut_match_set_name_speed_stage = _coconut_match_temp_26  #105 (line in Coconut source)
                _coconut_match_set_name_speed_nature = _coconut_match_temp_27  #105 (line in Coconut source)
                if not _coconut_match_kwargs:  #105 (line in Coconut source)
                    _coconut_match_check_7 = True  #105 (line in Coconut source)
        if _coconut_match_check_7:  #105 (line in Coconut source)
            _coconut_match_check_7 = False  #105 (line in Coconut source)
            if not _coconut_match_check_7:  #105 (line in Coconut source)
                _coconut_match_set_name_name = _coconut_sentinel  #105 (line in Coconut source)
                if (_coconut_match_temp_17) and (_coconut.isinstance(_coconut_match_temp_16, str)) and (_coconut.len(_coconut_match_temp_16) >= 1):  #105 (line in Coconut source)
                    _coconut_match_set_name_name = _coconut_match_temp_16[0]  #105 (line in Coconut source)
                    _coconut_match_temp_18 = _coconut.len(_coconut_match_temp_16) <= _coconut.max(1, _coconut.len(_coconut_match_temp_16.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_16, "_coconut_data_defaults", {}) and _coconut_match_temp_16[i] == _coconut.getattr(_coconut_match_temp_16, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_16.__match_args__))) if _coconut.hasattr(_coconut_match_temp_16, "__match_args__") else _coconut.len(_coconut_match_temp_16) == 1  # type: ignore  #105 (line in Coconut source)
                    if _coconut_match_temp_18:  #105 (line in Coconut source)
                        _coconut_match_check_7 = True  #105 (line in Coconut source)
                if _coconut_match_check_7:  #105 (line in Coconut source)
                    if _coconut_match_set_name_name is not _coconut_sentinel:  #105 (line in Coconut source)
                        name = _coconut_match_set_name_name  #105 (line in Coconut source)

            if not _coconut_match_check_7:  #105 (line in Coconut source)
                if (not _coconut_match_temp_17) and (_coconut.isinstance(_coconut_match_temp_16, str)):  #105 (line in Coconut source)
                    _coconut_match_check_7 = True  #105 (line in Coconut source)
                if _coconut_match_check_7:  #105 (line in Coconut source)
                    _coconut_match_check_7 = False  #105 (line in Coconut source)
                    if not _coconut_match_check_7:  #105 (line in Coconut source)
                        _coconut_match_set_name_name = _coconut_sentinel  #105 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_16) in _coconut_self_match_types:  #105 (line in Coconut source)
                            _coconut_match_set_name_name = _coconut_match_temp_16  #105 (line in Coconut source)
                            _coconut_match_check_7 = True  #105 (line in Coconut source)
                        if _coconut_match_check_7:  #105 (line in Coconut source)
                            if _coconut_match_set_name_name is not _coconut_sentinel:  #105 (line in Coconut source)
                                name = _coconut_match_set_name_name  #105 (line in Coconut source)

                    if not _coconut_match_check_7:  #105 (line in Coconut source)
                        _coconut_match_set_name_name = _coconut_sentinel  #105 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_16) in _coconut_self_match_types:  #105 (line in Coconut source)
                            _coconut_match_temp_19 = _coconut.getattr(str, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #105 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_19, _coconut.tuple):  #105 (line in Coconut source)
                                raise _coconut.TypeError("str.__match_args__ must be a tuple")  #105 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_19) < 1:  #105 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'str' only supports %s)" % (_coconut.len(_coconut_match_temp_19),))  #105 (line in Coconut source)
                            _coconut_match_temp_20 = _coconut.getattr(_coconut_match_temp_16, _coconut_match_temp_19[0], _coconut_sentinel)  #105 (line in Coconut source)
                            if _coconut_match_temp_20 is not _coconut_sentinel:  #105 (line in Coconut source)
                                _coconut_match_set_name_name = _coconut_match_temp_20  #105 (line in Coconut source)
                                _coconut_match_check_7 = True  #105 (line in Coconut source)
                        if _coconut_match_check_7:  #105 (line in Coconut source)
                            if _coconut_match_set_name_name is not _coconut_sentinel:  #105 (line in Coconut source)
                                name = _coconut_match_set_name_name  #105 (line in Coconut source)




        if _coconut_match_check_7:  #105 (line in Coconut source)
            _coconut_match_check_7 = False  #105 (line in Coconut source)
            if not _coconut_match_check_7:  #105 (line in Coconut source)
                _coconut_match_set_name_base_speed = _coconut_sentinel  #105 (line in Coconut source)
                if (_coconut_match_temp_22) and (_coconut.isinstance(_coconut_match_temp_21, int)) and (_coconut.len(_coconut_match_temp_21) >= 1):  #105 (line in Coconut source)
                    _coconut_match_set_name_base_speed = _coconut_match_temp_21[0]  #105 (line in Coconut source)
                    _coconut_match_temp_23 = _coconut.len(_coconut_match_temp_21) <= _coconut.max(1, _coconut.len(_coconut_match_temp_21.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_21, "_coconut_data_defaults", {}) and _coconut_match_temp_21[i] == _coconut.getattr(_coconut_match_temp_21, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_21.__match_args__))) if _coconut.hasattr(_coconut_match_temp_21, "__match_args__") else _coconut.len(_coconut_match_temp_21) == 1  # type: ignore  #105 (line in Coconut source)
                    if _coconut_match_temp_23:  #105 (line in Coconut source)
                        _coconut_match_check_7 = True  #105 (line in Coconut source)
                if _coconut_match_check_7:  #105 (line in Coconut source)
                    if _coconut_match_set_name_base_speed is not _coconut_sentinel:  #105 (line in Coconut source)
                        base_speed = _coconut_match_set_name_base_speed  #105 (line in Coconut source)

            if not _coconut_match_check_7:  #105 (line in Coconut source)
                if (not _coconut_match_temp_22) and (_coconut.isinstance(_coconut_match_temp_21, int)):  #105 (line in Coconut source)
                    _coconut_match_check_7 = True  #105 (line in Coconut source)
                if _coconut_match_check_7:  #105 (line in Coconut source)
                    _coconut_match_check_7 = False  #105 (line in Coconut source)
                    if not _coconut_match_check_7:  #105 (line in Coconut source)
                        _coconut_match_set_name_base_speed = _coconut_sentinel  #105 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_21) in _coconut_self_match_types:  #105 (line in Coconut source)
                            _coconut_match_set_name_base_speed = _coconut_match_temp_21  #105 (line in Coconut source)
                            _coconut_match_check_7 = True  #105 (line in Coconut source)
                        if _coconut_match_check_7:  #105 (line in Coconut source)
                            if _coconut_match_set_name_base_speed is not _coconut_sentinel:  #105 (line in Coconut source)
                                base_speed = _coconut_match_set_name_base_speed  #105 (line in Coconut source)

                    if not _coconut_match_check_7:  #105 (line in Coconut source)
                        _coconut_match_set_name_base_speed = _coconut_sentinel  #105 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_21) in _coconut_self_match_types:  #105 (line in Coconut source)
                            _coconut_match_temp_24 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #105 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_24, _coconut.tuple):  #105 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #105 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_24) < 1:  #105 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_24),))  #105 (line in Coconut source)
                            _coconut_match_temp_25 = _coconut.getattr(_coconut_match_temp_21, _coconut_match_temp_24[0], _coconut_sentinel)  #105 (line in Coconut source)
                            if _coconut_match_temp_25 is not _coconut_sentinel:  #105 (line in Coconut source)
                                _coconut_match_set_name_base_speed = _coconut_match_temp_25  #105 (line in Coconut source)
                                _coconut_match_check_7 = True  #105 (line in Coconut source)
                        if _coconut_match_check_7:  #105 (line in Coconut source)
                            if _coconut_match_set_name_base_speed is not _coconut_sentinel:  #105 (line in Coconut source)
                                base_speed = _coconut_match_set_name_base_speed  #105 (line in Coconut source)




        if _coconut_match_check_7:  #105 (line in Coconut source)
            if _coconut_match_set_name_speed_stage is not _coconut_sentinel:  #105 (line in Coconut source)
                speed_stage = _coconut_match_set_name_speed_stage  #105 (line in Coconut source)
            if _coconut_match_set_name_speed_nature is not _coconut_sentinel:  #105 (line in Coconut source)
                speed_nature = _coconut_match_set_name_speed_nature  #105 (line in Coconut source)

        if not _coconut_match_check_7:  #105 (line in Coconut source)
            raise _coconut_FunctionMatchError('data PokemonSpeed(', _coconut_match_args)  #105 (line in Coconut source)

        return _coconut.tuple.__new__(_coconut_cls, (name, base_speed, speed_stage, speed_nature))  #105 (line in Coconut source)
    def __str__(self):  #105 (line in Coconut source)
        return self.speed_stage.modifier_str() + self.name + str(self.speed_nature)  #111 (line in Coconut source)

    @property  #112 (line in Coconut source)
    @_coconut_tco  #113 (line in Coconut source)
    def stat(self):  #113 (line in Coconut source)
        return _coconut_tail_call(calc_stat, self.base_speed, self.speed_stage, self.speed_nature)  #113 (line in Coconut source)


_coconut_call_set_names(PokemonSpeed)  #115 (line in Coconut source)
def get_all_speeds(url):  #115 (line in Coconut source)
    for mon, stage, nature in cartesian_product(get_mons(url), important_stages, important_natures):  #116 (line in Coconut source)
        yield PokemonSpeed(mon.name, mon.base_stats.speed, stage, nature)  #121 (line in Coconut source)



def get_outspeed_benchmarks(url):  #124 (line in Coconut source)
    outspeed_benchmarks = defaultdict(_coconut_partial(defaultdict, list))  # type: dict[int, dict[Stage, list[PokemonSpeed]]]  #125 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #125 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #125 (line in Coconut source)
    __annotations__["outspeed_benchmarks"] = 'dict[int, dict[Stage, list[PokemonSpeed]]]'  #125 (line in Coconut source)
    speeds = set(get_all_speeds(url))  #126 (line in Coconut source)
    for stage in important_stages:  #127 (line in Coconut source)
        base_speed = 1  #128 (line in Coconut source)
        unused_speeds = speeds.copy()  #129 (line in Coconut source)
        while unused_speeds:  #130 (line in Coconut source)
            check_speed = (stage.apply)(base_speed)  #131 (line in Coconut source)
            for pokemon_speed in tuple(unused_speeds):  #132 (line in Coconut source)
                if check_speed > pokemon_speed.stat:  #133 (line in Coconut source)
                    outspeed_benchmarks[base_speed][stage].append(pokemon_speed)  #134 (line in Coconut source)
                    unused_speeds.remove(pokemon_speed)  #135 (line in Coconut source)
            base_speed += 1  #136 (line in Coconut source)
    return outspeed_benchmarks  #137 (line in Coconut source)



def write_csv(filename, url):  #140 (line in Coconut source)
    outspeed_benchmarks = get_outspeed_benchmarks(url)  #141 (line in Coconut source)
    with open(filename, "w", newline="") as csvfile:  #142 (line in Coconut source)
        writer = csv.writer(csvfile)  #143 (line in Coconut source)
        writer.writerow(["Speed: \\ Stage:",] + [str(stage) for stage in important_stages])  #144 (line in Coconut source)
        for base_speed in (sorted)(outspeed_benchmarks, reverse=True):  #145 (line in Coconut source)
            row = [base_speed,]  #146 (line in Coconut source)
            for stage in important_stages:  #147 (line in Coconut source)
                pokemon_speeds = outspeed_benchmarks[base_speed][stage]  #148 (line in Coconut source)
                row.append((", ".join)((map)(str, pokemon_speeds)))  #149 (line in Coconut source)
            writer.writerow(row)  #154 (line in Coconut source)



def main():  #157 (line in Coconut source)
    write_csv("./outspeed_benchmarks.csv", "https://www.pikalytics.com/")  #158 (line in Coconut source)
