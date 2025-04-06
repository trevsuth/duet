import argparse


def run(program_lines, trace=False):
    registers = [0] * 9

    def get_val(token):
        if token.isdigit():
            return int(token)
        raise ValueError(f"Invalid token: {token}")

    result = 0

    for line in program_lines:
        line = line.strip()
        if not line or line.startswith("<"):
            continue

        tokens = line.split()
        if len(tokens) < 3:
            continue

        a, b, c = tokens

        if b == "|":
            val = get_val(a)
        elif b == ".":
            reg = get_val(a)
            val = registers[reg]
        elif b == ":":
            reg = get_val(a)
            val = int(input(f"Enter value for register {reg}: "))
        else:
            raise ValueError(f"Unknown middle token: {b}")

        if c == "=":
            result = val
        elif c == "+":
            result += val
        elif c == "-":
            result -= val
        elif c == "-":
            result -= val
        elif c == "*":
            result *= val
        elif c == "/":
            result //= val
        elif c == "%":
            result %= val
        elif c == ">":
            if b == ":":
                registers[reg] = val
            elif b in ("|", "."):
                registers[get_val(a)] = result
            if get_val(a) == 0:
                print(f"Output: {registers[0]}")
        else:
            raise ValueError(f"Unknown operator: {c}")

        if trace:
            print(f"TRACE {registers}")


def main():
    parser = argparse.ArgumentParser(description="Intrepreter for Duet Esolang")
    parser.add_argument("file", help="Path to the source code file")
    parser.add_argument(
        "--trace",
        action="store_true",
        help="show register trace after each instruction",
    )

    args = parser.parse_args()

    with open(args.file) as f:
        lines = f.readlines()

    run(lines, trace=args.trace)


if __name__ == "__main__":
    main()
