# https://github.com/fernicar/ComfyUI_Limited
# These are the only requirements by ComfyUI Limited; torch and similar packages will not load.
# python.exe -s -m pip install aiohttp --no-warn-script-location

# For the ComfyUI Windows portable version, you will need to adjust the path to the root like this:
# ..\python_embedded\python.exe -s -m pip install aiohttp --no-warn-script-location

# If you decide to go the embedded route, download any Python embedded distribution and edit the .pth file so that 'import site' is uncommented.
# Since embedded distributions do not have pip, you can download pip.pyz, place it next to python.exe, and use it like this:
# python.exe -s pip.pyz install aiohttp --no-warn-script-location

""" This list of custom nodes will load without errors (2025-01-06)
git clone --depth 1 --filter=blob:none https://github.com/ltdrdata/ComfyUI-Manager
git clone --depth 1 --filter=blob:none https://github.com/rgthree/rgthree-comfy
git clone --depth 1 --filter=blob:none https://github.com/yolain/ComfyUI-Easy-Use
git clone --depth 1 --filter=blob:none https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes
git clone --depth 1 --filter=blob:none https://github.com/shiimizu/ComfyUI_smZNodes
git clone --depth 1 --filter=blob:none https://github.com/pythongosssss/ComfyUI-Custom-Scripts
git clone --depth 1 --filter=blob:none https://github.com/giriss/comfy-image-saver
git clone --depth 1 --filter=blob:none https://github.com/alexopus/ComfyUI-Image-Saver
git clone --depth 1 --filter=blob:none https://github.com/54rt1n/ComfyUI-DareMerge
git clone --depth 1 --filter=blob:none https://github.com/jags111/efficiency-nodes-comfyui
git clone --depth 1 --filter=blob:none https://github.com/WASasquatch/was-node-suite-comfyui
git clone --depth 1 --filter=blob:none https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG
git clone --depth 1 --filter=blob:none https://github.com/TinyTerra/ComfyUI_tinyterraNodes
git clone --depth 1 --filter=blob:none https://github.com/Nourepide/ComfyUI-Allor
git clone --depth 1 --filter=blob:none https://github.com/ltdrdata/ComfyUI-Impact-Pack
git clone --depth 1 --filter=blob:none https://github.com/ltdrdata/ComfyUI-Impact-Subpack ComfyUI-Impact-Pack/impact_subpack
git clone --depth 1 --filter=blob:none https://github.com/crystian/ComfyUI-Crystools
git clone --depth 1 --filter=blob:none https://github.com/Fannovel16/comfyui_controlnet_aux
git clone --depth 1 --filter=blob:none https://github.com/cubiq/ComfyUI_IPAdapter_plus
git clone --depth 1 --filter=blob:none https://github.com/spacepxl/ComfyUI-Florence-2
git clone --depth 1 --filter=blob:none https://github.com/Acly/comfyui-inpaint-nodes
git clone --depth 1 --filter=blob:none https://github.com/EllangoK/ComfyUI-post-processing-nodes
git clone --depth 1 --filter=blob:none https://github.com/cubiq/ComfyUI_essentials
git clone --depth 1 --filter=blob:none https://github.com/chflame163/ComfyUI_LayerStyle
git clone --depth 1 --filter=blob:none https://github.com/chflame163/ComfyUI_LayerStyle_Advance
git clone --depth 1 --filter=blob:none https://github.com/BadCafeCode/masquerade-nodes-comfyui
git clone --depth 1 --filter=blob:none https://github.com/receyuki/comfyui-prompt-reader-node --recursive
git clone --depth 1 --filter=blob:none https://github.com/M1kep/ComfyLiterals
git clone --depth 1 --filter=blob:none https://github.com/WASasquatch/ComfyUI_Preset_Merger
git clone --depth 1 --filter=blob:none https://github.com/filliptm/ComfyUI_Fill-Nodes
git clone --depth 1 --filter=blob:none https://github.com/ssitu/ComfyUI_UltimateSDUpscale --recursive
git clone --depth 1 --filter=blob:none https://github.com/Ttl/ComfyUi_NNLatentUpscale
git clone --depth 1 --filter=blob:none https://github.com/huchenlei/ComfyUI-layerdiffuse
git clone --depth 1 --filter=blob:none https://github.com/BlenderNeko/ComfyUI_ADV_CLIP_emb
git clone --depth 1 --filter=blob:none https://github.com/comfyanonymous/ComfyUI_experiments
git clone --depth 1 --filter=blob:none https://github.com/bvhari/ComfyUI_ImageProcessing
git clone --depth 1 --filter=blob:none https://github.com/Jcd1230/rembg-comfyui-node
git clone --depth 1 --filter=blob:none https://github.com/Loewen-Hob/rembg-comfyui-node-better
git clone --depth 1 --filter=blob:none https://github.com/Mamaaaamooooo/batchImg-rembg-ComfyUI-nodes
git clone --depth 1 --filter=blob:none https://github.com/Derfuu/Derfuu_ComfyUI_ModdedNodes
git clone --depth 1 --filter=blob:none https://github.com/fssorc/ComfyUI_FaceShaper
git clone --depth 1 --filter=blob:none https://github.com/Acly/comfyui-tooling-nodes
git clone --depth 1 --filter=blob:none https://github.com/asagi4/comfyui-prompt-control
"""

