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
| [TheFuzz](https://github.com/seatgeek/thefuzzg) | `ProcessTest` <br> `RatioTest` <br> `StringProcessingTest` <br> `TestCodeFormat` <br> `UtilsTest` <br> `ValidatorTest` |
| [Whois](https://github.com/richardpenman/whois) | `TestExtractDomain` <br> `TestParser` <br> `TestNICClient` |


## Results Sorted on Original Coverage Score (CSO)
| Project            | TestClass                    | T        | MO | MA | LOC   | CSO     | CSA     | CSI   | CLO  | CLA  | CAU  | RCLI   | MSO     | MSA     | MSI    | MKO  | MKA  | MNKA | MAA | RMSI    |
|--------------------|------------------------------|----------|----|----|-------|---------|---------|-------|------|------|------|--------|---------|---------|--------|------|------|------|-----|---------|
| pippin_nano_wallet | TestRandomUtil               | 00:00:00 |  1 |  0 |     7 | 100.00% | 100.00% | 0.00% |    7 |    7 |    0 |  0.00% | 100.00% | 100.00% |  0.00% |    0 |    0 |    0 |   0 |   0.00% |
| markdown           | TestVersion                  | 00:01:50 |  2 |  1 |    13 | 100.00% | 100.00% | 0.00% |   13 |   13 |    0 |  0.00% |  91.53% |  93.22% |  1.69% |   54 |   55 |    1 |   4 |   1.85% |
| pippin_nano_wallet | TestValidators               | 00:02:14 |  2 |  3 |    39 | 100.00% | 100.00% | 0.00% |   39 |   39 |    0 |  0.00% |  86.57% |  91.04% |  4.48% |   58 |   61 |    3 |   6 |   5.17% |
| addict             | ChildDictTests               | 01:10:04 | 63 |  2 |   130 | 100.00% | 100.00% | 0.00% |  130 |  130 |    0 |  0.00% |  80.52% |  83.12% |  2.60% |   62 |   64 |    2 |  13 |   3.23% |
| addict             | DictTests                    | 00:53:11 | 63 |  2 |   130 | 100.00% | 100.00% | 0.00% |  130 |  130 |    0 |  0.00% |  80.52% |  83.12% |  2.60% |   62 |   64 |    2 |  13 |   3.23% |
| markdown           | TestCliOptionParsing         | 00:10:01 | 16 |  2 |    41 | 100.00% | 100.00% | 0.00% |   41 |   41 |    0 |  0.00% |  75.44% |  80.70% |  5.26% |   43 |   46 |    3 |  11 |   6.89% |
| thefuzz            | StringProcessingTest         | 00:00:21 |  2 |  0 |    15 | 100.00% | 100.00% | 0.00% |   15 |   15 |    0 |  0.00% |  57.14% |  57.14% |  0.00% |    4 |    4 |    0 |   3 |   0.00% |
| python-twelve-tone | TestMIDIFile                 | 00:00:13 |  2 |  1 |    18 | 100.00% | 100.00% | 0.00% |   18 |   18 |    0 |  0.00% |  27.78% | 100.00% | 72.22% |    5 |   18 |   13 |   0 | 260.00% |
| pippin_nano_wallet | TestAESCrypt                 | 00:00:31 |  1 |  4 |    29 |  96.55% | 100.00% | 3.45% |   28 |   29 |    0 |  3.57% |  93.06% |  98.61% |  5.56% |   67 |   71 |    4 |   1 |   5.96% |
| pippin_nano_wallet | TestNanoUtil                 | 00:00:00 |  1 |  0 |    40 |  87.50% |  87.50% | 0.00% |   35 |   35 |    5 |  0.00% |  29.27% |  29.27% |  0.00% |   12 |   12 |    0 |  29 |   0.00% |
| python-twelve-tone | TestMatrix                   | 00:03:58 |  5 |  1 |    55 |  83.64% |  83.64% | 0.00% |   46 |   46 |    9 |  0.00% |  90.32% |  91.94% |  1.61% |  112 |  114 |    2 |  10 |   1.79% |
| thefuzz            | ProcessTest                  | 00:41:28 | 14 | 22 |   329 |  76.60% |  78.72% | 2.13% |  252 |  259 |   70 |  2.78% |  54.25% |  82.53% | 28.28% |  236 |  359 |  123 |  76 |  52.12% |
| pj                 | TestStringMethods            | 00:08:26 | 10 |  6 |   152 |  75.00% |  78.95% | 3.95% |  114 |  120 |   32 |  5.26% |  87.56% |  89.78% |  2.22% |  197 |  202 |    5 |  23 |   2.54% |
| mpyq               | TestMPQArchive               | 00:10:04 |  5 |  2 |   262 |  65.27% |  65.65% | 0.38% |  171 |  172 |   90 |  0.58% |  81.92% |  83.38% |  1.46% |  281 |  286 |    5 |  57 |   1.78% |
| mistune            | TestMiscCases                | 00:17:15 |  9 |  3 |   679 |  62.74% |  66.27% | 3.53% |  426 |  450 |  229 |  5.63% |  85.13% |  92.48% |  7.35% |  521 |  566 |   45 |  46 |   8.64% |
| markdown           | TestTOC                      | 02:29:50 | 15 | 18 | 1,672 |  61.30% |  67.17% | 5.86% | 1025 | 1123 |  549 |  9.56% |  79.88% |  92.93% | 13.10% | 1104 | 1285 |  181 |  97 |  16.39% |
| thefuzz            | RatioTest                    | 00:44:09 | 26 | 24 |   329 |  60.49% |  62.92% | 2.43% |  199 |  207 |  122 |  4.02% |  56.53% |  73.86% | 17.33% |  186 |  243 |   57 |  86 |  30.65% |
| mistune            | TestPluginDirective          | 00:05:22 |  3 |  6 |   679 |  59.50% |  62.74% | 3.24% |  404 |  426 |  253 |  5.45% |  95.96% |  98.07% |  2.11% |  546 |  558 |   12 |  11 |   2.20% |
| profig             | TestStrictMode               | 00:13:26 |  4 |  8 |   737 |  58.62% |  61.19% | 2.58% |  432 |  451 |  286 |  4.40% |  35.11% |  38.42% |  3.31% |  138 |  151 |   13 | 242 |   9.42% |
| mistune            | TestPluginAdmonition         | 00:07:57 |  8 |  5 |   679 |  56.85% |  58.32% | 1.47% |  386 |  396 |  283 |  2.59% |  97.27% |  97.27% |  0.00% |  463 |  463 |    0 |  13 |   0.00% |
| markdown           | TestAncestorExclusion        | 00:22:42 |  2 |  6 | 1,713 |  56.74% |  59.19% | 2.45% |  972 | 1014 |  699 |  4.32% |  89.77% |  95.02% |  5.24% | 1027 | 1087 |   60 |  57 |   5.84% |
| markdown           | TestAbbr                     | 00:08:15 |  2 |  6 | 1,672 |  55.92% |  57.83% | 1.91% |  935 |  967 |  705 |  3.42% |  96.18% |  99.31% |  3.13% |  981 | 1014 |   33 |   7 |   3.26% |
| markdown           | TestWikiLinks                | 00:33:50 |  6 |  7 | 1,672 |  53.41% |  54.55% | 1.14% |  893 |  912 |  760 |  2.13% |  92.32% |  96.38% |  4.06% |  841 |  878 |   37 |  33 |   4.40% |
| whois              | TestParser                   | 01:08:56 | 10 | 11 |   762 |  53.15% |  53.87% | 4.72% |  405 |  441 |  321 |  8.89% |  47.70% |  60.94% | 13.47% |  141 |  181 |   40 |  40 |  28.37% |
| markdown           | testSerializers              | 00:56:59 | 12 |  3 | 1,713 |  50.38% |  50.96% | 0.58% |  863 |  873 |  840 |  1.16% |  93.08% |  96.18% |  3.10% |  780 |  806 |   26 |   0 |   3.33% |
| markdown           | TestSmarty                   | 00:12:41 |  1 |  5 | 1,672 |  50.24% |  50.54% | 0.30% |  840 |  845 |  827 |  0.60% |  78.48% |  79.40% |  0.92% |  598 |  605 |    7 | 157 |   1.17% |
| profig             | TestBasic                    | 01:14:35 | 18 | 10 |   737 |  49.39% |  50.34% | 0.95% |  364 |  371 |  366 |  1.92% |  50.36% |  54.68% |  4.32% |  140 |  152 |   12 | 126 |   8.57% |
| markdown           | TestMetaData                 | 01:27:13 |  5 |  9 | 1,672 |  47.85% |  54.07% | 6.22% |  800 |  904 |  768 | 13.00% |  76.23% |  87.18% | 10.95% |  571 |  653 |   82 |  96 |  14.36% |
| markdown           | TestConvertFile              | 00:14:46 |  3 |  1 | 1,783 |  46.12% |  46.18% | 0.06% |  790 |  791 |  992 |  0.13% |  94.42% |  94.42% |  0.00% |  609 |  609 |    0 |  36 |   0.00% |
| markdown           | TestMarkdownBasics           | 00:19:34 |  6 |  4 | 1,713 |  45.94% |  46.53% | 0.58% |  787 |  797 |  916 |  1.27% |  89.73% |  94.50% |  4.78% |  620 |  653 |   33 |  38 |   5.32% |
| markdown           | testAtomicString             | 00:18:17 |  3 |  7 | 1,713 |  43.49% |  44.25% | 0.76% |  745 |  758 |  955 |  1.74% |  91.83% |  94.86% |  3.03% |  607 |  627 |   20 |  34 |   3.29% |
| whois              | TestNICClient                | 00:08:28 |  1 |  7 |   263 |  43.35% |  44.87% | 1.52% |  114 |  118 |  145 |  3.51% |  54.74% |  81.47% | 26.72% |  127 |  189 |   62 |  43 |  48.82% |
| markdown           | TestBlockParser              | 00:13:27 |  2 |  4 | 1,713 |  37.89% |  38.70% | 0.82% |  649 |  663 | 1050 |  2.16% |  90.71% |  93.81% |  3.10% |  498 |  515 |   17 |  34 |   3.41% |
| whois              | TestExtractDomain            | 01:12:52 |  7 |  2 | 1,107 |  37.49% |  37.58% | 0.09% |  415 |  416 |  691 |  0.24% |  43.88% |  48.98% |  5.10% |   43 |   48 |    5 |  50 |  11.63% |
| mistune            | TestAstRenderer              | 00:00:34 | 13 |  0 |   679 |  34.61% |  34.61% | 0.00% |  235 |  235 |  444 |  0.00% |  99.30% |  99.30% |  0.00% |  285 |  285 |    0 |   2 |   0.00% |
| PyPDF2             | PdfReaderTestCase            | 01:53:08 |  2 |  0 | 3,102 |  34.46% |  34.46% | 0.00% | 1069 | 1069 | 2033 |  0.00% |  89.27% |  89.27% |  0.00% | 1306 | 1306 |    0 | 157 |   0.00% |
| markdown           | testETreeComments            | 00:04:44 |  4 |  0 | 1,713 |  33.57% |  33.57% | 0.00% |  575 |  575 | 1138 |  0.00% |  92.37% |  92.37% |  0.00% |  351 |  351 |    0 |  29 |   0.00% |
| markdown           | TestErrors                   | 00:06:40 |  6 |  1 | 1,713 |  33.33% |  33.80% | 0.47% |  571 |  579 | 1134 |  1.40% |  93.21% |  93.21% |  0.00% |  398 |  398 |    0 |  29 |   0.00% |
| markdown           | TestAdmonition               | 00:06:02 |  1 |  0 | 1,672 |  33.25% |  33.25% | 0.00% |  556 |  556 | 1116 |  0.00% |  90.16% |  90.16% |  0.00% |  330 |  330 |    0 |  36 |   0.00% |
| markdown           | testElementTailTests         | 00:04:40 |  1 |  1 | 1,713 |  32.69% |  32.75% | 0.06% |  560 |  561 | 1152 |  0.18% |  91.41% |  91.41% |  0.00% |  330 |  330 |    0 |  31 |   0.00% |
| PyPDF2             | AddJsTestCase                | 03:19:31 |  2 |  1 | 3,102 |  32.14% |  32.17% | 0.03% |  997 |  998 | 2104 |  0.10% |  86.44% |  86.44% |  0.00% | 1077 | 1077 |    0 | 169 |   0.00% |
| markdown           | TestEscapeAppend             | 00:05:13 |  1 |  0 | 1,713 |  31.93% |  31.93% | 0.00% |  547 |  547 | 1166 |  0.00% |  91.62% |  91.62% |  0.00% |  317 |  317 |    0 |  29 |   0.00% |
| markdown           | TestBlockAppend              | 00:05:17 |  1 |  0 | 1,713 |  31.39% |  31.39% | 0.00% |  547 |  547 | 1166 |  0.00% |  91.62% |  91.62% |  0.00% |  317 |  317 |    0 |  29 |   0.00% |
| thefuzz            | UtilsTest                    | 00:01:26 |  4 |  0 |   329 |  29.79% |  29.79% | 0.00% |   98 |   98 |  231 |  0.00% |  19.23% |  19.23% |  0.00% |   15 |   15 |    0 |  63 |   0.00% |
| thefuzz            | ValidatorTest                | 00:03:30 |  2 |  0 |   329 |  28.27% |  28.27% | 0.00% |   93 |   93 |  236 |  0.00% |  34.65% |  34.65% |  0.00% |   35 |   35 |    0 |  66 |   0.00% |
| markdown           | RegistryTests                | 00:53:20 | 12 |  0 | 1,713 |  27.32% |  27.32% | 0.00% |  468 |  468 | 1245 |  0.00% |  92.44% |  92.44% |  0.00% |  269 |  269 |    0 |  22 |   0.00% |
| thefuzz            | TestCodeFormat               | 00:09:34 |  1 |  0 |   329 |  26.44% |  26.44% | 0.00% |   87 |   87 |  242 |  0.00% |   8.45% |   8.45% |  0.00% |    6 |    6 |    0 |  65 |   0.00% |
| markdown           | TestConfigParsing            | 00:07:55 |  3 |  3 | 1,713 |  25.80% |  25.80% | 0.00% |  442 |  442 | 1271 |  0.00% |  92.18% |  93.20% |  1.02% |  271 |  274 |    3 |  20 |   1.11% |
| markdown           | TestHtmlStash                | 00:06:07 |  3 |  1 | 1,713 |  25.74% |  25.74% | 0.00% |  441 |  441 | 1272 |  0.00% |  91.36% |  91.76% |  0.37% |  244 |  245 |    1 |  22 |   0.41% |
| markdown           | TestBlockParserState         | 00:11:52 |  4 |  0 | 1,713 |  25.39% |  25.39% | 0.00% |  435 |  435 | 1278 |  0.00% |  91.82% |  91.82% |  0.00% |  247 |  247 |    0 |  22 |   0.00% |
| markdown           | TestGeneralDeprecations      | 00:04:25 |  1 |  0 | 1,713 |  25.10% |  25.10% | 0.00% |  430 |  430 | 1283 |  0.00% |  91.47% |  91.47% |  0.00% |  236 |  236 |    0 |  22 |   0.00% |
| markdown           | TestCaseWithAssertStartsWith | 00:01:25 |  1 |  0 | 1,672 |  25.06% |  25.06% | 0.00% |  419 |  419 | 1253 |  0.00% |  91.09% |  91.09% |  0.00% |  225 |  225 |    0 |  22 |   0.00% |
| markdown           | TestExtensionClass           | 00:14:21 |  7 |  2 | 1,672 |  25.06% |  25.54% | 0.48% |  419 |  427 | 1245 |  1.91% |  81.23% |  88.45% |  7.22% |  225 |  245 |   20 |  32 |   8.89% |
| pippin_nano_wallet | TestWalletUtil               | 00:18:44 |  3 |  0 |   187 |  23.53% |  23.53% | 0.00% |   44 |   44 |  143 |  0.00% |  12.90% |  12.90% |  0.00% |    4 |    4 |    0 |  27 |   0.00% |



Execution Time (T), Methods Originally (MO) in the test class (MO) and Methods Added (MA).  
Lines Of Code (LOC) in the module under test.  
Coverage Score (CS.) and Mutation Score(MS.), of the original test class (..O) and after amplification (..A) and the (relative<sup>\*</sup>) increase in mutation score (R..I & ..I), allexpressed in %.  
Covered Lines (CL.) and uncovered lines after amplification (CAU).  
Mutants Killed (MK.), Mutants Newly Killed after Amplification (MNKA) and Mutatns Alive after Amplifcation (MAA).  

<sup>\*</sup> (MKA - MKO)/MKO or (LCA - LCO)/LCO

## Notes
1. It is possible to not replicate the exact same results for each run of AmPyfier.
This is caused by the randomness in the selection of amplified tests once the number of amplified tests exceeds the number of tests to be collected.
Another factor is the randomness of the generated function or method calls and their inputs.
