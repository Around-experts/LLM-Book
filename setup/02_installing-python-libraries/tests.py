# Copyright (c) Hieu Truong Cong (Brenton) under Apache License 2.0 (see LICENSE.txt).
# Source for "Build a Large Language Model From Scratch"
#   - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Code: https://github.com/Around-experts/LLM-Book

# File for internal use (unit tests)

from python_environment_check import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "FAIL" not in captured.out