DEBUG = False # You can see which commands are being ignored during testing.
NO_INSTALLS = True # Prevent pip and git modules from doing its thing

import sys
import os
import re
import traceback
import importlib
from unittest.mock import MagicMock
import importlib.metadata
import importlib.util

modules_to_mock = [
    # primary ComfyUI modules
    'torch',
    'yaml',
    'safetensors',
    'safetensors.torch',
    'numpy',
    'numpy.dtypes',
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
    'scipy.ndimage.filters',

    # ComfyUI-Manager modules
    'git',
    'git.remote',
    'pip',
    'pip.freeze',
    'pip.main',
]

# Path to the text file containing module names
whitelist_path = os.path.join(os.path.dirname(__file__), 'limited_whitelist.log')

# Example whitelist
whitelist = ['aiohttp']
# Read the module names from the file
if os.path.exists(whitelist_path):
    with open(whitelist_path, 'r') as file:
        modules = file.read().splitlines()
        whitelist.extend(modules)

# Import each module dynamically
for module_name in whitelist:
    try:
        module = importlib.import_module(module_name)
        if DEBUG: print(f">\tSuccessfully imported {module_name}")
    except ImportError as e:
        if DEBUG: print(f">\tError importing {module_name}: {e}")

# # Save the original import_module function
# original_import_module = importlib.import_module

# def safe_import_module(name, package=None):
#     try:
#         module = original_import_module(name, package)
#         # Check for required attributes
#         if not hasattr(module, 'NODE_CLASS_MAPPINGS') or not hasattr(module, 'NODE_DISPLAY_NAME_MAPPINGS'):
#             if DEBUG: print(f">\tModule {name} does not have the required attributes.")
#             # return None
#         return module
#     except ImportError as e:
#         if DEBUG: print(f">\tError importing {module_name}: {e}")
#         return None

# # Monkey-patch importlib.import_module
# importlib.import_module = safe_import_module

# Function to remove whitelisted modules and their submodules
def remove_whitelisted_modules(modules, whitelist):
    return [module for module in modules if not any(module == w or module.startswith(w + '.') for w in whitelist)]
# Update modules_to_mock by removing whitelisted modules
modules_to_mock = remove_whitelisted_modules(modules_to_mock, whitelist)

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
    if 'pip' in modules_to_mock:
        sys.modules['pip.freeze'].return_value = []

    import subprocess
    from types import SimpleNamespace
    # monkey-patch to Mock subprocess.check_output
    original_run = subprocess.run

    def mock_run(*args, **kwargs): # Needs more work to mimic each output from pip
        if 'pip' in args[0]:
            if DEBUG: print(f">\tHandle for intercepted subprocess.run pip command: {args}")
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
            if DEBUG: print(f">\tNeed handle for Intercepted subprocess.run command: {args[0]}")
        return original_run(*args, **kwargs)

    subprocess.run = mock_run

    # monkey-patch to Mock subprocess.check_output
    original_check_output = subprocess.check_output

    def mock_check_output(*args, **kwargs): # Needs more work to mimic each output from pip
        if 'pip' in args[0]:
            if DEBUG: print(f">\tHandle for intercepted subprocess.check_output pip command: {args}")
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
            if DEBUG: print(f">\tNeed handle for Intercepted subprocess.check_output command: {args[0]}")
        return original_check_output(*args, **kwargs)

    subprocess.check_output = mock_check_output

    # monkey-patch to Mock subprocess.check_call
    original_check_call = subprocess.check_call

    def mock_check_call(*args, **kwargs):
        if 'pip' in args[0]:
            if DEBUG: print(f">\tHandle for intercepted subprocess.check_call pip command: {args[0]}")
            return 0  # Simulate a successful pip command
        else:
            if DEBUG: print(f">\tNeed handle for subprocess.check_call command: {args[0]}")
        return original_check_call(*args, **kwargs)

    subprocess.check_call = mock_check_call

    import pip # Now we monkey-patch to ensure that no package get installed using pip.

    def pip_install_wrapper(args):
        if 'install' in args:
            if DEBUG: print(f">\tHandle for intercepted pip command: {' '.join(args)}")
            return SimpleNamespace(returncode=0, stdout='', stderr='')  # Return a zero exit code to indicate installed
        else:
            if DEBUG: print(f">\tNeed handle for Intercepted pip command: {args[0]}")
        return original_pip_main(args)

    # Save the original pip main function
    original_pip_main = pip.main if hasattr(pip, 'main') else pip._internal.main

    # Monkey-patch pip main function
    if hasattr(pip, 'main'):
        pip.main = pip_install_wrapper
    else:
        pip._internal.main = pip_install_wrapper
