import re
import copy
import math


class Parser:
    def __init__(self, stream):
        self.stream = stream
        self.token = stream[0]
        self.index = 0
        self.symbol_table = {}

    def get_next(self, stream):
        if self.index < len(stream)-1:
            self.index += 1
            self.token = copy.deepcopy(stream[self.index])
            return self.token

    # THIS IS PROG

    def prog(self, out):
        out.write("Output from this program:\n")
        print('prog')
        if self.token[0] == 'prog':
            print('prog')
            self.get_next(self.stream)
            if self.token[1] == 'ID':
                print(self.token[0])
                self.get_next(self.stream)
                if self.token[0] == '{':
                    print(self.token[0])
                    self.get_next(self.stream)
                    res = self.sl(self.token, out)
        elif self.token[0] == '{':
            print('{')
            self.get_next(self.stream)
            res = self.sl(self.token, out)

    # THIS IS SL

    def sl(self, token, out):
        print('\t sl')
        res = self.s(token, out)
        while self.token[0] == ';':
            print('\t\t s')
            print('\t\t' + self.token[0])
            self.get_next(self.stream)
            res = self.s(self.token, out)
        print("SL", res)
        return res

    # THIS IS S

    def s(self, token, out):
        print('\t\t s')
        if token[1] == 'ID' and token[0] != 'sin' and token[0] != 'cos' and token[0] != 'tan':
            if token[0] not in self.symbol_table:
                self.symbol_table[token[0]] = 0
                res = 0
            else:
                res = self.symbol_table[token[0]]
            print('\t\t\t', token[0])
            self.get_next(self.stream)
            if self.token[0] == '=':
                print('\t\t\t' + self.token[0])
                res += float(self.expr(self.get_next(self.stream), out))
                self.symbol_table[token[0]] = res
            elif self.token[0] == '+':
                print('\t\t\t' + self.token[0])
                print('\t\t\t expr')
                add = float(self.term(self.get_next(self.stream), out))
                res += add
            elif self.token[0] == '-':
                print('\t\t\t' + self.token[0])
                print('\t\t\t expr')
                sub = float(self.term(self.get_next(self.stream), out))
                res -= sub
            elif self.token[0] == '*':
                print('\t\t\t\t' + self.token[0])
                print('\t\t\t\t term')
                times = float(self.pow(self.get_next(self.stream), out))
                res *= times
            elif self.token[0] == '/':
                print('\t\t\t\t' + self.token[0])
                print('\t\t\t\t term')
                div = float(self.pow(self.get_next(self.stream), out))
                res /= div
            elif self.token[0] == '^':
                print('\t\t\t\t\t' + self.token[0])
                print('\t\t\t\t\t fact')
                pows = float(self.fact(self.get_next(self.stream), out))
                res = res**pows
        else:
            res = float(self.expr(self.token, out))
        out.write(str(res)+'\n')
        return res

    # THIS IS EXPR

    def expr(self, token, out):
        print('\t\t\t expr')
        res = float(self.term(token, out))
        while self.token[0] == '+' or self.token[0] == '-':
            print('\t\t\t\t term')
            print('\t\t\t\t' + self.token[0])
            if self.token[0] == '+':
                add = float(self.term(self.get_next(self.stream), out))
                res += add
            elif self.token[0] == '-':
                sub = float(self.term(self.get_next(self.stream), out))
                res -= sub
        print("expr",res)
        return res

    # THIS IS TERM

    def term(self, token, out):
        print('\t\t\t\t term')
        res = float(self.pow(token, out))
        while self.token[0] == '*' or self.token[0] == '/':
            print('\t\t\t\t\t pow')
            print('\t\t\t\t\t' + self.token[0])
            if self.token[0] == '*':
                times = float(self.pow(self.get_next(self.stream), out))
                res *= times
            elif self.token[0] == '/':
                div = float(self.pow(self.get_next(self.stream), out))
                res /= div
        print("term",res)
        return res

    # THIS IS POW

    def pow(self, token, out):
        print('\t\t\t\t\t pow')
        res = float(self.fact(token, out))
        while self.token[0] == '^':
            print('\t\t\t\t\t\t fact')
            print('\t\t\t\t\t\t' + self.token[0])
            times = float(self.fact(self.get_next(self.stream), out))
            res = res**times
        print("pow",res)
        return res

    # THIS IS FACT

    def fact(self, token, out):
        print('\t\t\t\t\t\t fact')
        if token[1] == 'ID':
            if token[0] == 'sin':
                print('\t\t\t\t\t\t\t ID:' + token[0])
                self.get_next(self.stream)
                if self.token[0] == '(':
                    print('\t\t\t\t\t\t\t SYMBOL:' + self.token[0])
                    self.get_next(self.stream)
                    res = math.sin(self.expr(self.token, out))
                    if self.token[0] == ')':
                        print('\t\t\t\t\t\t\t SYMBOL:' + self.token[0])
                        self.get_next(self.stream)
                        return res
            elif token[0] == 'cos':
                print('\t\t\t\t\t\t\t ID:' + token[0])
                self.get_next(self.stream)
                if self.token[0] == '(':
                    print('\t\t\t\t\t\t\t SYMBOL:' + self.token[0])
                    self.get_next(self.stream)
                    res = math.cos(self.expr(self.token, out))
                    if self.token[0] == ')':
                        print('\t\t\t\t\t\t\t SYMBOL:' + self.token[0])
                        self.get_next(self.stream)
                        return res
            elif token[0] == 'tan':
                print('\t\t\t\t\t\t\t ID:' + token[0])
                self.get_next(self.stream)
                if self.token[0] == '(':
                    print('\t\t\t\t\t\t\t SYMBOL:' + self.token[0])
                    self.get_next(self.stream)
                    res = math.tan(self.expr(self.token, out))
                    if self.token[0] == ')':
                        print('\t\t\t\t\t\t\t SYMBOL:' + self.token[0])
                        self.get_next(self.stream)
                        return res
            else:
                print('\t\t\t\t\t\t\t ID:' + token[0])
                if token[0] in self.symbol_table:
                    res = self.symbol_table[token[0]]
                else:
                    self.symbol_table[token[0]] = 0
                    res = 0
                self.get_next(self.stream)
                return res
        elif token[1] == 'DIGIT':
            print('\t\t\t\t\t\t\t DIGIT:' + token[0])
            self.get_next(self.stream)
            return token[0]
        elif token[1] == 'SYMBOL':
            print('\t\t\t\t\t\t\t SYMBOL:' + token[0])
            if token[0] == '(':
                self.get_next(self.stream)
                res = float(self.expr(self.token, out))
                if self.token[0] == ')':
                    print('\t\t\t\t\t\t\t SYMBOL:' + self.token[0])
                    self.get_next(self.stream)
                    return res
            elif token[0] == '}':
                out.write('-----END-----\n')
                return 0
        else:
            return "ERROR - INVALID TOKEN"


