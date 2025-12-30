from abc import ABC, abstractmethod

class MLModel(ABC):
    @abstractmethod
    def preprocess_data(self, data, y):
        pass

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass


class SVM(MLModel):
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at SVM")

    def fit(self):
        print("Training at SVM")

    def predict(self):
        print("Evaluating at SVM")


class DecisionTree(MLModel):
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at DecisionTree")

    def fit(self):
        print("Training at DecisionTree")

    def predict(self):
        print("Evaluating at DecisionTree")


svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()

dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()