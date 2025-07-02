# Predicting Oral Drug Elimination Half-life In Humans Using Regression Models
This repo contains the independent research project of my Senior Thesis, conducted from June 2023 to May 2025. 

## Abstract
  In drug development, the elimination half-life, or the time it takes for half of a drug to be excreted from the body, is a critical factor in determining the effectiveness of a drug. However, determining half-life with clinical tests is often time-consuming and expensive. This project studied the use of regression models with different molecular fingerprints in order to predict elimination half-life. The data consisted of 1645 drugs, their molecular structure represented by a SMILES string, and their half-lives. Traditional SMILES strings are difficult to use with supervised learning models, so Extended-Connectivity Fingerprints (ECFPs) and a molecular fingerprint used to predict logP, logS, and logBB were used for representations of molecular structure. Models used were Linear Least Squares, Random Forest, SVR, SGDR, and XGBoost. Benchmarks show that SVR and Random Forest models that were trained with ECFPs produced the best predictions. 

## Additional Work
Check out my senior thesis paper [here](https://docs.google.com/document/d/1C1_kjGoyhx8V5uNx3NdTx2Vd4aDwjWU50ewxMySKC18/edit?usp=sharing)! 
Also check out my slide deck, which I presented to my school, right [here](https://docs.google.com/presentation/d/1zWgq9-1N3qztLdnUXXn93dwPdod0lUTxRdZcEbEJz9w/edit?usp=sharing).

### Questions about my work? Let me know at songmichael11@gmail.com!
