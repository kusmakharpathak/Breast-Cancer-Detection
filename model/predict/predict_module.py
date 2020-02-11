from sklearn.externals import joblib
import numpy as np


class Predict:

    def __init__(self, mean_radius, mean_perimeter, mean_area, radius_worst, perimeter_worst):
        self.mean_radius = mean_radius
        self.mean_perimeter = mean_perimeter
        self.radius_worst = radius_worst
        self.perimeter_worst = perimeter_worst
        self.mean_area = mean_area

    def predict(self):
        diagnosis = [
            self.mean_radius,
            self.mean_perimeter,
            self.mean_area,
            self.radius_worst,
            self.perimeter_worst,
                     ]

        print(diagnosis)
        test_data = np.array(diagnosis).reshape(-1, 5)
        print(test_data)
        load_module = joblib.load("E:\\Python\\BreastCancer\\model\\predict\\Final_finalized_model.sav")
        result = load_module.predict(test_data)
        print(result)

        # Diagnosis(M=malignant, B=benign)

        if load_module.predict(test_data) == 'B':
            return True
        else:
            return False


# a = Predict(7.76, 47.92, 181.0, 9.456, 59.16)
# a.predict()
# if a.predict():
#     print("Yes")
# else:
#     print("No")
