from string import punctuation


async def username_contain_forbidden_symbol(word: str) -> str | None:
    # r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    for c in word:
        if c in punctuation:
            return c
