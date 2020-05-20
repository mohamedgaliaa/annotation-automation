from four_points_to_segmentation_handler import FourPointToSegmentationHandler
from item_auto_annotation_automation_handler import ItemAutoAnnotationHandler
from bbox_to_segmentation_handler import BBoxToSegmentationHandler
import keras.backend as K
import tensorflow as tf
import dtlpy as dl
import logging

logger = logging.getLogger('annotation.automation')


class ServiceRunner(dl.BaseServiceRunner):
    """
    Package runner class

    """

    def __init__(self, project_name, package_name):
        """
        Init package attributes here

        :return:
        """
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        K.set_session(tf.Session(config=config))

        self.four_points_to_segmentation_handler = FourPointToSegmentationHandler(project_name=project_name,
                                                                                  package_name=package_name)

        self.item_auto_annotation_automation_handler = ItemAutoAnnotationHandler(project_name=project_name,
                                                                                 package_name=package_name)

        self.bbox_to_segmentation_handler = BBoxToSegmentationHandler(project_name=project_name,
                                                                      package_name=package_name)

    def item_auto_annotation_automation(self, progress, item, config=None):
        """
        Auto annotate a platform item using maskrcnn

        :param progress:
        :param item: dl.Item
        :param config: optional - dictionary
        :return:
        """
        progress.logger.info('updating progress')
        progress.update(message='started maskrcnn')
        progress.logger.info('started maskrcnn')
        return self.item_auto_annotation_automation_handler.run(progress=progress,
                                                                item=item,
                                                                config=config)

    def four_points_to_segmentation(self, progress, item, annotations, config=None):
        """
        Converts a four points closed polygon into a segmentation

        :param progress:
        :param item: dl.Item
        :param annotations: list of annotations dict
        :param config: optional - dictionary
        :return:
        """
        progress.logger.info('updating progress')
        progress.update(message='started dextr')
        progress.logger.info('started dextr')
        return self.four_points_to_segmentation_handler.run(progress=progress,
                                                            item=item,
                                                            config=config,
                                                            annotations=annotations)

    def bbox_to_segmentation(self, progress, item, annotations, config=None):
        """
        Converts a bounding box into a segmentation

        :param progress:
        :param item: dl.Item
        :param annotations: list of annotations dict
        :param config: optional - dictionary
        :return:
        """
        progress.logger.info('updating progress')
        progress.update(message='started box2seg')
        progress.logger.info('started box2seg')
        return self.bbox_to_segmentation_handler.run(progress=progress,
                                                     item=item,
                                                     config=config,
                                                     annotations=annotations)
