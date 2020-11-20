
'''
Binary Classification
Multiclass Classification
Multi label Classification
sigle Column Regression
Multi Column Regression
Holdout
'''



class CrossValidation:
    def __init__(
            self,
            df,
            target_cols,
            problem_type='binary_classification',
            num_folds=5,
            shuffle=True,
            random_state = 42
        ):
        self.Dataframe = df
        self.target_cols = target_cols
        self.num_target = len(target_cols)
        self.problem_type = problem_type
        self.num_folds = num_folds
        self.shuffle = shuffle
        self.random_state = random_state

        if self.shuffle is True:
            self.Dataframe = self.Dataframe.sample(frac=1).reset_index(drop=True)



    def split(self):
        if self.problem_type == 'binaray_classification':
            if unique_value ==1:
                raise Exception("Only one type target value found!")
            elif unique_value > 1:
                target = self.target_cols[0]
                kf = model_selection.StratifiedKFold((n_splits=self.num_folds, shuffle=self.shuffle, random_state=self.random_state))
                




