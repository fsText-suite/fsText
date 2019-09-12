# Few Shot Text Classification

<img alt="GitHub contributors" src="https://img.shields.io/github/contributors-anon/maelfabien/FewShotTextClassification.svg"> <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/3.svg">

*Use Case* : A user has a column of short texts (e.g user reviews) but those comments are not labeled. We ask the user to hand-label just a few texts for each class (i.e. few-shot), and provide a method that leverages pre-trained embeddings to generalize the classification.

This library will gather several state-of-the-art techniques. We will present the concepts behind each algorithm and its implementation in the section below.

## Pre-trained WordEmbedding and Cosine Similarity

Implementation of [Few-Shot Text Classification with Pre-Trained Word Embeddings and a Human in the Loop](https://arxiv.org/pdf/1804.02063.pdf) by Katherine Bailey and Sunny Chopra Acquia.

This simple approach relies on :
- computing the mean embedding of each class using a pre-trained word embedding (Word2Vec)
- for a new example, find the closest class using the cosine distance

We can illustrate it the following way :

![images](Images/nlp_fs_4.png)

The model performance on the test dataset we provide (`Datasets` folder) is the following:

![images](Images/perf_1.png)
