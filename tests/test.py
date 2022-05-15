import unittest
import parser


class ParserGetTest(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()

    def test_get_basic(self):
        output = self.parser.parse_command("get sword")
        self.assertEqual(output.get('get'), "sword")

    def test_take(self):
        output = self.parser.parse_command("take boots")
        self.assertEqual(output.get('get'), "boots")

    def test_acquire(self):
        output = self.parser.parse_command("acquire boots")
        self.assertEqual(output.get('get'), "boots")

    def test_get_double(self):
        output = self.parser.parse_command("get red boots")
        self.assertEqual(output.get('get'), "red boots")

    def test_get_triple(self):
        output = self.parser.parse_command("get blue suede shoes")
        self.assertEqual(output.get('get'), "blue suede shoes")


class ParserDropTest(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()

    def test_drop(self):
        output = self.parser.parse_command("drop boots")
        self.assertEqual(output.get('drop'), "boots")


class ParserMoveTest(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()

    def test_move_n(self):
        output = self.parser.parse_command("go n")
        self.assertEqual(output.get('move'), "n")

    def test_move_s(self):
        output = self.parser.parse_command("go s")
        self.assertEqual(output.get('move'), "s")

    def test_move_e(self):
        output = self.parser.parse_command("go e")
        self.assertEqual(output.get('move'), "e")

    def test_move_w(self):
        output = self.parser.parse_command("go w")
        self.assertEqual(output.get('move'), "w")

    def test_move_north(self):
        output = self.parser.parse_command("go north")
        self.assertEqual(output.get('move'), "n")

    def test_move_south(self):
        output = self.parser.parse_command("go south")
        self.assertEqual(output.get('move'), "s")

    def test_move_west(self):
        output = self.parser.parse_command("go west")
        self.assertEqual(output.get('move'), "w")

    def test_move_east(self):
        output = self.parser.parse_command("go east")
        self.assertEqual(output.get('move'), "e")


class ParserExamineTest(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()

    def test_examine(self):
        output = self.parser.parse_command("examine green wine bottle")
        self.assertEqual(output.get('examine'), "green wine bottle")

    def test_inspect(self):
        output = self.parser.parse_command("inspect green wine bottle")
        self.assertEqual(output.get('examine'), "green wine bottle")

    def test_check(self):
        output = self.parser.parse_command("check ancient whalebone talisman")
        self.assertEqual(output.get('examine'), "ancient whalebone talisman")

    def test_look(self):
        output = self.parser.parse_command("look at ancient turtle pope")
        self.assertEqual(output.get('examine'), "ancient turtle pope")


class LookTest(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()

    def test_look(self):
        output = self.parser.parse_command("look")
        self.assertEqual(output.get('look'), "")

    def test_l(self):
        output = self.parser.parse_command("l")
        self.assertEqual(output.get('look'), "")

    def test_look_around(self):
        output = self.parser.parse_command("look around")
        self.assertEqual(output.get('look'), "")


class UseTest(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()

    def test_use_on_subject(self):
        output = self.parser.parse_command("use fork on salad")
        self.assertEqual(output.get('use'), {'fork': 'salad'})

    def test_many_words(self):
        output = self.parser.parse_command("use black key on evil doorway")
        self.assertEqual(output.get('use'), {'black key': 'evil doorway'})

class ActivateTest(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()

    def test_basic_activate(self):
        output = self.parser.parse_command("activate radio")
        self.assertEqual(output.get('activate'), "radio")

    def test_alt_activate(self):
        output = self.parser.parse_command("turn on radio")
        self.assertEqual(output.get('activate'), "radio")

    def test_activate_multi(self):
        output = self.parser.parse_command("activate ancient wooden radio")
        self.assertEqual(output.get('activate'), "ancient wooden radio")

    def test_alternate_multi_activate(self):
        output = self.parser.parse_command("turn on devilishly handsome woman")
        self.assertEqual(output.get('activate'), "devilishly handsome woman")

if __name__ == '__main__':
    unittest.main()
