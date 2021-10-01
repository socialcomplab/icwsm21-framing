# Studying Moral-based Differences in the Framing of Political Tweets

This repository contains the code for the paper `Studying Moral-based Differences in the Framing of Political Tweets`. ([Link to paper](https://ojs.aaai.org/index.php/ICWSM/article/view/18135) or [Link to preprint](https://arxiv.org/abs/2103.11853))

The paper deals with moral framing using five moral foundations: (a) care, (b) fairness, (c) loyalty, (d) authority, and (e) sanctity.  
The experiments are conducted in Austrian and US based Twitter data.  

Method: We capture the moral frames using the FrameAxis approach, which defines semantic axes in the latent space formed by word vectors. As resources, we use moral foundation dictionary version 2 to define moral words (consisting of positive virtue associated and negative vice-associated words) and use GloVe for their representation. Then, for each of the five moral axes, we assign one end to the centroid of virtues and vices to the other one. These axes are used to extract the moral bias (defined by the mean) and the moral intensity (defined by the variance in relation to its baseline bias) by aggregating contributions of words in a document, i.e., their cosine similarity with the axes. Finally, we apply a logistic regression classifier to investigate the learned coefficient for the different groups present in the datasets. 

TLDR: we find that different moral values are associated with different political messages spread by US & Austrian politicians via Twitter.

![Preview](preview.png)

## Structure

The repo consists of 5 notebooks corresponding to the following 5 sections in the paper:
- [Capturing Moral Frames](frame_axis.ipynb)
- [Validation of Moral Frame Axes](1_validation_of_moral_frame_axes.ipynb)
- [Validation on Annotated Tweets](2_validation_on_annotated_tweets.ipynb)
- [Moral-based Framing in US-based Tweets](3_moral_based_framing_in_us_based_tweets.ipynb)
- [Moral-based Framing in Austrian-based Tweets](4_moral_based_framing_in_austrian_based_tweets.ipynb)

Plots of the five moral axis are provided in [plots](plots/).  
Additonally, some example are outlined in [examples.ipynb](examples.ipynb).

## Cite

Bibtex for [Paper](https://ojs.aaai.org/index.php/ICWSM/article/view/18135):

```
@inproceedings{reiter2021studying,
  title={Studying Moral-based Differences in the Framing of Political Tweets},
  author={Reiter-Haas, Markus and Kopeinik, Simone and Lex, Elisabeth},
  booktitle={Proceedings of the International AAAI Conference on Web and Social Media},
  volume={15},
  pages={1085--1089},
  year={2021}
}
```
