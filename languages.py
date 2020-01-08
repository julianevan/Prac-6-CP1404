from programming_language import ProgrammingLanguage


def main():
    languages_list = []
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages_list.append(ruby)
    languages_list.append(python)
    languages_list.append(visual_basic)
    print(ruby)
    print(python)
    print(visual_basic)
    print("The dynamic languages are:")
    for i in languages_list:
        status = i.is_dynamic()
        if status == "Dynamic":
            print(i.get_name())


if __name__ == '__main__':
    main()