# End of installer modules ------------------------------------------------------------------------

# Mock the find_spec function globally for ComfyUI-Easy-Use, ComfyUI_smZNode
original_find_spec = importlib.util.find_spec
importlib.util.find_spec = MagicMock(return_value=None)

modules_with_applied_fixes = set()
def custom_fix(modules_to_mock):
    global whitelist
    global modules_with_applied_fixes
    # Mock the module class to have the same metaclass as type
    class MockTypeMetaclass:
        pass
    # for ComfyUI-Allor avoid class CustomAbstractSession(CustomBaseSession, CustomSessionContainer): TypeError: metaclass conflict
    module = 'rembg.sessions'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for ComfyUI-Allor avoid TypeError: metaclass conflict is applied")
        sys.modules[module].BaseSession = MockTypeMetaclass
    # for ComfyUI_LayerStyle avoid class BiRefNet(nn.Module, PyTorchModelHubMixin): TypeError: metaclass conflict
    module = 'huggingface_hub'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for ComfyUI_LayerStyle avoid TypeError: metaclass conflict is applied")
        class MockNNModule(type): # Mock nn.Module as a subclass of type
            def __init_subclass__(cls, **kwargs):
                pass
        sys.modules['torch.nn'].Module = MockNNModule
        class MockPyTorchModelHubMixin(MockNNModule): # Mock PyTorchModelHubMixin as a subclass of MockNNModule
            def __init_subclass__(cls, **kwargs):
                pass
        sys.modules[module].PyTorchModelHubMixin = MockPyTorchModelHubMixin
    # for ComfyUI-Crystools pynvml.nvmlDeviceGetCount return 0
    module = 'pynvml'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for ComfyUI-Crystools pynvml.nvmlDeviceGetCount return 0 is applied")
        sys.modules[module].nvmlDeviceGetCount.return_value = 0
    # for comfyui_controlnet_aux numpy.pi
    module = 'numpy'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for comfyui_controlnet_aux numpy.pi is applied")
        sys.modules[module].configure_mock(pi=3.14159265359)
    # for clipseg.py and ComfyUI_Comfyroll_CustomNodes unknown problem
    module = 'matplotlib'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for clipseg.py and ComfyUI_Comfyroll_CustomNodes unknown problem is applied")
        sys.modules['matplotlib.colors'] = MagicMock()
    # for ComfyUI-Easy-Use checks define the monkeypatched version function
    module = 'diffusers'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        original_version = importlib.metadata.version # Save the original function
        def mock_version(package):
            if package == "diffusers":
                return "0.27.2"
            if DEBUG: print(f">\tmock_version package: {package}")
            return original_version(package)
        importlib.metadata.version = mock_version # Apply the monkeypatch
    # for ComfyUI-layerdiffuse version checks define the monkeypatched parse function
    module = 'packaging.version'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for ComfyUI-layerdiffuse version checks from parse is applied")
        def mock_parse(version): # Define the custom parse function
            return version
        # Assign the custom parse function to the MagicMock object
        sys.modules[module].parse = mock_parse
    # for ComfyUI-layerdiffuse avoid class UNet1024(ModelMixin, ConfigMixin): TypeError: metaclass conflict
    module = 'diffusers.models.modeling_utils'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for ComfyUI-layerdiffuse avoid TypeError: metaclass conflict is applied")
        class MockModelMixin(type): # Mock ModelMixin as a subclass of type
                pass
        sys.modules[module].ModelMixin = MockModelMixin
        class MockConfigMixin(metaclass=MockModelMixin): # Mock MockConfigMixin as a subclass of MockModelMixin
                pass
        sys.modules['diffusers.configuration_utils'].ConfigMixin = MockConfigMixin
    # for comfyui-prompt-control version checks define the monkeypatched parse function
    module = 'lark'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for comfyui-prompt-control lark.__version__ checks is applied")
        # Assign the custom version to the MagicMock object
        sys.modules[module].__version__ = "1.2.0"
    # for efficiency-nodes-comfyui mocking simpleeval to get more nodes loaded
    module = 'efficiency-nodes-comfyui'
    if module in sys.modules and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        module_to_mock = 'simpleeval'
        if module_to_mock not in whitelist: 
            if DEBUG: print(f"\t>The Workaround efficiency-nodes-comfyui load simpleeval dependent nodes is applied for next restart")
            sys.modules[module_to_mock] = MagicMock()
            update_log_file(log_file_path, module_to_mock)
    # for ComfyUI-Impact-Subpack avoid aliasIterableSimpleNamespace = type("IterableSimpleNamespace", (IterableSimpleNamespace,), {}): TypeError: metaclass conflict
    module = 'ultralytics.utils'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for ComfyUI-Impact-Subpack avoid TypeError: metaclass conflict is applied")
        sys.modules['ultralytics.utils'].IterableSimpleNamespace = MockTypeMetaclass
    module = 'ultralytics.utils.tal'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for ComfyUI-Impact-Subpack avoid TypeError: metaclass conflict is applied")
        sys.modules['ultralytics.utils.tal'].TaskAlignedAssigner = MockTypeMetaclass
    module = 'ultralytics.nn.tasks'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for ComfyUI-Impact-Subpack avoid TypeError: metaclass conflict is applied")
        sys.modules['ultralytics.nn.tasks'].DetectionModel = MockTypeMetaclass
    module = 'ultralytics.utils.loss'
    if module in modules_to_mock and module not in modules_with_applied_fixes:
        modules_with_applied_fixes.add(module)
        if DEBUG: print(f">\tThe Workaround for ComfyUI-Impact-Subpack avoid TypeError: metaclass conflict is applied")
        import ultralytics.utils.loss as loss_modules
        loss_modules.E2EDetectLoss = MockTypeMetaclass


