#!-*- coding:utf8-*-
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def randomWalk(_g, _corpus_num, _deep_num, _current_word):
	_corpus = []
	for i in range(_corpus_num):
		sentence = [_current_word]  
		current_word = _current_word
		count = 0
		while count<_deep_num:
			count+=1
			_node_list = []
			_weight_list = []
			for _nbr, _data in _g[current_word].items():
				_node_list.append(_nbr)
				_weight_list.append(_data['weight'])
			_ps = [float(_weight) / sum(_weight_list) for _weight in _weight_list]
			sel_node = roulette(_node_list, _ps)
			sentence.append(sel_node)
			current_word = sel_node
		_corpus.append(sentence)
	return _corpus

def roulette(_datas, _ps):
	return np.random.choice(_datas, p=_ps)



G = nx.DiGraph() 
path = './graph.txt'
word_list = []
with open(path,'r') as f:
	k=1
	for line in f:

		cols = line.strip().split(',')

		G.add_weighted_edges_from([(cols[0], cols[1], float(cols[2]))])
		word_list.append(cols[0])
		G.add_weighted_edges_from([(cols[1], cols[0], float(cols[2]))])
		word_list.append(cols[1])
		print(k)
		k+=1


word_set = set(word_list)
# nx.draw(G)
# plt.savefig("youxiangtu.png")
# plt.show()
num = 10
deep_num = 20
sentence_file = open('./GraphSentence.txt','w')
k = 1
for word in word_set:
	print(k)
	k+=1
	corpus = randomWalk(G, num, deep_num, word)
	# print(corpus)
	for cols in corpus:
		sentences = '\t'.join(cols)
		sentence_file.write(sentences+'\n')
		
















# G.add_edge(2,3)
# G.add_weighted_edges_from([(3, 4, 3.5),(3, 5, 7.0)])      


# print G.get_edge_data(2, 3)
# print G.get_edge_data(3, 4)
# print G.get_edge_data(3, 5)
