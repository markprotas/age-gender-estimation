import pytest

from ads.crowd_classifier import CrowdClassifier
from ads.ad_classes import AdClasses
from ads.identified_face import IdentifiedFace


@pytest.fixture
def crowd_classifier():
    return CrowdClassifier()


def test_should_resolve_generic_ad_class_for_empty_list(crowd_classifier):
    assert crowd_classifier.classify([]) == AdClasses.GENERIC


def test_should_resolve_middle_aged_men_if_all_faces_identified_are_men_between_30_and_55(crowd_classifier):
    faces = [IdentifiedFace('M', 35), IdentifiedFace('M', 43), IdentifiedFace('M', 50)]
    assert crowd_classifier.classify(faces) == AdClasses.MIDDLE_AGED_MEN

def test_should_resolve_middle_aged_men_if_one_is_identified(crowd_classifier):
    faces = [IdentifiedFace('M', 35)]
    assert crowd_classifier.classify(faces) == AdClasses.MIDDLE_AGED_MEN

def test_should_resolve_families_if_mixed_genders_and_ages(crowd_classifier):
    faces = [IdentifiedFace('M', 42), IdentifiedFace('F', 38), IdentifiedFace('M', 7)]
    assert crowd_classifier.classify(faces) == AdClasses.FAMILIES