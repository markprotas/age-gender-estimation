from ads.ad_classes import AdClasses


class CrowdClassifier(object):
    def classify(self, gender_age_tuples):
        if len(gender_age_tuples) > 1:
            return AdClasses.MIDDLE_AGED_MEN
        return AdClasses.GENERIC
