from flask import Flask, request
import json
import numpy as np
import networkx as nx

sentence_num = 3
result = []

app = Flask(__name__)



@app.route("/test", methods=["POST"])
def check():


    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}

    if request.get_data() is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)

    get_Data = request.get_data()

    get_Data = json.loads(get_Data)
    article = get_Data.get('article')


    return_dict['result'] = tt(article)

    return json.dumps(return_dict, ensure_ascii=False)


def cut_sentences(content):

    end_flag = ['?', '!', '.', '？', '！', '。', '…']

    content_len = len(content)
    sentences = []
    tmp_char = ''
    for idx, char in enumerate(content):

        tmp_char += char


        if (idx + 1) == content_len:
            sentences.append(tmp_char)
            break

        if char in end_flag:

            next_idx = idx + 1
            if not content[next_idx] in end_flag:
                sentences.append(tmp_char)
                tmp_char = ''

    return sentences


def word_pretreatment(text):
    words = []
    from nltk.tokenize import word_tokenize
    s = open("stopword", 'r', encoding='utf-8')
    sw = s.read()
    stopword = sw.splitlines()
    punctuation_list = [',', '–', '.', '"', '’', '“', '”', ';', '?', '!', '(', ')', ':', '...']

    for sent in text:
        word = list(word_tokenize(sent))
        word = [w for w in word if w not in stopword]
        word = [w for w in word if w not in punctuation_list]
        words.append(word)

    return words


def get_word_vector(list_word1, list_word2):
    key_word = list(set(list_word1 + list_word2))
    words_vector1 = np.zeros(len(key_word))
    words_vector2 = np.zeros(len(key_word))

    for i in range(len(key_word)):
        for j in range(len(list_word1)):
            if key_word[i] == list_word1[j]:
                words_vector1[i] += 1

        for k in range(len(list_word2)):
            if key_word[i] == list_word2[k]:
                words_vector2[i] += 1

    return words_vector1, words_vector2


def cos_dist(vec1, vec2):
    dist1 = float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))

    return dist1


def Sim_Matrix(words):
    n = len(words)
    sim_matrix = np.empty([n, n], dtype=float)

    for i in range(n):
        for j in range(n):
            vec1, vec2 = get_word_vector(words[i], words[j])
            a = cos_dist(vec1, vec2)
            sim_matrix[i][j] = a

    return sim_matrix


def G_Matrix(sim_matrix):
    n = len(sim_matrix)
    g_matrix = np.empty([n, n], dtype=float)
    for i in range(n):
        for j in range(n):
            if sim_matrix[i][j]<=0.0:
                sim_matrix[i][j]=0.000000000000000000001
            x = pow(0.1, abs(i - j - 1))
            g_matrix[i][j] = (sim_matrix[i][j]) * x

    return g_matrix


def Graph_genneration(g_matrix,vertex_list):
    g_data = []

    for i in vertex_list:
        for j in vertex_list:
            if i > j:
                if g_matrix[i][j]>0.0:
                    g_data.extend([(i,j,g_matrix[i][j])])

    g = nx.Graph()
    g.add_weighted_edges_from(g_data)

    return g


def cut_iter(g_matrix,vertex_list):
    g = Graph_genneration(g_matrix, vertex_list)
    a = nx.stoer_wagner(g)
    if len(a[1][0])>sentence_num:
        cut_iter(g_matrix,a[1][0])
    if len(a[1][0]) <= sentence_num:
        result.append(a[1][0])
    if len(a[1][1])>sentence_num:
        cut_iter(g_matrix,a[1][1])
    if len(a[1][1]) <= sentence_num:
        result.append(a[1][1])


def dec(text):
    sentences = cut_sentences(text)
    word_list = word_pretreatment(sentences)
    sim_matrix = Sim_Matrix(word_list)
    g_matrix = G_Matrix(sim_matrix)
    V_num = len(g_matrix)
    V_list = []
    for i in range(V_num):
        V_list.append(i)


    cut_iter(g_matrix, V_list)

    result.sort()

    return result,sentences


def tt(text):
    result,sentences = dec(text)
    result_len = len(result)
    json_list = []
    for i in range(result_len):
        temp_str = ''
        for j in result[i]:
            temp_str = temp_str + sentences[j]
        json_list.append({'paragraph':temp_str,'index':i})
    return json_list


if __name__ == "__main__":
    app.run(debug=True)