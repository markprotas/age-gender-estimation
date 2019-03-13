import cv2


class AdRenderer(object):
    def render(self, ad_class):
        img = cv2.imread("images/" + ad_class.get_image_path())
        cv2.imshow('img', img)