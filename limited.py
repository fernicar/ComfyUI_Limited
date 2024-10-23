# These are the only requirements by ComfyUI Limited; torch and similar packages will not load.
# python.exe -s -m pip install aiohttp --no-warn-script-location

# For the ComfyUI Windows portable version, you will need to adjust the path to the root like this:
# ..\python_embedded\python.exe -s -m pip install aiohttp --no-warn-script-location

# If you decide to go the embedded route, download any Python embedded distribution and edit the .pth file so that 'import site' is uncommented.
# Since embedded distributions do not have pip, you can download pip.pyz, place it next to python.exe, and use it like this:
# python.exe -s pip.pyz install aiohttp --no-warn-script-location

""" This list of custom nodes will load without errors (2024-10-21)
git clone --depth 1 --filter=blob:none https://github.com/ltdrdata/ComfyUI-Manager
git clone --depth 1 --filter=blob:none https://github.com/rgthree/rgthree-comfy
git clone --depth 1 --filter=blob:none https://github.com/yolain/ComfyUI-Easy-Use
git clone --depth 1 --filter=blob:none https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes
git clone --depth 1 --filter=blob:none https://github.com/shiimizu/ComfyUI_smZNodes
git clone --depth 1 --filter=blob:none https://github.com/pythongosssss/ComfyUI-Custom-Scripts
git clone --depth 1 --filter=blob:none https://github.com/giriss/comfy-image-saver
git clone --depth 1 --filter=blob:none https://github.com/54rt1n/ComfyUI-DareMerge
git clone --depth 1 --filter=blob:none https://github.com/jags111/efficiency-nodes-comfyui
git clone --depth 1 --filter=blob:none https://github.com/WASasquatch/was-node-suite-comfyui
git clone --depth 1 --filter=blob:none https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG
git clone --depth 1 --filter=blob:none https://github.com/TinyTerra/ComfyUI_tinyterraNodes
git clone --depth 1 --filter=blob:none https://github.com/Nourepide/ComfyUI-Allor
git clone --depth 1 --filter=blob:none https://github.com/ltdrdata/ComfyUI-Impact-Pack
git clone --depth 1 --filter=blob:none https://github.com/crystian/ComfyUI-Crystools
git clone --depth 1 --filter=blob:none https://github.com/Fannovel16/comfyui_controlnet_aux
git clone --depth 1 --filter=blob:none https://github.com/cubiq/ComfyUI_IPAdapter_plus
git clone --depth 1 --filter=blob:none https://github.com/spacepxl/ComfyUI-Florence-2
git clone --depth 1 --filter=blob:none https://github.com/Acly/comfyui-inpaint-nodes
git clone --depth 1 --filter=blob:none https://github.com/EllangoK/ComfyUI-post-processing-nodes
git clone --depth 1 --filter=blob:none https://github.com/cubiq/ComfyUI_essentials
git clone --depth 1 --filter=blob:none https://github.com/chflame163/ComfyUI_LayerStyle
git clone --depth 1 --filter=blob:none https://github.com/BadCafeCode/masquerade-nodes-comfyui
git clone --depth 1 --filter=blob:none --recursive https://github.com/receyuki/comfyui-prompt-reader-node
git clone --depth 1 --filter=blob:none https://github.com/ltdrdata/ComfyUI-Impact-Subpack ComfyUI-Impact-Pack/impact_subpack
git clone --depth 1 --filter=blob:none https://github.com/M1kep/ComfyLiterals
git clone --depth 1 --filter=blob:none https://github.com/WASasquatch/ComfyUI_Preset_Merger
git clone --depth 1 --filter=blob:none https://github.com/filliptm/ComfyUI_Fill-Nodes
git clone --depth 1 --filter=blob:none https://github.com/ssitu/ComfyUI_UltimateSDUpscale --recursive
git clone --depth 1 --filter=blob:none https://github.com/Ttl/ComfyUi_NNLatentUpscale
"""

DEBUG = False # You can see which commands are being ignored during testing.
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
    'scipy.ndimage.filters',

    # ComfyUI-Manager modules
    'git',
    'git.remote',
    'pip',
    'pip.freeze',
    'pip.main',
]

# Example whitelist
whitelist = ['aiohttp']
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

