import markovify
import MeCab

m = MeCab.Tagger('-Owakati')
parsed_text = ""

for line in open('tweets.txt', 'r'):
    words = m.parse(line)
    words = words.rstrip('\n')
    parsed_text += words
    parsed_text += '\n'

text_model = markovify.NewlineText(parsed_text, state_size=3)

for _ in range(10):
    sentence = text_model.make_short_sentence(
        140, 10, tries=150)
    print(sentence.replace(' ', ''))
