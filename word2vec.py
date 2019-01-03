import gensim
with open('./GraphSentence.txt','r') as f:
    sentences = []
    for line in f:
        cols = line.strip().split('\t')
        sentences.append(cols)



model = gensim.models.Word2Vec(sentences, sg=1, size=300, alpha=0.025, window=3, min_count=1, max_vocab_size=None, sample=1e-3, seed=1, workers=45, min_alpha=0.0001, hs=0, negative=20, cbow_mean=1, hashfxn=hash, iter=5, null_word=0, trim_rule=None, sorted_vocab=1, batch_words=1e4)


outfile = './test'
fname = './testmodel-0103'
# save
model.save(fname) 
model.wv.save_word2vec_format(outfile + '.model.bin', binary=True)  
model.wv.save_word2vec_format(outfile + '.model.txt', binary=False) 


fname = './testmodel-0103'
model = gensim.models.Word2Vec.load(fname)  
a = model.most_similar('男')
print(a)



