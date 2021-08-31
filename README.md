# AmPyfier Evaluation
Evaluation of AmPyfier on several open-source projects

## Projects
| **Project** | **Selected test class**|
| --- | --- |
| [Python Twelve Tone](https://github.com/accraze/python-twelve-tone) | `tests.test_composer.TestMatrix` <br> `tests.test_midi.TestMIDIFile` |
| [Pippin Nano Wallet](https://github.com/appditto/pippin_nano_wallet) | `tests.validator_tests.TestValidators` <br> `tests.crypt_tests.TestAESCrypt` |
| [Whois](https://github.com/richardpenman/whois) | `tests.test_main.TestExtractDomain` |
| [PyPDF2](https://github.com/mstamy2/PyPDF2) | `tests.tests.PdfReaderTestCases` <br> `tests.tests.AddJsTestCase` |
| [Addict](https://github.com/mewwts/addict) | `test_addict.DictTests` <br> `test_addict.ChildDictTests` |
| [MPyQ](https://github.com/eagleflo/mpyq) | `test.test_mpqarchive.TestMPQArchive` |
| [PJ](https://github.com/eatonphil/pj) | `tests.test_pj.TestStringMethods` |

## Results
|                    |  MSO  |  MSA  |  MSI  |  RMSI   |
|:-------------------|:-----:|:-----:|:-----:|:-------:|
| TestMatrix         | 89.29 | 89.29 |   0   |    0    |
| TestMIDIFile       |  100  |  100  |   0   |    0    |
| TestValidators     | 86.57 | 89.55 | 2.99  |  3.45   |
| TestAESCrypt       | 91.43 | 98.57 | 7.14  |  7.81   |
| TestExtractDomain  | 2.69  | 55.84 | 53.15 | 1975.86 |
| PdfReaderTestCases | 49.73 | 54.08 | 4.35  |  8.75   |
| AddJsTestCase      | 48.08 | 48.08 |   0   |    0    |
| DictTests          | 84.06 | 86.96 | 2.90  |  3.45   |
| ChildDictTests     | 84.06 | 86.96 | 2.90  |  3.45   |
| TestMPQArchive     | 59.47 | 59.47 |   0   |    0    |
| TestStringMethods  | 95.59 | 96.32 | 0.74  |  0.77   |

Mutation score before (MSO) and after amplification (MSA) and the
(relative<sup>\*</sup>) increase in mutation score (RMSI & MSI), all
expressed in %

<sup>\*</sup> (Mutants killed Amplified - Mutants killed
Originally)/Mutants killed Originally

## Notes
1. The reports contained in this repository are bare-boned text files. In future versions of AmPyfier more comprehensive reports will be generated
2. It is possible to not replicate the exact same results for each run of AmPyfier.
This is caused by the randomness in the selection of amplified tests once the number of amplified tests exceeds the number of tests to be collected.
Another factor is the randomness of the generated function or method calls and their inputs.
