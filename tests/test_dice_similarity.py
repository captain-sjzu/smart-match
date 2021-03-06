import unittest
import smart_match

class TestDiceSimilarity(unittest.TestCase):
    
    def setUp(self):
        smart_match.use('dice')

    def test_similarity(self):
        self.assertAlmostEqual(smart_match.similarity('hello', 'hero'), 0.75)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.similarity('test string1', 'test string2'), 0.5)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity('test', 'test string2')), 0.6667)
        self.assertAlmostEqual(smart_match.similarity('', 'test string2'), 0.0000)
        self.assertAlmostEqual(smart_match.similarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.7500)
        self.assertAlmostEqual(smart_match.similarity('a b c d', 'a b c e'), 0.7500)

        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sealed'), 0.0000)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Healthy'), 0.0000)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Herded'), 0.0000)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Help'), 0.0000)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sold'), 0.0000)
        self.assertAlmostEqual(smart_match.similarity('Healed', 'Sold'), 0.0000)

        self.assertAlmostEqual(float('%.4f' % smart_match.similarity('Sam J Chapman', 'Samuel John Chapman')), 0.3333)
        self.assertAlmostEqual(smart_match.similarity('Sam Chapman', 'S Chapman'), 0.5000)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Samuel John Chapman'), 0.4000)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'Sam Chapman'), 0.0000)
        self.assertAlmostEqual(smart_match.similarity('John Smith', 'S Chapman'), 0.0000)

        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Web Database Applications with PHP & MySQL'), 0.6000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity('Web Database Applications', 'Creating Database Web Applications with PHP and ASP')), 0.5455)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity('Web Database Applications', 'Building Database Applications on the Web Using PHP3')), 0.5455)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity('Web Database Applications', 'Building Web Database Applications with Visual Studio 6')), 0.5455)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Web Application Development With PHP'), 0.2500)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection'), 0.4000)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'Structural Assessment: The Role of Large and Full-Scale Testing'), 0.0000)
        self.assertAlmostEqual(smart_match.similarity('Web Database Applications', 'How to Find a Scholarship Online'), 0.0000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity('Web Applications', 'Web Database Applications with PHP & MySQL')), 0.4444)
        self.assertAlmostEqual(smart_match.similarity('Web Applications', 'Creating Database Web Applications with PHP and ASP'), 0.4000)
        self.assertAlmostEqual(smart_match.similarity('Web Applications', 'Building Database Applications on the Web Using PHP3'), 0.4000)
        self.assertAlmostEqual(smart_match.similarity('Web Applications', 'Building Web Database Applications with Visual Studio 6'), 0.4000)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity('Web Applications', 'Web Application Development With PHP')), 0.2857)
        self.assertAlmostEqual(float('%.4f' % smart_match.similarity('Web Applications', 'WebRAD: Building Database Applications on the Web with Visual FoxPro and Web Connection')), 0.2857)
        self.assertAlmostEqual(smart_match.similarity('Web Applications', 'Structural Assessment: The Role of Large and Full-Scale Testing'), 0.0000)
        self.assertAlmostEqual(smart_match.similarity('Web Applications', 'How to Find a Scholarship Online'), 0.0000)

    def test_dissimilarity(self):
        self.assertAlmostEqual(smart_match.dissimilarity('hello', 'hero'), 0.25)
        smart_match.set_params(level='term')
        self.assertAlmostEqual(smart_match.dissimilarity('test string1', 'test string2'), 0.5)
        self.assertAlmostEqual(float('%.4f' % smart_match.dissimilarity('test', 'test string2')), 0.3333)
        self.assertAlmostEqual(smart_match.dissimilarity('', 'test string2'), 1.0000)
        self.assertAlmostEqual(smart_match.dissimilarity('aaa bbb ccc ddd', 'aaa bbb ccc eee'), 0.2500)
        self.assertAlmostEqual(smart_match.dissimilarity('a b c d', 'a b c e'), 0.2500)

if __name__ == '__main__':
    unittest.main()
