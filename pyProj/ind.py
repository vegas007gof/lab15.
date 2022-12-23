#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decorator(func):
    def decorator_inside(*args):
        data = func(*args)
        return dict(zip(*data))

    return decorator_inside

@decorator
def listing(A, B):
    return A.split(), B.split()


if __name__ == '__main__':
    First = input("Введите первую строку: ")
    Second = input("Введите вторую строку: ")
    print(listing(First, Second))