import conda



# 1. create env
# 2. prepare recipe
# 3. conda build
# 4. anaconda-client upload

env_name ='py38_test_env'
create_env = conda.create_env(env_name)

activate_env = conda.activate(env_name)

# build conda build recipe\meta.yaml-- tar.tz
# test - numpy
# run  - import pandas, import numpy



