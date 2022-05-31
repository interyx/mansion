from parsimonious import NodeVisitor
from parsimonious.grammar import Grammar


class Parser:
    grammar = Grammar(
        """
        instruction     = receive / drop / inspect / move / look / use / activate
        receive         = get ws nounphrase
        drop            = "drop" ws nounphrase
        inspect         = examine_synonym ws nounphrase
        look            = look_s
        move            = (go ws)? direction
        use             = "use" ws c_nounphrase
        activate        = ("activate" / "turn on") ws item
        look_s          = ~"look( around)?"i / ~"l"i
        examine_synonym = "examine" / "inspect" / "check" / "look at"
        direction       = ~"north"i / ~"south"i / ~"east"i / ~"west"i / ~"[NSEW]"i 
        get             = "get" / "pick up" / "take" / "acquire"
        go              = ~"go"i
        c_nounphrase    = item ws conjunction ws item
        conjunction     = (~"with"i / ~"and"i / ~"from "i / ~"to"i / ~"on"i)
        item            = (noun (ws)?)+
        nounphrase      = noun (ws noun)* 
        noun            = ~"(?!on|with|and|from|to)[A-Za-z]+"i
        ws              = ~"\s*"

    """)

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

    def parse_command(self, command):
        tree = self.grammar.parse(command)
        ev = self.ExprVisitor()
        return ev.visit(tree)

    class ExprVisitor(NodeVisitor):
        def visit_instruction(self, node, visited_children):
            """ Returns the overall output. """
            return visited_children[0]

        def visit_receive(self, node, visited_children):
            """ Visits the Receive node; assembles instruction into key:value pair"""
            instruction, _, noun = visited_children
            return {instruction: noun}

        def visit_get(self, node, visited_children):
            """ Visits the GET node to return the instruction """
            return "get"

        def visit_drop(self, node, visited_children):
            instruction, _, noun = visited_children
            return {"drop": noun}

        def visit_look_s(self, node, visited_children):
            return {"look": ""}

        def visit_move(self, node, visited_children):
            _, direction = visited_children
            return {"move": direction[0]}

        def visit_direction(self, node, visited_children):
            return node.text

        def visit_inspect(self, node, visited_children):
            instruction, _, noun = visited_children
            return {"examine": noun}

        def visit_use(self, node, visited_children):
            _, _, c_nounphrase = visited_children
            return {"use": c_nounphrase}

        def visit_activate(self, node, visited_children):
            _, _, item = visited_children
            return {"activate": item}

        def visit_c_nounphrase(self, node, visited_children):
            item1, _, _, _, item2 = visited_children
            return {item1: item2}

            # if non_empty_string:
            #     return {"use": {noun: subject.text}}
            # else:
            #     return {"use": noun}
        def visit_noun(self, node, visited_children):
            return node.text

        def visit_item(self, node, visited_children):
            """ Items have the form of (noun) (space?),
            somehow this results in a space after every noun.
            This node holds the whole item name (ancient golden sword) versus its children
            which are 'ancient', 'golden', and 'sword' and all the spaces.
            Returns the item name with trailing space removed."""
            return node.text.rstrip()

        def visit_nounphrase(self, node, visited_children):
            """ Visits the NOUNPHRASE node to return the noun/phrase """
            return node.text

        def generic_visit(self, node, visited_children):
            """ At the bottom level, just send the node back. """
            return visited_children or node
