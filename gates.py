#!/usr/bin/python
#commad line -> python gates.py --nand 1 0
#commad line -> python gates.py --nor 1 0

import click
@click.command()
@click.option('--nand', nargs=2, type=bool)
@click.option('--nor', nargs=2, type=bool)
def gates(nand, nor):
    if nand and not nor:
        nAnd = NandGate(nand[0],nand[1]).logic()
        print(nAnd)
    elif nor and not nand:
        nOr = NorGate(nor[0],nor[1]).logic()
        print(nOr)


class Gate(object):
    def __init__(self, *args):
        self.input = args
        self.output = None

    def logic(self):
        raise NotImplementedError

    def output(self):
        return self.output


class AndGate(Gate):
    def logic(self):
        self.output = self.input[0] and self.input[1]
        return self.output


class OrGate(Gate):
    def logic(self):
        self.output = self.input[0] or self.input[1]
        return self.output


class NotGate(Gate):
    def logic(self):
        self.output = not self.input[0]
        return self.output


class NandGate(AndGate, NotGate):
    def logic(self):
        andResult = super(NandGate, self).logic()
        NotGate.__init__(self, andResult)
        self.output = NotGate.logic(self)
        return self.output



class NorGate(OrGate, NotGate):
    def logic(self):
        orResult = super(NorGate, self).logic()
        NotGate.__init__(self, orResult)
        self.output = NotGate.logic(self)
        return self.output


if __name__ == '__main__':
    gates()

			
