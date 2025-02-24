MAIN_X = 380
STARTING_Y = 40


def main():
    with open("ascii.txt", "r") as f:
        lines = f.readlines()
        new_lines = []
        for i, l in enumerate(lines):
            formatting_front = f'<tspan x="{MAIN_X}" y="{STARTING_Y + 20 * (i)}">'
            formatting_back = "</tspan>"
            new_lines.append(formatting_front + l.rstrip() + formatting_back)

    with open("ascii.svg", "w") as f:
        f.write("\n".join(new_lines))


if __name__ == "__main__":
    main()
