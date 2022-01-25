# AmPyfier Evaluation
Evaluation of AmPyfier on several open-source projects

## Projects Evaluated
| **Project** | **Test Class**|
| --- | --- |
| [Addict](https://github.com/mewwts/addict) | `test_addict.DictTests` <br> `test_addict.ChildDictTests` |
| [markdown](https://github.com/Python-Markdown/markdown) | `TestAbbr` <br> `TestAdmonition` <br> `TestAncestorExclusion` <br> `testAtomicString` <br> `TestBlockAppend` <br> `TestBlockParser` <br> `TestBlockParserState` <br> `TestCaseWithAssertStartsWith` <br> `TestCliOptionParsing` <br> `TestConfigParsing` <br> `TestConvertFile` <br> `testElementTailTests` <br> `TestErrors` <br> `TestEscapeAppend` <br> `testETreeComments` <br> `TestExtensionClass` <br> `TestGeneralDeprecations` <br> `TestHtmlStash` <br> `TestMarkdownBasics` <br> `TestMetaData` <br> `testSerializers` <br> `TestSmarty` <br> `TestTOC` <br> `TestVersion` <br> `TestWikiLinks` |
| [mistune](https://github.com/lepture/mistune) | `TestAstRenderer` <br> `TestMiscCases` <br> `TestPluginAdmonition` <br> `TestPluginDirective` |
| [MPyQ](https://github.com/eagleflo/mpyq) | `test.test_mpqarchive.TestMPQArchive` |
| [Pippin Nano Wallet](https://github.com/appditto/pippin_nano_wallet) | `TestAESCrypt` <br> `TestNanoUtil` <br> `TestRandomUtil` <br> `TestValidators` <br> `TestWalletUtil` |
| [PJ](https://github.com/eatonphil/pj) | `tests.test_pj.TestStringMethods` |
| [profig](https://github.com/dhagrow/profig) | `TestBasic` <br> `TestStrictMode` |
| [PyPDF2](https://github.com/mstamy2/PyPDF2) | `tests.tests.PdfReaderTestCases` <br> `tests.tests.AddJsTestCase` |
| [Python Twelve Tone](https://github.com/accraze/python-twelve-tone) | `tests.test_composer.TestMatrix` <br> `tests.test_midi.TestMIDIFile` |
| [TheFuzz](https://github.com/dhagrow/profig) | `ProcessTest` <br> `RatioTest` <br> `StringProcessingTest` <br> `TestCodeFormat` <br> `UtilsTest` <br> `ValidatorTest` |
| [Whois](https://github.com/richardpenman/whois) | `TestExtractDomain` <br> `TestParser` <br> `TestNICClient` |


## Results Sorted on Original Mutation Score (MSO)
| Project            | TestClass                    | Methods Added | CSO     | CSA     | CSI   | RCSI  | MSO    | MSA     | MSI    | RMSI    |
|--------------------|------------------------------|---------------|---------|---------|-------|-------|--------|---------|--------|---------|
| pippin_nano_wallet | TestRandomUtil               |             0 |    100% |    100% |    0% |    0% |   100% |    100% |   100% |      0% |
| mistune            | TestAstRenderer              |             0 |  34,61% |  34,61% |    0% |    0% | 99,30% |  99,30% |     0% |      0% |
| mistune            | TestPluginAdmonition         |             5 |  56,85% |  58,32% | 1,47% | 2,59% | 97,27% |  97,27% |     0% |      0% |
| markdown           | TestAbbr                     |             7 |  55,92% |  57,83% | 1,91% | 3,42% | 96,18% |  99,31% |  3,13% |   3,26% |
| mistune            | TestPluginDirective          |             6 |  59,50% |  62,74% | 3,24% | 5,45% | 95,96% |  98,07% |  2,11% |   2,20% |
| markdown           | TestConvertFile              |             1 |  46,12% |  46,18% | 0,06% | 0,13% | 94,42% |  94,42% |     0% |      0% |
| markdown           | TestErrors                   |             1 |  33,33% |  33,80% | 0,47% | 1,40% | 93,21% |  93,21% |     0% |      0% |
| markdown           | testSerializers              |             3 |  50,38% |  50,96% | 0,58% | 1,16% | 93,08% |  96,18% |  3,10% |   3,33% |
| pippin_nano_wallet | TestAESCrypt                 |             4 |  96,55% |    100% | 3,45% | 3,57% | 93,06% |  98,61% |  5,56% |   5,96% |
| markdown           | RegistryTests                |             0 |  27,32% |  27,32% | 0,00% | 0,00% | 92,44% |  92,44% |     0% |      0% |
| markdown           | testETreeComments            |             0 |  33,57% |  33,57% |    0% |    0% | 92,37% |  92,37% |     0% |      0% |
| markdown           | TestWikiLinks                |             7 |  53,41% |  54,55% | 1,14% | 2,13% | 92,32% |  96,38% |  4,06% |   4,40% |
| markdown           | TestConfigParsing            |             3 |  25,80% |  25,80% | 0,00% |    0% | 92,18% |  93,20% |  1,02% |   1,11% |
| markdown           | testAtomicString             |             7 |  43,49% |  44,25% | 0,76% | 1,74% | 91,83% |  94,86% |  3,03% |   3,29% |
| markdown           | TestBlockParserState         |             0 |  25,39% |  25,39% |    0% |    0% | 91,82% |  91,82% |     0% |      0% |
| markdown           | TestBlockAppend              |             0 |  31,39% |  31,39% |    0% |    0% | 91,62% |  91,62% |     0% |      0% |
| markdown           | TestEscapeAppend             |             0 |  31,93% |  31,93% |    0% |    0% | 91,62% |  91,62% |     0% |      0% |
| markdown           | TestVersion                  |             1 | 100,00% | 100,00% | 0,00% |    0% | 91,53% |  93,22% |  1,69% |   1,85% |
| markdown           | TestGeneralDeprecations      |             0 |  25,10% |  25,10% |    0% |    0% | 91,47% |  91,47% |     0% |      0% |
| markdown           | testElementTailTests         |             1 |  32,69% |  32,75% | 0,06% | 0,18% | 91,41% |  91,41% |     0% |      0% |
| markdown           | TestHtmlStash                |             1 |  25,74% |  25,74% |    0% |    0% | 91,36% |  91,76% |  0,37% |   0,41% |
| markdown           | TestCaseWithAssertStartsWith |             0 |  25,06% |  25,06% |    0% |    0% | 91,09% |  91,09% |     0% |      0% |
| markdown           | TestBlockParser              |             4 |  37,89% |  38,70% | 0,82% | 2,16% | 90,71% |  93,81% |  3,10% |   3,41% |
| python-twelve-tone | TestMatrix                   |             1 |  83,64% |  83,64% |    0% |    0% | 90,32% |  91,94% |  1,61% |   1,79% |
| markdown           | TestAdmonition               |             0 |  33,25% |  33,25% |    0% |    0% | 90,16% |  90,16% |     0% |      0% |
| markdown           | TestAncestorExclusion        |             6 |  56,74% |  59,19% | 2,45% | 4,32% | 89,77% |  95,02% |  5,24% |   5,84% |
| markdown           | TestMarkdownBasics           |             4 |  45,94% |  46,53% | 0,58% | 1,27% | 89,73% |  94,50% |  4,78% |   5,32% |
| PyPDF2             | PdfReaderTestCase            |             0 |  34,46% |  34,46% |    0% |    0% | 89,27% |  89,27% |     0% |      0% |
| pj                 | TestStringMethods            |             6 |     75% |  78,95% | 3,95% | 5,26% | 87,56% |  89,78% |  2,22% |   2,54% |
| pippin_nano_wallet | TestValidators               |             3 |    100% |    100% |    0% |    0% | 86,57% |  91,04% |  4,48% |   5,17% |
| PyPDF2             | AddJsTestCase                |             1 |  32,14% |  32,17% | 0,03% | 0,10% | 86,44% |  86,44% |     0% |      0% |
| mistune            | TestMiscCases                |             3 |  62,74% |  66,27% | 3,53% | 5,63% | 85,13% |  92,48% |  7,35% |   8,64% |
| mpyq               | TestMPQArchive               |             2 |  65,27% |  65,65% | 0,38% | 0,58% | 81,92% |  83,38% |  1,46% |   1,78% |
| markdown           | TestExtensionClass           |             2 |  25,06% |  25,54% | 0,48% | 1,91% | 81,23% |  88,45% |  7,22% |   8,89% |
| addict             | ChildDictTests               |             2 | 100,00% | 100,00% | 0,00% | 0,00% | 80,52% |  83,12% |  2,60% |   3,23% |
| addict             | DictTests                    |             2 | 100,00% | 100,00% | 0,00% | 0,00% | 80,52% |  83,12% |  2,60% |   3,23% |
| markdown           | TestTOC                      |            18 |  61,30% |  67,17% | 5,86% | 9,56% | 79,88% |  92,93% | 13,10% |  16,39% |
| markdown           | TestSmarty                   |             5 |  50,24% |  50,54% | 0,30% | 0,60% | 78,48% |  79,40% |  0,92% |   1,17% |
| markdown           | TestMetaData                 |             9 |  47,85% |  54,07% | 6,22% |   13% | 76,23% |  87,18% | 10,95% |  14,36% |
| markdown           | TestCliOptionParsing         |             2 |    100% |    100% |    0% |    0% | 75,44% |  80,70% |  5,26% |   6,89% |
| TheFuzz            | StringProcessingTest         |             0 |    100% |    100% |    0% | 0,00% | 66,67% |  66,67% |     0% |      0% |
| TheFuzz            | RatioTest                    |            24 |  60,49% |  62,92% | 2,43% | 4,02% | 56,53% |  73,86% | 17,33% |  30,65% |
| whois              | TestNICClient                |             7 |  43,35% |  44,87% | 1,52% | 3,51% | 54,74% |  81,47% | 26,72% |  48,82% |
| TheFuzz            | ProcessTest                  |            22 |  76,60% |  78,72% | 2,13% | 2,78% | 54,25% |  82,53% | 28,28% |  52,12% |
| profig             | TestBasic                    |            10 |  49,39% |  50,34% | 0,95% | 1,92% | 50,36% |  54,68% |  4,32% |   8,57% |
| whois              | TestParser                   |            11 |  53,15% |  53,87% | 4,72% | 8,89% | 47,70% |  60,94% | 13,47% |  28,37% |
| whois              | TestExtractDomain            |             2 |  37,49% |  37,58% | 0,09% | 0,24% | 43,88% |  48,98% |  5,10% |  11,63% |
| profig             | TestStrictMode               |             8 |  58,62% |  61,19% | 2,58% | 4,40% | 35,11% |  38,42% |  3,31% |   9,42% |
| TheFuzz            | ValidatorTest                |             0 |  28,27% |  28,27% |    0% |    0% | 34,65% |  34,65% |     0% |      0% |
| pippin_nano_wallet | TestNanoUtil                 |             0 |  87,50% |  87,50% |    0% |    0% | 29,27% |  29,27% |     0% |      0% |
| python-twelve-tone | TestMIDIFile                 |             1 | 100,00% | 100,00% | 0,00% | 0,00% | 27,78% | 100,00% | 72,22% | 260,00% |
| TheFuzz            | UtilsTest                    |             0 |  29,79% |  29,79% |    0% |    0% | 19,23% |  19,23% |     0% |      0% |
| pippin_nano_wallet | TestWalletUtil               |             0 |  23,53% |  23,53% |    0% |    0% | 12,90% |  12,90% |  0,00% |   0,00% |
| TheFuzz            | TestCodeFormat               |             0 |  26,44% |  26,44% |    0% |    0% |  8,45% |   8,45% |     0% |      0% |

Coverage Score (CS) and Mutation Score(MS), of the original test class (..O) and after amplification (..A) and the
(relative<sup>\*</sup>) increase in mutation score (R..I & ..I), all
expressed in %

<sup>\*</sup> (mutants killed amplified - mutants killed originally)/mutants killed originally or    
(lines covered amplified - lines covered originally)/lines covered originally

## Notes
1. It is possible to not replicate the exact same results for each run of AmPyfier.
This is caused by the randomness in the selection of amplified tests once the number of amplified tests exceeds the number of tests to be collected.
Another factor is the randomness of the generated function or method calls and their inputs.
