#!/usr/bin/python3
"""
This module provides the function `text_indentation`.
It splits text into blocks based on specific punctuation marks.
"""


def text_indentation(text):
      """
          Prints a text with 2 new lines after each of these characters: ., ? and :

              Args:
                      text: The string to be formatted and printed.

                          Raises:
                                  TypeError: If text is not a string.
                                      """
      if not isinstance(text, str):
                raise TypeError("text must be a string")

      # Characters that trigger two new lines
      special_chars = [".", "?", ":"]

    c = 0
    # Trim leading/trailing whitespace from the entire block first
    text = text.strip()

    while c < len(text):
              print(text[c], end="")
              if text[c] in special_chars:
                            print("\n")
                            # Skip all subsequent spaces after the special character
                            if c + 1 < len(text):
                                              while c + 1 < len(text) and text[c + 1] == ' ':
                                                                    c += 1
                                                        c += 1
