import pandas as import pd
from sklearn import model_selection

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
            shuffle,
            random_state = 42,
            multilabel_delimiter=','
        ):
        self.Dataframe = df
        self.target_cols = target_cols
        self.num_target = len(target_cols)
        self.problem_type = problem_type
        self.num_folds = num_folds
        self.shuffle = shuffle
        self.random_state = random_state
        self.multilabel_delimiter = multilabel_delimiter

        if self.shuffle is True:
            self.Dataframe = self.Dataframe.sample(frac=1).reset_index(drop=True)
        self.Dataframe['Kfold'] = -1



    def split(self):
        if self.problem_type in ('binaray_classification','multiclass_classification':
            if self.num_target != 1:
                raise Exception("Invalid number of targets for this problem type")
            target = self.target_cols[0]
            unique_values = self.Dataframe[target].nunique()

            if unique_values ==1:
                raise Exception("Only one type target value found!")
            elif unique_value > 1:
                kf = model_selection.StratifiedKFold(n_splits=self.num_folds,
                                                    shuffle=False)
                for fold,(train_idx,val_idx) in enumerate(kf.split(X = self.Dataframe,y=self.Dataframe[target])):
                    self.Dataframe.loc[val_idx,'kfold'] = 
            
        elif self.problem_type in ('single_col_regression','multi_col_regression'):
            if self.num_target != 1 and self.problem_type == 'single_col_regression':
                raise Exception("Invalid number of targets for this problem type")
            if self.num_target < 2 and self.problem_type == 'multi_col_regression':
                raise Exception("Invalid number of targets for this problem type")
            kf = model_selection.KFold(n_splits=self.num_folds)
            for fold,(train_idx,val_idx) in enumerate(kf.split(X=self.Dataframe)):
                self.Dataframe.loc[val_idx,'kfold'] = fold
        elif self.problem_type.startswith('holdout_'):
            holdout_percentage = int(self.problem_type.split('_')[1])
            num_holdout_samples = int(len(self.Dataframe) * holdout_percentage / 100)
            self.Dataframe.loc[:len(self.Dataframe) - num_holdout_samples,"kfold"]=0
            self.Dataframe.loc[len(self.Dataframe) - num_holdout_samples:,"kfold"] = 1
        elif self.problem_type == "multilabel_classification":
            if self.num_target != 1:
                raise Exception("Invalid number of targets for this problem type")
            target = self.Dataframe[self.target_cols[0]].apply(lambda x: len(str(x).split(self.multilabel_delimiter)))
            kf = model_selection.StratifiedKFold(n_splits = self.num_folds)
            for fold, (train_idx,val_idx) in enumerate(kf.split(X = self.Dataframe,y = targets)):
                self.Dataframe.loc[val_idx,'kfold'] = fold
        else:
            raise Exception("Problem Type not Understood")
        return self.Dataframe
if __name__ == "__main__":
    df = pd.read_csv("../input/train.csv")
    cv = CrossValidation(df,shuffle=True,target_cols=['attribute_ids'],
                    problem_type='multilabel_classification',multilabel_delimiter=" ")
                    df_split = cv.split()
                    print(df_split.head())
                    print(df_split.kfold.value_counts())


            

            





