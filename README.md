# Blackjack Test Generator

Generates blackjack basic strategy tests.

Creates two files in the working directory, the test file and answers file.
Each file contains a list of blackjack strategy questions and corresponding legend.
The answers file fills in the blanks with the correct basic strategy answers.

See the [sample test](test_sample.txt) and [sample answer key](test_sample_answers.txt) for an example of what the program outputs.

### Running the program

Clone or download this repository, then run the following command:

```python3 blackjack_test_generator.py [--size SIZE] [--versions VERSIONS]```

| Argument | Description | Default value |
|----|----|----|
| size | number of questions to generate | 48 |
| versions | comma separated list of versions | A |
