from plox.token_types import Token
from dataclasses import dataclass
from typing import Any


class Expr:
    pass


@dataclass
class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr


@dataclass
class Call(Expr):
    callee: Expr
    paren: Token
    args: [Expr]


@dataclass
class Logical(Expr):
    left: Expr
    operator: Token
    right: Expr


@dataclass
class Unary(Expr):
    operator: Token
    right: Expr


@dataclass
class Grouping(Expr):
    expression: Expr


@dataclass
class Literal(Expr):
    value: Any


@dataclass
class Variable(Expr):
    name: Token


@dataclass
class Assignment(Expr):
    name: Token
    value: Expr
