from twttr import shorten

def main():
    text = input("Input: ")
    result = test_assert(text)
    print("Output:", result)

def test_assert():
    assert shorten("hello world") == "hll wrld"
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("h3ll0 w0rld") == "h3ll0 w0rld"
    assert shorten("h@llo w*rld!!!") == "h@ll w*rld!!!"

if __name__ == "__main__":
    main()
