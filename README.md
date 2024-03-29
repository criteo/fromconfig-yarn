# FromConfig Yarn
[![pypi](https://img.shields.io/pypi/v/fromconfig-yarn.svg)](https://pypi.python.org/pypi/fromconfig-yarn)
[![ci](https://github.com/criteo/fromconfig-yarn/workflows/Continuous%20integration/badge.svg)](https://github.com/criteo/fromconfig-yarn/actions?query=workflow%3A%22Continuous+integration%22)

A [fromconfig](https://github.com/criteo/fromconfig) `Launcher` for yarn execution.

<!-- MarkdownTOC -->

- [Install](#install)
- [Quickstart](#quickstart)
- [Usage Reference](#usage-reference)
  - [Options](#options)

<!-- /MarkdownTOC -->


<a id="install"></a>
## Install

```bash
pip install fromconfig_yarn
```

<a id="quickstart"></a>
## Quickstart

Once installed, the launcher is available with the name `yarn`.

Given the following module

```python
class Model:
    def __init__(self, learning_rate: float):
        self.learning_rate = learning_rate

    def train(self):
        print(f"Training model with learning_rate {self.learning_rate}")
```


and config files

```yaml
# config.yaml
model:
  _attr_: foo.Model
  learning_rate: "${params.learning_rate}"

# params.yaml
params:
  learning_rate: 0.001

# launcher.yaml
yarn:
  name: test-fromconfig

logging:
  level: 20

launcher:
  run: yarn
```

Run (assuming you are in a Hadoop environment)

```bash
fromconfig config.yaml params.yaml launcher.yaml - model - train
```

Which prints

```
INFO:fromconfig.launcher.logger:- yarn.name: test-fromconfig
INFO:fromconfig.launcher.logger:- logging.level: 20
INFO:fromconfig.launcher.logger:- params.learning_rate: 0.001
INFO:fromconfig.launcher.logger:- model._attr_: foo.Model
INFO:fromconfig.launcher.logger:- model.learning_rate: 0.001
INFO skein.Driver: Driver started, listening on 12345
INFO:fromconfig_yarn.launcher:Uploading pex to viewfs://root/user/path/to/pex
INFO:cluster_pack.filesystem:Resolved base filesystem: <class 'pyarrow.hdfs.HadoopFileSystem'>
INFO:cluster_pack.uploader:Zipping and uploading your env to viewfs://root/user/path/to/pex
INFO skein.Driver: Uploading application resources to viewfs://root/user/...
INFO skein.Driver: Submitting application...
INFO impl.YarnClientImpl: Submitted application application_12345
INFO:fromconfig_yarn.launcher:TRACKING_URL: http://12.34.56/application_12345
```

You can also monkeypatch the relevant functions to "fake" the Hadoop environment with

```bash
python monkeypatch_fromconfig.py config.yaml params.yaml launcher.yaml - model - train
```

This example can be found in [`docs/examples/quickstart`](docs/examples/quickstart).


<a id="usage-reference"></a>
## Usage Reference

<a id="options"></a>
### Options

To configure Yarn, add a `yarn` entry to your config.

You can set the following parameters.

- `env_vars`: A list of environment variables to forward to the container(s)
- `hadoop_file_systems`: The list of available filesystems
- `ignored_packages`: The list of packages not to include in the environment
- `jvm_memory_in_gb`: The JVM memory (default, `8`)
- `memory`: The executor's memory (default, `32 GiB`)
- `num_cores`: The executor's number of cores (default, `8`)
- `package_path`: The HDFS location where to save the environment
- `zip_file`: The path to an existing `pex` file, either local or on HDFS
- `name`: The application name
- `queue`: The yarn queue to submit the application to
- `node_label`: The label of the hadoop node to be scheduled
- `pre_script_hook`: A script to be executed before python is invoked
- `extra_env_vars`: A mapping of extra environment variables to forward to the container(s)