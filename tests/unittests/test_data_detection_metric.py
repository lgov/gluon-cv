from gluoncv.utils.metrics.voc_detection import VOC07MApMetric

import numpy as np

# These tests cover VOC07MApMetric, both normal scenarios and edge cases.

def test_voc_detection_metric_basic():
    val_metric = VOC07MApMetric(iou_thresh=0.5)
    # Don't crash
    try:
        val_metric.get()
    except AssertionError:
        # Good, expected.
        return
    assert False, "val_metric.get() without update() first should have failed with assertion."
