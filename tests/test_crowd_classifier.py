from ads.crowd_classifier import CrowdClassifier
from ads.ad_classes import AdClasses

def test_should_resolve_generic_ad_class_for_empty_list():
    crowd_classifier = CrowdClassifier()
    assert crowd_classifier.classify([]) == AdClasses.GENERIC