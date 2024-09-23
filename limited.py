# These are the only requirements by ComfyUI Limited; torch and similar packages will not load.
# python.exe -s -m pip install aiohttp --no-warn-script-location

# For the ComfyUI Windows portable version, you will need to adjust the path to the root like this:
# ..\python_embedded\python.exe -s -m pip install aiohttp --no-warn-script-location

# If you decide to go the embedded route, download any Python embedded distribution and edit the .pth file so that 'import site' is uncommented.
# Since embedded distributions do not have pip, you can download pip.pyz, place it next to python.exe, and use it like this:
# python.exe -s pip.pyz install aiohttp requests --no-warn-script-location

# This list of custom nodes will load without errors (2024-09-23)
# git clone https://github.com/ltdrdata/ComfyUI-Manager
# git clone https://github.com/rgthree/rgthree-comfy
# git clone https://github.com/yolain/ComfyUI-Easy-Use
# git clone https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes
# git clone https://github.com/shiimizu/ComfyUI_smZNodes
# git clone https://github.com/pythongosssss/ComfyUI-Custom-Scripts
# git clone https://github.com/giriss/comfy-image-saver
# git clone https://github.com/54rt1n/ComfyUI-DareMerge
# git clone https://github.com/jags111/efficiency-nodes-comfyui
# git clone https://github.com/WASasquatch/was-node-suite-comfyui
# git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG
# git clone https://github.com/TinyTerra/ComfyUI_tinyterraNodes
# git clone https://github.com/Nourepide/ComfyUI-Allor
# git clone https://github.com/ltdrdata/ComfyUI-Impact-Pack
# git clone https://github.com/crystian/ComfyUI-Crystools
# git clone https://github.com/Fannovel16/comfyui_controlnet_aux
# git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus
# git clone https://github.com/spacepxl/ComfyUI-Florence-2
# git clone https://github.com/Acly/comfyui-inpaint-nodes
# git clone https://github.com/EllangoK/ComfyUI-post-processing-nodes
# git clone https://github.com/cubiq/ComfyUI_essentials
# git clone https://github.com/chflame163/ComfyUI_LayerStyle
# git clone https://github.com/BadCafeCode/masquerade-nodes-comfyui
# git clone https://github.com/receyuki/comfyui-prompt-reader-node

DEBUG = True # You can see which commands are being ignored during testing.
NO_INSTALLS = True # Prevent pip and git modules from doing its thing

import sys
from unittest.mock import MagicMock

modules_to_mock = [
	# primary ComfyUI modules
	'torch',
	'yaml',
	'safetensors',
	'safetensors.torch',
	'numpy',
	'PIL',
	'PIL.PngImagePlugin',
	'PIL.PngImagePlugin.PngInfo',
	'psutil',
	'torch.autograd',
	'torchvision',
	'torch.nn',
	'torch.nn.functional',
	'einops',
	'torch.utils',
	'torch.utils.checkpoint',
	'transformers',
	'scipy',
	'torchsde',
	'tqdm',
	'tqdm.auto',
	'scipy.stats',
	'requests',
	'typing_extensions',

	# secondary ComfyUI modules
	'torchaudio',
	'kornia',
	'kornia.filters',
	'kornia.morphology',
	'spandrel',

	# common when loading custom nodes
	'scipy.ndimage',

	# ComfyUI-Manager modules
	'git',
	'git.remote',
	'pip',
	'pip.freeze',
	'pip.main',

	# ComfyUI-Easy-Use modules
	'packaging',
	'lark',
	'cv2',
	'accelerate',
	'torch.distributed',
	'torchvision.transforms',
	'torchvision.transforms.functional',
	'diffusers',
	'diffusers.configuration_utils',
	'diffusers.models',
	'diffusers.models.modeling_utils',
	'diffusers.models.unets.unet_2d_blocks',

	# ComfyUI_Comfyroll_CustomNodes
	'matplotlib',
	'matplotlib.pyplot',
	'matplotlib.patches',
	'matplotlib.colors',

	# efficiency-nodes-comfyui
	'huggingface_hub',
	'simpleeval',

	# ComfyUI_smZNodes
	'compel',

	# Comfy-image-saver
	'piexif',
	'piexif.helper',

	# ComfyUI_essentials
	'torchvision.transforms.v2',

	# comfyui_controlnet_aux
	'scipy.ndimage.filters',
	'skimage',
	'skimage.measure',
	'torch.hub',

	# ComfyUI_essentials
	'torchvision.transforms.v2',

	# ComfyUI_IPAdapter_plus
	'einops.layers',
	'einops.layers.torch',

	# ComfyUI_tinyterraNodes

	# ComfyUI-Allor
	'PIL.Image',
	'onnxruntime',
	'pooch',
	'rembg',
	'rembg.sessions',

	# ComfyUI-BRIA_AI-RMBG

	# ComfyUI-Crystools
	'PIL.ExifTags',
	'PIL.JpegImagePlugin',
	'cpuinfo',
	'deepdiff',
	'pynvml',

	# ComfyUI-Custom-Scripts

	# ComfyUI-DareMerge

	# ComfyUI-Florence-2
	'transformers.dynamic_module_utils',

	# ComfyUI-Impact-Pack
	'segment_anything',
	'skimage',
	'skimage.measure',
	'torchvision.datasets',
	'torchvision.datasets.utils',
	'ultralytics',

	# comfyui-inpaint-nodes
	'torch.jit',

	# ComfyUI-post-processing-nodes

	# comfyui-prompt-reader-node

	# efficiency-nodes-comfyui
	'huggingface_hub',
	'simpleeval',

	# masquerade-nodes-comfyui
	'torchvision.ops',

	# rgthree-comfy

	# was-node-suite-comfyui
	'numba',

	# ComfyUI_LayerStyle
	'blend_modes',
	'huggingface_hub',
	'segment_anything',
	'segment_anything.modeling',
	'segment_anything.modeling.common',
	'timm',
	'timm.models',
	'timm.models.layers',
	'timm.models.registry',
	'torchvision.models',
	'torchvision.ops',
	'torchvision.ops.boxes',
	'wget',
]

