# fsTC : Few-Shot Text Classification

<img alt="GitHub contributors" src="https://img.shields.io/github/contributors-anon/maelfabien/FewShotTextClassification.svg"> <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/3.svg">
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](.github/CODE_OF_CONDUCT.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

*Use Case* : A user has a column of short texts (e.g user reviews) but those comments are not labeled. We ask the user to hand-label just a few texts for each class (i.e. few-shot), and provide a method that leverages pre-trained embeddings to generalize the classification.

This library will gather several state-of-the-art techniques. We will present the concepts behind each algorithm and its implementation in the section below.

## Table of Contents <!-- omit in toc -->

- [Installation](#Installation)
  - [With pip](#With-pip)
  - [From source](#From-source)
- [Implemented Models](#Models)
- [Getting started](#Getting-started)
  - [Preparing your data](#Preparing-your-data)
  - [Downloading pre-trained models](#Downloading-pre-trained-models)
  - [Training models](#Training-models)
  - [Making predictions](#Making-predictions)
  - [Evaluating models](#Evaluating-models)
- [Notebook Examples](#Notebook-Examples)
- [Contributing](#Contributing)
- [References](#References)
- [LICENSE](#LICENSE)

## Installation

### With pip

(To come)

```shell
pip install fsTC
```

### From source

```shell
git clone https://github.com/fsTC-suite/fsTC.git
cd cdQA
pip install -e .
```

## Implemented Models

### Pre-trained WordEmbedding and Cosine Similarity

Implementation of [Few-Shot Text Classification with Pre-Trained Word Embeddings and a Human in the Loop](https://arxiv.org/pdf/1804.02063.pdf) by Katherine Bailey and Sunny Chopra Acquia.

This simple approach relies on :
- computing the mean embedding of each class using a pre-trained word embedding (Word2Vec)
- for a new example, find the closest class using the cosine distance

We can illustrate it the following way :

![images](Images/nlp_fs_4.png)

The model performance on the test dataset we provide (`Datasets` folder) is the following:

![images](Images/perf_1.png)

### Pre-trained WordEmbedding and Classifier

Extension of [Few-Shot Text Classification with Pre-Trained Word Embeddings and a Human in the Loop](https://arxiv.org/pdf/1804.02063.pdf) by Katherine Bailey and Sunny Chopra Acquia.

This approach relies on :
- apply data augmentation (replace, delete, insert, swap words)
- computing the different embeddings for each class using a pre-trained word embedding (Word2Vec)
- fit a classifier (K-NN, Random Forest) on the training samples
- for a new example, use the trained classifier

The model performance on the test dataset we provide (`Datasets` folder) is the following:

![images](Images/perf_2.png)

## Getting started

### Preparing your data

We offer a text pre-processing pipeline as well as data augmentation techniques. To use `fstc` you need to create a Pandas DataFrame with the following columns:

| Text              | Label               |
| ----------------- | --------------------|
| First short text  | Label of first text |

### Training models

Fit the cosine classifier on your annotated texts:

```python
from fsTC.cosine_classifier import *

clf = cosine_classifier()
clf.fit(X_train, y_train)
```

We include an automated label encoding of `y_train` which can therefore take any form.

### Making predictions

To get the prediction on the rest of your un-labeled texts:

```python
clf.predict(X_test)
```

## Notebook Examples

We prepared some notebook examples under the [examples](examples) directory.

You can also play directly with these notebook examples using [Binder](https://gke.mybinder.org/) or [Google Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb):

| Notebook | Description |
| --- | --- |
| [1] FewShot | A simple demonstration of fsTC pre-trained WordEmbeddings classifers |
| [2] DLFewShot | Extension leveraging Deep-Learning approaches |

## Contributing

Read our [Contributing Guidelines](.github/CONTRIBUTING.md).

## References

| Type                 | Title                                                                                                                                        | Author                                                                                 | Year |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ---- |
| :newspaper: Paper    | [One-shot and few-shot learning of word embeddings](https://arxiv.org/abs/1710.10280)                 | Andrew K. Lampinen & James L. McClelland                                   | 2018 |

## LICENSE

[Apache-2.0](LICENSE)

