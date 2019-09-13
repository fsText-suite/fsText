# fsText : Few-Shot Text Classification

<img alt="GitHub contributors" src="https://img.shields.io/github/contributors-anon/maelfabien/FewShotTextClassification.svg"> <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/3.svg">
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](.github/CODE_OF_CONDUCT.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

🚧 ! This library is currently a work in progress !

*Use Case* : A user has a column of short texts (e.g user reviews) but the comments are not labeled. We ask the user to hand-label just a few texts of each class (i.e. few-shot), and provide a method that leverages pre-trained embeddings to generalize the classification to the whole dataset.

This library will gather several state-of-the-art techniques. We will present the concepts behind each algorithm and its implementation in the section below.

## Table of Contents <!-- omit in toc -->

- [Installation](#Installation)
  - [With pip](#With-pip)
  - [From source](#From-source)
- [Implemented Models](#Models)
- [Getting started](#Getting-started)
  - [Preparing your data](#Preparing-your-data)
  - [Training models](#Training-models)
  - [Making predictions](#Making-predictions)
- [Notebook Examples](#Notebook-Examples)
- [Contributing](#Contributing)
- [References](#References)
- [LICENSE](#LICENSE)
- [Contacts and Contributors](#LICENSE)

## Installation

### With pip

```shell
pip install fsText
```

### From source

```shell
git clone https://github.com/maelfabien/fsText.git
cd fsText
pip install -e .
```

## Implemented Models


| Model              | Status               | Details | Reference Paper |
| ----------------- | --------------------| -------------------- | -------------------- |
| Word2Vec + Cosine Similarity  | ✅ | [Article](https://maelfabien.github.io/machinelearning/NLP_5/) | [Few-Shot Text Classification with Pre-Trained Word Embeddings and a Human in the Loop](https://arxiv.org/abs/1804.02063) |
| Word2Vec + Advanced Classifiers  | 🚧 | [Article](https://maelfabien.github.io/machinelearning/NLP_6/) | [Few-Shot Text Classification with Pre-Trained Word Embeddings and a Human in the Loop](https://arxiv.org/abs/1804.02063) |
| DistilBert + Advanced Classifier  | 🚧 | [Article](https://maelfabien.github.io/machinelearning/NLP_7/) | --- |
| Siamese Network | ❌ | [Article](https://data4thought.com/fewshot_learning_nlp.html) | --- |
| Fine-Tuning Pre-trained Bert | ❌ | --- | [Improving Few-shot Text Classification via Pretrained Language Representations](https://arxiv.org/abs/1908.08788) |

## Getting started

### Preparing your data

We offer a text pre-processing pipeline as well as data augmentation techniques. To use `fsText` you need to create a Pandas DataFrame with the following columns:

| Text              | Label               |
| ----------------- | --------------------|
| First short text  | Label of first text |

### Training models

Fit the cosine classifier on your annotated texts:

```python
from fsText.Classifier import CosineClassifier

clf = CosineClassifier()
clf.fit(X_train, y_train)
```

We include an automated label encoding of `y_train` which can therefore take any form.

### Making predictions

To get the prediction on the rest of your un-labeled texts:

```python
clf.predict(X_test)
```

To assess the accuracy of the prediction in case you have a labeled dataset:

```python
from sklearn.metrics import accuracy_score
accuracy_score(clf.predict(X_test), y_test)
```

## Notebook Examples

We prepared some notebook examples under the [examples](examples) directory.

You can also play directly with these notebook examples using [Binder](https://gke.mybinder.org/) or [Google Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb):

| Notebook | Description |
| --- | --- |
| [1] CosineClassifierDemo | A simple demonstration of fsText Cosine Classifier + Word2Vec |

## Contributing

Read our [Contributing Guidelines](.github/CONTRIBUTING.md).

## References

| Type                 | Title                                                                                                                                        | Author                                                                                 | Year |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ---- |
| :newspaper: Paper    | [One-shot and few-shot learning of word embeddings](https://arxiv.org/abs/1710.10280)                 | Andrew K. Lampinen & James L. McClelland                                   | 2018 |
| :newspaper: Paper    | [Few-Shot Text Classification with Pre-Trained Word Embeddings and a Human in the Loop](https://arxiv.org/abs/1804.02063)                | Katherine Bailey, Sunny Chopra                                  | 2018 |
| :newspaper: Paper    | [Improving Few-shot Text Classification via Pretrained Language Representations](https://arxiv.org/abs/1908.08788)                | Ningyu Zhang, Zhanlin Sun, Shumin Deng, Jiaoyan Chen, Huajun Chen                                   | 2019 |

## LICENSE

[Apache-2.0](LICENSE)

## Contacts and contributors

<table><tr><td align="center">
<td align="center">
<a href="https://github.com/andrelmfarias"><img src="https://avatars3.githubusercontent.com/u/43521764?s=400&v=4" width="100px;" alt="mfix22"/>
<br /><sub><b>andrelmfarias</b></sub>
</a><br /><a href="https://github.com/maelfabien/fsTC/commits?author=andrelmfarias" title="Code">💻      </a></td>
</td>
<td align="center">
<a href="https://github.com/mamrouch"><img src="https://avatars3.githubusercontent.com/u/29277719?s=400&v=4" width="100px;" alt="mfix22"/>
<br /><sub><b>mamrouch</b></sub>
</a><br /><a href="https://github.com/maelfabien/fsTC/commits?author=mamrouch" title="Code">💻      </a></td>
</td>
<td align="center">
<a href="https://github.com/maelfabien"><img src="https://avatars0.githubusercontent.com/u/24256555?v=4" width="100px;" alt="mfix22"/>
<br /><sub><b>maelfabien</b></sub>
</a><br /><a href="https://github.com/maelfabien/fsTC/commits?author=maelfabien" title="Code">💻      </a></td>
</td>
</tr></table>
