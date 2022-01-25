import numpy as np

class DecisionTreeClassifier:

    def fit(self, X, y):
        self.classes_ = set(y)
        self.n_classes_ = len(self.classes_)
        self.n_features_ = X.shape[1]

    def split_on(self, X, y):
        # if there is only zero or one datapoint remaining its not even worth testing to split it
        number_of_samples = y.shape[0]
        if(number_of_samples <= 1):
            return None, None  
        # calculate the current gini score of this node
        classes_in_node = [np.sum(y == c) for c in self.classes_]
        node_gini_impurity = 1 - sum([samples_in_bucket / number_of_samples for samples_in_bucket in classes_in_node])
        