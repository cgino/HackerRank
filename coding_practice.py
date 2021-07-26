# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.
import numpy as np

text_input = "Heute Nachmittag war es mega heiss, welch Mühsal. Darum habe ich eine eisgekühlte Pommalunder genossen." \
             " Wer könnte mir dies schon ankreiden?"


def sentence_maker(text, punctuation):
    sentences = []
    i = 0
    while i < len(text):
        if punctuation.intersection(set(text[i])):
            sentences.append(text[:i + 1])
            text = text[i + 2:]
            i = 0
        else:
            i += 1
    return sentences

def word_maker(text, punctuation):
    sentences = []
    i = 0
    while i < len(text):
        if punctuation.intersection(set(text[i])):
            sentences.append(text[:i + 1])
            text = text[i + 1:]
            i = 0
        else:
            i += 1
    return sentences

def av_word_len(sentence):
    punctuation = ['.', '!', '?', ',', '-']
    # sentence = sentence[:-1]
    # sentence = set(sentence)
    print(sentence)
    print(type(sentence))
    i = 0
    mean_lens = []
    for ele in sentence:
        print(i)
        i += 1
        # print(type(ele))
        print('ele1: ', ele)
        # str_val = "".join(map(str, ele))
        # remains = map(lambda x: ele.replace(x, ""), punctuation)  # str_val.replace()
        for sign in punctuation:
            ele = ele.replace(sign, '')
        print('ele:', 'll:', ele)
        print(ele.split())
        # word_len.append(ele.replace(' ', ''))
        # print(ele+'...')
        # print(ele)
        words = word_maker(ele+' ', punctuation={' '})

        # words = sentence_maker(ele+' ', punctuation={' '})

        print('words: ', words)
        print(type(words))
        word_len = map(len, words)
        word_len = list(word_len)
        print(word_len)
        word_len = [x - 1 for x in word_len]
        print(word_len)
        mean_lens.append(np.round(np.mean(word_len), 2))
        print(mean_lens)
    return  mean_lens
        # return mean(word_len)
        # print(list(word_len))
        # print(str_val)
        # remains = set(ele).difference(punctuation)
        # remains =
        # print(list(remains))




if __name__ == "__main__":

    input_sent = sentence_maker(text_input, punctuation={'.', '!', '?'})
    print(input_sent)
    av_word_lengths = av_word_len(input_sent)
    print(av_word_lengths)