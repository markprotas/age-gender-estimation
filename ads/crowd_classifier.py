from ads.ad_classes import AdClasses


class CrowdClassifier(object):
    def classify(self, gender_age_tuples):
        if len(gender_age_tuples) > 0:
            if all(ga.gender == 'M' for ga in gender_age_tuples):
                return AdClasses.MIDDLE_AGED_MEN
            return AdClasses.FAMILIES
        return AdClasses.GENERIC
