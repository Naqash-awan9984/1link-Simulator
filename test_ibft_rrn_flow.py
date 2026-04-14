import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("1link-simulator.py")
SPEC = importlib.util.spec_from_file_location("one_link_simulator", MODULE_PATH)
simulator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(simulator)


class IbftRrnFlowTests(unittest.TestCase):
    def setUp(self):
        simulator.RRN_TRACKER = {}
        simulator.RRN_TRACKER_DATE = simulator.datetime.now().date()

    def test_first_delayed_request_reserves_success_and_retry_is_duplicate(self):
        rrn = "123456789012"

        self.assertEqual(simulator._get_rrn_decision(rrn, 1), ("delay", 1))
        self.assertEqual(simulator._get_rrn_decision(rrn, 1), ("duplicate", 0))
        simulator._complete_delayed_rrn_response(rrn)
        self.assertEqual(simulator._get_rrn_decision(rrn, 1), ("duplicate", 0))

    def test_delayed_request_completes_and_later_retry_is_duplicate(self):
        rrn = "123456789013"

        self.assertEqual(simulator._get_rrn_decision(rrn, 1), ("delay", 1))
        simulator._complete_delayed_rrn_response(rrn)
        self.assertEqual(simulator._get_rrn_decision(rrn, 1), ("duplicate", 0))

    def test_without_delay_first_request_succeeds_immediately(self):
        rrn = "123456789014"

        self.assertEqual(simulator._get_rrn_decision(rrn, 0), ("succeed", 0))
        self.assertEqual(simulator._get_rrn_decision(rrn, 0), ("duplicate", 0))


if __name__ == "__main__":
    unittest.main()