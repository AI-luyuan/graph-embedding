Rethinking Knowledge Graph Propagation for Zero-Shot Learning [Paper link](https://arxiv.org/abs/1805.11724)

This paper tries to solve the problem of zero-shot learning: using prior knowledge to classify images from unseen classes into correct categories.

## Motivation:
Graph convolutional neural networks have recently shown great potential for the task of zero-shot learning. However, multi-layer architectures, which are required to propagate knowledge to distant nodes in the graph, dilute the knowledge by performing extensive Laplacian smoothing at each layer and thereby consequently decrease performance.

## Contribution:
The proposed method build a dense connectivity structure, which explicitly exploits the hierarchical
structure of the knowledge graph to perform zero-shot learning by efficiently propagating knowledge.

![DGP_DenseGraph](https://github.com/AI-luyuan/graph-embedding/blob/master/images/DGP_DenseGraph.png)

## Approach:

The Dense Graph Propagation module for zero-shot learning aims to use the hierarchical graph structure for the zero-shot learning task and avoids dilution of knowledge by intermediate nodes. This is achieved using a dense graph connectivity scheme consisting of two phases, namely descendant propagation and ancestor propagation. 

![DGP_Framework](https://github.com/AI-luyuan/graph-embedding/blob/master/images/DGP_Framework.png)
 

The overall DGP propagation rule: 

<a href="https://www.codecogs.com/eqnedit.php?latex=H=\sigma\left(D_{a}^{-1}&space;A_{a}&space;\sigma\left(D_{d}^{-1}&space;A_{d}&space;X&space;\Theta_{d}\right)&space;\Theta_{a}\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H=\sigma\left(D_{a}^{-1}&space;A_{a}&space;\sigma\left(D_{d}^{-1}&space;A_{d}&space;X&space;\Theta_{d}\right)&space;\Theta_{a}\right)" title="H=\sigma\left(D_{a}^{-1} A_{a} \sigma\left(D_{d}^{-1} A_{d} X \Theta_{d}\right) \Theta_{a}\right)" /></a>


