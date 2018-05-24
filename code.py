from nltk import word_tokenize

def step_one_read_in(textfile):
    text = ''
    with open(textfile, 'rt') as file_in:
        for line in file_in:
            text = text + line
    return text


def step_two_tokenize_text(text):
    tokenized = word_tokenize(text)
    return tokenized


def step_four_parse_text(tokenized):
    # let's set up some lists to hold our pieces of narrative and dialog
    parsed_dialog = []
    parsed_narrative = []
    # and this list will be a bucket for the text we're currently exploring
    current = []

    # now let's set up values that will help us loop through the text
    length = len(tokenized)
    found_q = False
    counter = 0
    quote_open, quote_close = '“', '”'

    # now we'll start our loop saying that as long as our sentence is...
    while counter < length:
        word = tokenized[counter]

        # until we find a quotation mark, we're working with narrative
        if quote_open not in word and quote_close not in word:
            current.append(word)

        # here's what we do when we find a closed quote
        else:
            # we append the narrative we've collected & clear our our
            # current variable
            parsed_narrative.append(current)
            current = []
            # now current is ready to hold dialog and we're working on
            # a piece of dialog
            current.append(word)
            found_q = True

            # while we're in the quote, we're going to increment the counter
            # and append to current in this while loop
            while found_q and counter < length-1:
                counter += 1
                if quote_close not in tokenized[counter]:
                    current.append(tokenized[counter])
                else:
                    # if we find a closing quote, we add our dialog to the
                    # appropriate list, clear current and flip our found_q
                    # variable to False
                    current.append(tokenized[counter])
                    parsed_dialog.append(current)
                    current = []
                    found_q = False

        # increment the counter to move us through the text
        counter += 1

    return (parsed_dialog, parsed_narrative)


for __name__ in "__main__":
    text = step_one_read_in('text.txt')
    tokenized = step_two_tokenize_text(text)
    parsed_dialog, parsed_narrative = step_four_parse_text(tokenized)
    print("Here is the dialog", parsed_dialog)
    print("*" * 100)
    print("Here is the narrative",  parsed_narrative)
