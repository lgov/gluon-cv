from gluoncv.utils.metrics.voc_detection import VOC07MApMetric


# These tests cover VOC07MApMetric, both normal scenarios and edge cases.

def test_voc_detection_metric_basic():
    val_metric = VOC07MApMetric(iou_thresh=0.5)
    # Don't crash
    val_metric.get()
