from parser import Parser


def main():
    parser = Parser()
    output = parser.parse_command("use fork on salad")
    print(output)



if __name__ == "__main__":
    main()

#     instruction    = receive
#     receive        = get ws nounphrase
#     drop           = "drop" ws nounphrase
#     move           = (go ws)? direction
#     examine        = inspect ws nounphrase
#     look           = observe ws nounphrase
#     use            = "use" ws nounphrase (ws conjunction ws nounphrase)?
#     equip          = "equip" ws nounphrase
#     hide           = "hide" (ws "in" nounphrase)?
#     unlock         = "unlock" ws nounphrase
#     lock           = "lock" ws nounphrase
#     run            = run_synonym
#     run_synonym    = "escape" / "run away" / "run"
#     open           = "open" ws nounphrase
#     close          = "close" / "shut" ws nounphrase
#     get            = "get" / "pick up" / "take" / "acquire"
#     observe        = "observe" / "look around" / "look"
#     inspect        = "inspect" / "examine" / "check" / "look at"
#     go             = ~"go"i
#     direction      = ~"[NSEW]"
#     nounphrase     = ~"[A-Z]+*"
#     ws             = ~"\s*"
#     conjunction    = ~"with" / ~"and" / ~"from" / ~"to"
