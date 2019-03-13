from ads.ad_classes import AdClasses


class CrowdClassifier(object):
    def classify(self, gender_age_tuples):
        return AdClasses.GENERIC