# Example whitelist
whitelist = ['aiohttp']
# Function to remove whitelisted modules and their submodules
def remove_whitelisted_modules(modules, whitelist):
	return [module for module in modules if not any(module == w or module.startswith(w + '.') for w in whitelist)]
# Update modules_to_mock by removing whitelisted modules
modules_to_mock = remove_whitelisted_modules(modules_to_mock, whitelist)

if DEBUG:
	print(f"---------------Disabled modules by Limited: {modules_to_mock}")
for module in modules_to_mock:
	sys.modules[module] = MagicMock()

if 'psutil' in modules_to_mock:
	mock_psutil = sys.modules['psutil']
	mock_psutil.configure_mock(**{'virtual_memory': MagicMock(return_value=MagicMock(total=8 * 1024 * 1024 * 1024))})

if 'torch' in modules_to_mock:
	mock_torch = sys.modules['torch']
	mock_torch.cuda.mem_get_info.return_value = (1024 * 1024 * 1024, 2048 * 1024 * 1024)  # Example values in bytes
	mock_torch.device = MagicMock(return_value=MagicMock(type='cpu')) # Mock torch.device specifically
	# mock_torch.deviceGetCount.return_value = 0
	for layer in ['Linear', 'Conv1d', 'Conv2d', 'Conv3d', 'ConvTranspose1d', 'ConvTranspose2d', 'ConvTranspose3d', 'GroupNorm', 'LayerNorm', 'Embedding', 'Module']:
		setattr(mock_torch.nn, layer, MagicMock) #MagicMock without () somehow does the job

	class MockLayer(metaclass=type):
		def __init__(self, *args, **kwargs): pass
	setattr(mock_torch.nn, 'Sequential', MockLayer) #Avoid class TimestepEmbedSequential(nn.Sequential, TimestepBlock): TypeError: metaclass conflict
# End of blacklisting module load-------------------------------------------------------------------------------

if NO_INSTALLS:
	sys.modules['pip.freeze'].return_value = []

	import subprocess
	from types import SimpleNamespace
	# monkey-patch to Mock subprocess.check_output
	original_run = subprocess.run

	def mock_run(*args, **kwargs): # Needs more work to mimic each output from pip
		if 'pip' in args[0]:
			if DEBUG:
				print(f">\tHandle for intercepted subprocess.run pip command: {args}")
			if 'show' in args[0]:
				return SimpleNamespace(returncode=0, stdout='WARNING: Package(s) not found: ' + args[0][-1] + '\n', stderr='')
			if 'freeze' in args[0]:
				return SimpleNamespace(returncode=0, stdout='absl-py==2.1.0\naiohttp==3.10.4\n', stderr='')
			if 'list' in args[0]:
				return SimpleNamespace(returncode=0, stdout="Package                      Version\n---------------------------- --------------------\npip                          24.2\nsetuptools                   69.5.1\n", stderr='')
			if 'install' or 'uninstall' in args[0]:
				return SimpleNamespace(returncode=0, stdout='', stderr='')
			return SimpleNamespace(returncode=1, stdout='', stderr="ERROR: (see \"pip help\")\n")
		else:
			if DEBUG:
				print(f">\tNeed handle for Intercepted subprocess.run command: {args[0]}")
		return original_run(*args, **kwargs)

	subprocess.run = mock_run

	# monkey-patch to Mock subprocess.check_output
	original_check_output = subprocess.check_output

	def mock_check_output(*args, **kwargs): # Needs more work to mimic each output from pip
		if 'pip' in args[0]:
			if DEBUG:
				print(f">\tHandle for intercepted subprocess.check_output pip command: {args}")
			if 'show' in args[0]:
				return b'WARNING: Package(s) not found: ' + args[0][-1].encode() + b'\n'
			if 'freeze' in args[0]:
				return b'absl-py==2.1.0\naiohttp==3.10.4\n'
			if 'list' in args[0]:
				return b"Package                      Version\n---------------------------- --------------------\npip                          24.2\nsetuptools                   69.5.1\n"
			if 'install' or 'uninstall' in args[0]:
				return b''
			return b"ERROR: (see \"pip help\")\n"
		else:
			if DEBUG:
				print(f">\tNeed handle for Intercepted subprocess.check_output command: {args[0]}")
		return original_check_output(*args, **kwargs)

	subprocess.check_output = mock_check_output

	# monkey-patch to Mock subprocess.check_call
	original_check_call = subprocess.check_call

	def mock_check_call(*args, **kwargs):
		if 'pip' in args[0]:
			print(f">\tHandle for intercepted subprocess.check_call pip command: {args[0]}")
			return 0  # Simulate a successful pip command
		else:
			if DEBUG:
				print(f">\tNeed handle for subprocess.check_call command: {args[0]}")
		return original_check_call(*args, **kwargs)

	subprocess.check_call = mock_check_call

	import pip # Now we monkey-patch to ensure that no package get installed using pip.

	def pip_install_wrapper(args):
		if 'install' in args:
			if DEBUG:
				print(f">\tHandle for intercepted pip command: {' '.join(args)}")
			return SimpleNamespace(returncode=0, stdout='', stderr='')  # Return a zero exit code to indicate installed
		else:
			if DEBUG:
				print(f">\tNeed handle for Intercepted pip command: {args[0]}")
		return original_pip_main(args)

	# Save the original pip main function
	original_pip_main = pip.main if hasattr(pip, 'main') else pip._internal.main

	# Monkey-patch pip main function
	if hasattr(pip, 'main'):
		pip.main = pip_install_wrapper
	else:
		pip._internal.main = pip_install_wrapper