# End of specific checks by custom nodes------------------------------------------------------------

def patch_after_init_extra_nodes():
    if 'ComfyUI-Crystools' in sys.modules:
        module = sys.modules['ComfyUI-Crystools']
        if DEBUG: print(f'\n>----------sys.modules[\'ComfyUI-Crystools\']\n{dir(module)}')
        module.cmonitor.stopMonitor()
        def mock_startMonitor(*args, **kwargs):
            return None
        module.CMonitor.startMonitor = mock_startMonitor
        if DEBUG: print(f">\tThe Workaround for ComfyUI-Crystools hardware monitor crash is applied")
    custom_fix(sys.modules)

def get_modules_to_mock(log_file_path):
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as file:
            return file.read().splitlines()
    return []

def update_log_file(log_file_path, module_name):
    with open(log_file_path, 'a') as file:
        file.write(f"{module_name}\n")

def mock_modules(modules):
    for module in modules:
        if DEBUG: print(f'>\t{module} will be mocked')
        sys.modules[module] = MagicMock()
    custom_fix(modules)

def load_custom_node(module_path: str, ignore=set(), module_parent="custom_nodes"):
    module_name = os.path.basename(module_path)
    if os.path.isfile(module_path):
        sp = os.path.splitext(module_path)
        module_name = sp[0]
    try:
        if DEBUG: print(">\tTrying to mock requirements from custom node {}".format(module_path))
        if os.path.isfile(module_path):
            module_spec = importlib.util.spec_from_file_location(module_name, module_path)
        else:
            module_spec = importlib.util.spec_from_file_location(module_name, os.path.join(module_path, "__init__.py"))
        module = importlib.util.module_from_spec(module_spec)
        sys.modules[module_name] = module
        module_spec.loader.exec_module(module)
    except Exception as e:
        error_message = str(e)
        match = re.search(r"No module named '([^']+)'", error_message)
        if not match:
            match = re.search(r"([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)\.[a-zA-Z_][a-zA-Z0-9_]* failed to import", error_message)
        if not match or match in sys.modules:
            match = re.search(r"([^']+) failed to import", error_message)
        if match:
            if DEBUG: print(f'>\t{match.group(1)} from error_message: {e}')
            return match.group(1)
        # error_message = str(e).split("'")[0]
        # if error_message == 'No module named ':
        #     return str(e).split("'")[1]
        else:
            if DEBUG: print(f'>\t{module_name} needs Workaround for: {e}')
            if DEBUG: print(traceback.format_exc())
            exit()
            return False
    if module_name in sys.modules:
        del sys.modules[module_name]
    return True