modules_with_applied_fixes = set()
def custom_fix(modules_to_mock):
    global modules_with_applied_fixes
    # Mock the module class to have the same metaclass as type
    class MockTypeMetaclass:
        pass
    # for ComfyUI-Allor avoid class CustomAbstractSession(CustomBaseSession, CustomSessionContainer): TypeError: metaclass conflict
    if 'rembg.sessions' in modules_to_mock and 'rembg.sessions' not in modules_with_applied_fixes:
        modules_with_applied_fixes.add('rembg.sessions')
        if DEBUG: print(f">\tThe workarround for ComfyUI-Allor avoid TypeError: metaclass conflict is applied")
        sys.modules['rembg.sessions'].BaseSession = MockTypeMetaclass
    # for ComfyUI_LayerStyle avoid class BiRefNet(nn.Module, PyTorchModelHubMixin): TypeError: metaclass conflict
    if 'huggingface_hub' in modules_to_mock and 'huggingface_hub' not in modules_with_applied_fixes:
        modules_with_applied_fixes.add('huggingface_hub')
        if DEBUG: print(f">\tThe workarround for ComfyUI_LayerStyle avoid TypeError: metaclass conflict is applied")
        class MockNNModule(type): # Mock nn.Module as a subclass of type
            def __init_subclass__(cls, **kwargs):
                pass
        sys.modules['torch.nn'].Module = MockNNModule
        class MockPyTorchModelHubMixin(MockNNModule): # Mock PyTorchModelHubMixin as a subclass of MockNNModule
            def __init_subclass__(cls, **kwargs):
                pass
        sys.modules['huggingface_hub'].PyTorchModelHubMixin = MockPyTorchModelHubMixin

    if 'timm.models.layers' in modules_to_mock and 'timm.models.layers' not in modules_with_applied_fixes:
        modules_with_applied_fixes.add('timm.models.layers')
        if DEBUG: print(f">\tThe workarround for comfyui_controlnet_aux numpy.pi is applied")
        sys.modules['timm.models.layers'].DropPath = MockTypeMetaclass
        sys.modules['timm.models.layers'].to_2tuple = MockTypeMetaclass
        sys.modules['timm.models.layers'].trunc_normal_ = MockTypeMetaclass
    # for ComfyUI-Crystools pynvml.nvmlDeviceGetCount return 0
    if 'pynvml' in modules_to_mock and 'pynvml' not in modules_with_applied_fixes:
        modules_with_applied_fixes.add('pynvml')
        if DEBUG: print(f">\tThe workarround for ComfyUI-Crystools pynvml.nvmlDeviceGetCount return 0 is applied")
        sys.modules['pynvml'].nvmlDeviceGetCount.return_value = 0
    # for comfyui_controlnet_aux numpy.pi
    if 'numpy' in modules_to_mock and 'numpy' not in modules_with_applied_fixes:
        modules_with_applied_fixes.add('numpy')
        if DEBUG: print(f">\tThe workarround for comfyui_controlnet_aux numpy.pi is applied")
        sys.modules['numpy'].configure_mock(pi=3.14159265359)
    # for clipseg.py and ComfyUI_Comfyroll_CustomNodes unknown problem
    if 'matplotlib' in modules_to_mock and 'matplotlib' not in modules_with_applied_fixes:
        modules_with_applied_fixes.add('matplotlib')
        if DEBUG: print(f">\tThe workarround for clipseg.py and ComfyUI_Comfyroll_CustomNodes unknown problem is applied")
        sys.modules['matplotlib.colors'] = MagicMock()

# End of specific checks by custom nodes------------------------------------------------------------

def patch_after_init_extra_nodes():
    import sys
    if 'ComfyUI-Crystools' in sys.modules:
        module = sys.modules['ComfyUI-Crystools']
        if DEBUG: print(f'\n>----------sys.modules[\'ComfyUI-Crystools\']\n{dir(module)}')
        module.cmonitor.stopMonitor()
        def mock_startMonitor(*args, **kwargs):
            return None
        module.CMonitor.startMonitor = mock_startMonitor
        if DEBUG: print(f">\tThe workarround for ComfyUI-Crystools hardware monitor crash is applied")
    custom_fix(sys.modules)

def get_modules_to_mock(log_file_path):
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as file:
            return set(file.read().splitlines())
    return set()

def update_log_file(log_file_path, module_name):
    with open(log_file_path, 'a') as file:
        file.write(f"{module_name}\n")

def mock_modules(modules):
    for module in modules:
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
        error_message = str(e).split("'")[0]
        if error_message == 'No module named ':
            return str(e).split("'")[1]
        else: return False
    if module_name in sys.modules:
        del sys.modules[module_name]
    return True

log_file_path = 'limited_modules.log'
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
            modules_to_mock.add(missing_module)
            update_log_file(log_file_path, missing_module)
            mock_modules([missing_module])
            log_modules_to_mock.append(missing_module)
            retries += 1

    if retries == retry_limit:
        if DEBUG: print(f">\tFailed to import {module_path} after {retry_limit} retries")
        return False

if DEBUG: print(f"---------------Disabled modules by Limited: {log_modules_to_mock}")


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
        # Search init_extra_nodes and add patch_after_init_extra_nodes line
        code = code.replace("    nodes.init_extra_nodes(init_custom_nodes=not args.disable_all_custom_nodes)", replacement)
        code = compile(code, main_path, 'exec') # Compile and execute the modified code
        exec(code)
