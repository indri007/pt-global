import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pages_content.nodexl_network import render_nodexl_network, NODEXL_CLOUD_TOKEN

class TestNodeXLPage(unittest.TestCase):
    def test_token_matches_gallery(self):
        self.assertEqual(NODEXL_CLOUD_TOKEN, "c1d8d71236e1cae9628f0b5c7a55b581")

    def test_callable(self):
        self.assertTrue(callable(render_nodexl_network))

    def test_top_10_betweenness_data(self):
        from pages_content.nodexl_network import get_top_10_betweenness
        df = get_top_10_betweenness()
        self.assertEqual(len(df), 10, "Must return exactly top 10 betweenness actors")
        self.assertTrue(df["Betweenness Centrality"].is_monotonic_decreasing, "Must be sorted descending")

    def test_top_10_topics_data(self):
        from pages_content.nodexl_network import get_top_10_topics
        topics = get_top_10_topics()
        self.assertEqual(len(topics), 10, "Must return exactly 10 WhatsApp conversation topics")
        self.assertIn("Topik Pembicaraan WhatsApp", topics.columns)
        self.assertIn("Pangsa Volume", topics.columns)

    def test_whatsapp_corpus_stats(self):
        from pages_content.nodexl_network import get_whatsapp_corpus_stats
        stats = get_whatsapp_corpus_stats()
        self.assertEqual(stats["total_corpus_volume"], 1_000_000)
        self.assertEqual(stats["period"], "2000-2026")
        self.assertIn("indobert_accuracy", stats)

if __name__ == "__main__":
    unittest.main()
