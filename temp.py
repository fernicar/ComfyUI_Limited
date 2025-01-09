import sys
from unittest.mock import MagicMock

# MagicMoking ultralytics module because it is not installed in the environment
modules_to_mock = [
    "ultralytics",
    "ultralytics.utils",
    "ultralytics.utils.loss",
]
for module in modules_to_mock:
    sys.modules[module] = MagicMock()

# Define a mock class with a compatible metaclass
class MockE2EDetectLoss(metaclass=type):
    pass

# Create a mock for the ultralytics.utils.loss module
mock_loss_modules = sys.modules['ultralytics.utils.loss']
mock_loss_modules.E2EDetectLoss = MockE2EDetectLoss

# Now you can use the third-party code without errors
# this third-party code can not be modified
import ultralytics.utils.loss as loss_modules

aliasv10DetectLoss = type("v10DetectLoss", (loss_modules.E2EDetectLoss,), {})
print("Mock class created successfully")