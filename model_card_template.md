# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
    - Name: Classifying for Predicting salary brackets
    - Type: classification
    - Algorithm: RandomForestClassifier
    - Description: Model predicts whether an individual makes more than $50,000/year based on demographic and employment features. Identifies 'high income' earners using census data.

## Intended Use
    - classify individuals into 2 brackets, whether or not they earn more than $50,000/year

## Training Data
    - Dataset: https://archive.ics.uci.edu/dataset/2/adult

## Evaluation Data
    - Split from original census data
    - Size: 20% of original dataset

## Metrics
    - Precision: 0.7444
    - Recall: 0.6321
    - F1 score: 0.6836

## Ethical Considerations
    - Model performance will vary across different demographics. We must consider the models bias regarding gender, race, or other attributes.
    - Ensure data is handled in compliance with safetty and privacy regulations

## Caveats and Recommendations
    - Ensure clean data for best performance.
    - Model does not generalize to other datasets.
