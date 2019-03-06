"""Testing file of the functions in XMLHelper."""

import unittest
from demand_modelling.daily_flow.flow import XMLHelper


class TestXMLHelper(unittest.TestCase):

    def setUp(self):
        self.routes_file = "fixtures/hello.rou.xml"
        self.output_file = "fixtures/hello_out.rou.xml"

    def test_read_xml(self):
        tree = XMLHelper.read_xml(self.routes_file)
        self.assertIsNotNone(tree)
        self.assertEqual(tree.getroot().tag, "routes")

    def test_write_xml(self):
        tree = XMLHelper.read_xml(self.routes_file)
        self.assertEqual(len(tree.getroot().getchildren()), 7)
        XMLHelper.write_xml(tree, self.output_file)

    def test_add_child_node(self):
        tree = XMLHelper.read_xml(self.routes_file)
        element = XMLHelper.create_node("flow", {"id": "1", "type": "car"})
        XMLHelper.add_child_node(tree.getroot(), element)
        self.assertEqual(len(tree.getroot().getchildren()), 8)

    def test_del_node(self):
        tree = XMLHelper.read_xml(self.routes_file)
        XMLHelper.del_node(tree.getroot(), "flow")
        self.assertEqual(len(tree.getroot().getchildren()), 4)


if __name__ == "__main__":
    unittest.main()
