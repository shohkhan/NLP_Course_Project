1. Splitting the dataset:
	i. split -l 1215433 nlp_dataset this will divide the dataset into 2 parts, first part used for training language model. This gave us nlp_train and nlp_test files.
	ii. split -l 810288 nlp_dataset this will divide the dataset into 3 parts, first part used for training language model

2. Running language models for three experimental setups:
	python lm_lm_all_tokens.py > test1
	python lm_verb_noun_tri.py > test2
	python lm_verb_noun_uni.py > test3

3. Running NB and NN classifiers over the data:
	python classifier.py
