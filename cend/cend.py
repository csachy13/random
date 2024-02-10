from sys import argv
from sys import exit as out
from os import system
from os.path import dirname
from time import sleep
from termcolor import cprint, colored
from tabulate import tabulate
from random import randint


def err(message):
    cprint(f"cend1: ", attrs=["bold"], end="")
    cprint("error: ", "red", attrs=["bold"], end="")
    print(message)
    out(-1)


class Program:
    def suppressErrors(self) -> None:
        self.suppressError = int(1)

    def err(self, message, lines=0) -> None:
        if not bool(self.suppressError):
            cprint(f"cend1", attrs=["bold"], end="")
            cprint(f"[line:{lines}]: ", "grey", end="")
            cprint("error: ", "red", attrs=["bold"], end="")
            print(message)
            out(1)
        else:
            pass

    def toInt(self, x):
        try:
            self.setd(x, int(self.variables[x][1]))
        except ValueError:
            self.err("Value could not be converted into an int.", self.lines)

    def __init__(self):
        self.variables = {
            'TRUE': (int, 1),
            'FALSE': (int, 0),
        }
        self.functions = {}
        self.suppressError = int(0)
        self.QUOTE = '"'
        self.COMMANDS = {
            ":println": lambda *args: (
                print(" ".join(args)[1:])
                if args[0][0] == "_"
                else print(
                    colored(
                        f"{args[0]}: <"
                        + (self.variables[args[0]][1]).__class__.__name__
                        + ">",
                        "grey",
                    ),
                    self.variables[args[0]][1],
                )
            ),
            ":print": lambda *args: (
                print(" ".join(args)[1:], end=" ")
                if args[0][0] == "_"
                else print(
                    colored(
                        f"{args[0]}: <"
                        + (self.variables[args[0]][1]).__class__.__name__
                        + ">",
                        "grey",
                    ),
                    self.variables[args[0]][1],
                    end=" ",
                )
            ),
            ":rawprint": lambda *args: (
                print(" ".join(args)[1:], end=" ")
                if args[0][0] == "_"
                else print(self.variables[args[0]][1], end=" ")
            ),
            ":rawprintln": lambda *args: (
                print(" ".join(*args)[1:], end="\n")
                if args[0][0] == "_"
                else print(self.variables[args[0]][1], end="\n")
            ),
            ":rawrawprint": lambda *args: (
                print("".join(args)[1:], end="")
                if args[0][0] == "_"
                else print(self.variables[args[0]][1], end="")
            ),
            ":set": lambda *args: self.setd(args[0], " ".join(args[1:])),
            ":setadd": lambda x, y, z, mode=int, *args: (
                self.setd(x, mode(y[1:]) + mode(z[1:]))
                if (y[0] == "_" and z[0] == "_")
                else self.setd(x, self.variables[y][1] + self.variables[z][1])
            ),
            ":setminus": lambda x, y, z, mode=int, *args: (
                self.setd(x, mode(y[1:]) - mode(z[1:]))
                if (y[0] == "_" and z[0] == "_")
                else self.setd(x, self.variables[y][1] - self.variables[z][1])
            ),
            ":setdiv": lambda x, y, z, mode=int, *args: (
                self.setd(x, mode(y[1:]) // mode(z[1:]))
                if (y[0] == "_" and z[0] == "_")
                else self.setd(x, self.variables[y][1] // self.variables[z][1])
            ),
            ":setmult": lambda x, y, z, mode=int, *args: (
                self.setd(x, mode(y[1:]) * mode(z[1:]))
                if (y[0] == "_" and z[0] == "_")
                else self.setd(x, self.variables[y][1] * self.variables[z][1])
            ),
            ":setpow": lambda x, y, z, mode=int, *args: (
                self.setd(x, mode(y[1:]) ** mode(z[1:]))
                if (y[0] == "_" and z[0] == "_")
                else self.setd(x, self.variables[y][1] ** self.variables[z][1])
            ),
            ":setnot": lambda x, y, *args: self.setd(x, abs(self.variables[y][1] - 1)),
            ":setstr": lambda x, y, *args: self.setd(x, y, typse=str),  # type: ignore
            ":setgreater": lambda x, y, z: (
                self.setd(x, y, int(y > z))
                if y[0] == "_"
                else self.setd(x, int(self.variables[y] > self.variables[z]))
            ),
            ":setequals": lambda x, y, z: (
                self.setd(x, y, int(y == z))
                if y[0] == "_"
                else self.setd(x, int(self.variables[y] == self.variables[z]))
            ),
            ":settype": lambda x, y: self.setd(
                x, self.variables[y][1].__class__.__name__, typstr=True
            ),
            ":if": lambda x, *args: (
                self.run(" ".join(args), countLines=False)
                if (self.variables[x][1] == 1)
                else 0
            ),
            ":repeat": lambda x, *args: self.reprun(" ".join(args), int(x)),
            # 'SETINT': lambda x, y, *args: self.setd(x, y),
            ":setconcat": lambda x, y, z, *args: self.setd(
                x, self.variables[y][1] + self.variables[z][1], typstr=True
            ),
            ":copyvar": lambda x, y: self.setd(x, self.variables[y][1]),
            ":content": lambda file: print(self.content(file)),
            ":display": lambda *args: print(self.variables),
            ":rand100": lambda *args: self.setd("rand100", randint(0, 100)),
            ":rand1000": lambda *args: self.setd("rand1000", randint(0, 1000)),
            ":rand10": lambda *args: self.setd("rand10", randint(0, 10)),
            ":clear": lambda *args: system("clear"),
            ":getarguments": lambda *args: self.setd("args", sys.argv[2:] + ["0"] * 20, typse=list),  # type: ignore
            ":toint": self.toInt,
            ":end": lambda *args: out(0),
            ":wait": lambda t, *args: sleep(int(t) / 1000),
            ":fun": self.addFunction,
            ":displayfn": lambda *args: print(self.functions),
            ":suppress": self.suppressErrors,
            ":keys": lambda *args: print(
                tabulate(
                    [self.COMMANDN[i : i + 4] for i in range(0, len(self.COMMANDN), 4)]
                )
            ),
            ":incr": lambda x, *args: self.setd(x, self.variables[x][1] + 1),
            ":zero": lambda x, *args: self.setd(x, 0),
            ":err": lambda *args: self.err(' '.join(args), self.lines)
        }
        self.COMMANDN = list(self.COMMANDS.keys())
        self.lines = 0

    def addFunction(self, name, *args):
        if name in self.COMMANDN:
            self.err(
                f'function {colored(self.QUOTE + name + self.QUOTE, "green")} is already a command',
                self.lines,
            )
        else:
            self.functions[name] = " ".join(args)

    def reprun(self, code, times):
        for i in range(times):
            self.run(code, countLines=False)

    def setd(self, x, y, *args, typse=int, typstr=False):
        if typstr:
            typse = str
        # cprint(f'SETD FUNC: args[x={x} y={y} typse={typse}]','grey')
        if type(y) == str and ":" in y:
            y = y.split(":")
            y[0] = y[0][1:]
            # cprint(f'SETD FUNCY: args[x={x} y={y} typse={typse}]','grey')
            # cprint(y[0], 'grey')
            # cprint(f'SETD FUNCY2: args[x={x} y={y} typse={typse}], {self.variables[ y[0] ] [1] [int(y[1])]}','grey')
            # cprint(f'{self.variables[y[0]][1][int(y[1])]}', 'red')
            # self.setd(x, self.variables[y[0]][1][int(y[1])], str)
            test = self.variables[y[0]][1][int(y[1])]
            self.variables[x] = (str, test)
            # print(self.variables[y[0]][1][int(y[1])])
            # print('Hello')
            return
        if type(y) == str:
            if "$" in y:
                self.variables[x] = (str, input(y[1:] + "".join(args)))
                return
        try:
            if y[0] + y[1] == "__":
                typse = str
                y = y[2:]
        except:
            pass
        if typse == int:
            try:
                y = int(y)
            except:
                self.err("Not an int", self.lines)
                return
        self.variables[x] = (typse, y)

    def content(self, file):
        with open(file, "r") as a:
            return a.read()

    def run(self, codeText, countLines=True):
        self.codeParts = [item.strip() for item in codeText.split(" ")]
        self.lines += int(countLines)
        if self.codeParts[0].strip() == "":
            return
        if (
            self.codeParts[0] not in self.COMMANDN
            and self.codeParts[0] not in self.functions
        ):
            if self.codeParts[0][0] == "#":
                if self.codeParts[0] == "#module":
                    if len(self.codeParts) == 1:
                        self.err(f"No file given as module", self.lines)
                    file = self.codeParts[1]
                    try:
                        runFile = open(file, "r")
                    except:
                        if file[0] == "<" and file[-1] == ">":
                            try:
                                runFile = open(
                                    dirname(__file__) + "/cendStandard/" + file[1:-1]
                                )
                            except:
                                self.err(
                                    f"File not found as module in standard library: {file}",
                                    self.lines,
                                )
                        else:
                            self.err(f"File not found as module: {file}", self.lines)

                    fileLines: list[str] = runFile.read().split("\n")
                    runFile.close()
                    for line in fileLines:
                        self.run(line, countLines=False)
                return
            self.err(
                f"Not a real command: {colored(self.codeParts[0], 'green')}", self.lines
            )
            return
        else:
            try:
                if self.codeParts[0] in self.COMMANDN:
                    self.COMMANDS[self.codeParts[0]](*self.codeParts[1:])
                else:
                    func = self.functions[self.codeParts[0]]
                    func = func.split("|")
                    for code in func:
                        if code.strip() != None:
                            code: str = code.strip()
                            self.run(code, countLines=False)
            except KeyboardInterrupt:
                self.err("KeyboardInterrupt", self.lines)


if __name__ == "__main__":
    if len(argv) == 1:
        err("No input files")
        out(1)
    if len(argv) == 2 and argv[1] == '-v':
        print('')
    arguments: list[str] = argv[1:]
    try:
        runFile = open(arguments[0], "r")
    except:
        err("File not found")
        out(1)

    fileLines: list[str] = runFile.read().split("\n")
    fileLines = [item.strip() for item in fileLines]
    runFile.close()
    if fileLines[0].strip() != "#develop":
        cprint(f"Running {arguments[0]}...", "blue", attrs=["bold"])
    else:
        fileLines = fileLines[1:]
    program = Program()
    for line in fileLines:
        program.run(line)
    runFile.close()