log_file_path = os.path.join(os.path.dirname(__file__), 'limited_modules.log')
log_modules_to_mock = modules_to_mock
modules_to_mock = get_modules_to_mock(log_file_path)
log_modules_to_mock.extend(modules_to_mock)
mock_modules(modules_to_mock)
def retry_load_custom_node(module_path: str, ignore=set(), module_parent="custom_nodes") -> bool:
    global log_modules_to_mock
    retry_limit = 35
    retries = 0
    while retries < retry_limit:
        missing_module = load_custom_node(module_path, ignore, module_parent=module_parent)
        if missing_module is True:
            if DEBUG: print(f">\tSuccessfully imported {module_path}")
            return True
        else:
            if DEBUG: print(f">\tMissing module: {missing_module}")
            if missing_module in ignore:
                if DEBUG: print(f">\tIgnoring module: {missing_module}")
                return False
            modules_to_mock.append(missing_module)
            update_log_file(log_file_path, missing_module)
            mock_modules([missing_module])
            log_modules_to_mock.append(missing_module)
            retries += 1

    if retries == retry_limit:
        if DEBUG: print(f">\tFailed to import {module_path} after {retry_limit} retries")
        return False

if DEBUG: print(f">\t---------------Disabled modules by Limited: {log_modules_to_mock}")


# Now you can run the original main.py from ComfyUI with Limited functionality

force_arg = ["--cpu"]
# Check if custom --port is provided by console command, else leave ComfyUI default port 8188 free.
if "--port" not in sys.argv:
    force_arg += ["--port", "8189"]

# Mimic the behavior of the "python -s" option by removing user site-packages
if hasattr(sys, 'base_prefix'):
    user_site = os.path.join(sys.base_prefix, 'lib', 'site-packages')
    if user_site in sys.path:
        sys.path.remove(user_site)
# Remove global site-packages directory preventing installed modules to load if not whitelisted.
global_site = os.path.join(sys.prefix, 'lib', 'site-packages')
if global_site in sys.path:
    sys.path.remove(global_site)

# Construct the path to ComfyUI's main.py dynamically
main_path = os.path.join(os.path.dirname(__file__), 'main.py')

# Run main.py with arguments
if __name__ == "__main__":
    sys.argv = [main_path] + sys.argv[1:] + force_arg
    patterntext = "    nodes.init_extra_nodes(init_custom_nodes=not args.disable_all_custom_nodes)"
    replacement = """
    original_load_custom_node = nodes.load_custom_node
    def monkeypatch_load_custom_node(module_path: str, ignore=set(), module_parent="custom_nodes") -> bool:
        success = original_load_custom_node(module_path, ignore, module_parent)
        if not success:
            success = retry_load_custom_node(module_path, ignore, module_parent)
            success = original_load_custom_node(module_path, ignore, module_parent)
        return success
    nodes.load_custom_node = monkeypatch_load_custom_node
    nodes.init_extra_nodes(init_custom_nodes=not args.disable_all_custom_nodes)
    patch_after_init_extra_nodes()"""

    with open(main_path) as f:
        code = f.read()
        if patterntext in code:
            # Search init_extra_nodes and add patch_after_init_extra_nodes line
            code = code.replace(patterntext, replacement)
        else:
            raise ValueError("Expected pattern not found in main.py")
        try:
            code = compile(code, main_path, 'exec') # Compile and execute the modified code
            exec(code)
        except Exception as e:
            traceback.print_exc()
            print(f"An error occurred while executing the code from {main_path}: {e}")