# End of installer modules ------------------------------------------------------------------------

if 'diffusers' in modules_to_mock:
	import importlib.metadata
	# Save the original function
	original_version = importlib.metadata.version
	# Define the monkeypatched version function for ComfyUI-Easy-Use checks
	def mock_version(package):
		if package == "diffusers":
			return "0.27.2"
		print(f">\tmock_version package: {package}")
		return original_version(package)
	# Apply the monkeypatch
	importlib.metadata.version = mock_version

import importlib.util
# Mock the find_spec function globally for ComfyUI-Easy-Use, ComfyUI_smZNode
original_find_spec = importlib.util.find_spec
importlib.util.find_spec = MagicMock(return_value=None)

# Mock the module class to have the same metaclass as type
class MockTypeMetaclass:
	pass
# for ComfyUI-Allor avoid class CustomAbstractSession(CustomBaseSession, CustomSessionContainer): TypeError: metaclass conflict
if 'rembg.sessions' in modules_to_mock:
	sys.modules['rembg.sessions'].BaseSession = MockTypeMetaclass
# for ComfyUI_LayerStyle avoid class class BiRefNet(nn.Module, PyTorchModelHubMixin): TypeError: metaclass conflict
if 'huggingface_hub' in modules_to_mock:
	class MockNNModule(type): # Mock nn.Module as a subclass of type
		def __init_subclass__(cls, **kwargs):
			pass
	sys.modules['torch.nn'].Module = MockNNModule
	class MockPyTorchModelHubMixin(MockNNModule): # Mock PyTorchModelHubMixin as a subclass of MockNNModule
		def __init_subclass__(cls, **kwargs):
			pass
	sys.modules['huggingface_hub'].PyTorchModelHubMixin = MockPyTorchModelHubMixin

if 'timm' in modules_to_mock:
	sys.modules['timm.models.layers'].DropPath = MockTypeMetaclass
	sys.modules['timm.models.layers'].to_2tuple = MockTypeMetaclass
	sys.modules['timm.models.layers'].trunc_normal_ = MockTypeMetaclass
# for ComfyUI-Crystools pynvml.nvmlDeviceGetCount return 0
if 'pynvml' in modules_to_mock:
	sys.modules['pynvml'].nvmlDeviceGetCount.return_value = 0
# End of specific checks by custom nodes------------------------------------------------------------


# Now you can run the original main.py from ComfyUI with Limited functionality
import os

force_arg = ["--cpu"]
# Check if custom --port is provided by console command, else leave ComfyUI default port 8188 free.
if "--port" not in sys.argv:
	force_arg += ["--port", "8189"]

# Mimic the behavior of the "python -s" option by removing user site-packages
if hasattr(sys, 'base_prefix'):
	user_site = os.path.join(sys.base_prefix, 'lib', 'python' + sys.version[:3], 'site-packages')
	if user_site in sys.path:
		sys.path.remove(user_site)

# Construct the path to ComfyUI's main.py dynamically
main_path = os.path.join(os.path.dirname(__file__), 'main.py')

# Run main.py with arguments
if __name__ == "__main__":
	sys.argv = [main_path] + sys.argv[1:] + force_arg
	with open(main_path) as f:
		code = compile(f.read(), main_path, 'exec')
		exec(code)