def what_type(token):
    digit = re.compile(r'^[-+]?[0-9]*\.?[0-9]+')
    identifier = re.compile(r'^([a-z]|[A-Z])+[0-9]*')
    symbol = re.compile(r'^[(){}+^\-=*;/]')
    digit_matches = copy.deepcopy(digit.finditer(str(token)))
    identifier_matches = copy.deepcopy(identifier.finditer(str(token)))
    symbol_matches = copy.deepcopy(symbol.finditer(str(token)))
    for match in digit_matches:
        token_stream.append([token, 'DIGIT'])

    for match in identifier_matches:
        token_stream.append([token, 'ID'])

    for match in symbol_matches:
        token_stream.append([token, 'SYMBOL'])


RAWtoken_stream = []
token_stream = []

with open("Sample Data.txt", 'r') as a:
    text = a.read().splitlines()

#Tokens
    # num | ID | symbol
token = re.compile(r'[-+]?[0-9]*\.?[0-9]+|([a-z]|[A-Z])+[0-9]*|[()^{}+\-=*;/]')

realMatches = token.finditer(str(text))

for match in realMatches:
    RAWtoken_stream.append(match.group(0))

while ',' in RAWtoken_stream:
    RAWtoken_stream.remove(',')

for token in RAWtoken_stream:
    what_type(token)

print("These are the tokens I've collected from the RAW data:")
for pair in token_stream:
    print(pair)

P = Parser(token_stream)
with open('output.txt', 'w') as out:
    print("\nThis is the Parse Tree:\n")
    P.prog(out)

print("Symbol Table: \n",P.symbol_table)
