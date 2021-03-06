# Copyright (c) 2018-present, Royal Bank of Canada and other authors.
# See the AUTHORS.txt file for a list of contributors.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
#
#
# Automatically generated benchmark report (screen print of running this file)
#
# sysname: Linux
# release: 4.4.0-146-generic
# version: #172-Ubuntu SMP Wed Apr 3 09:00:08 UTC 2019
# machine: x86_64
# python: 3.6.8
# torch: 1.4.0
# torchvision: 0.5.0
# advertorch: 0.2.2

# attack type: SquareAttack
# attack kwargs: norm=Linf
#                n_restarts=1
#                n_queries=1000
#                eps=0.3
#                p_init=0.8
# data: mnist_test, 10000 samples
# model: MNIST LeNet5 standard training
# accuracy: 98.89%
# attack success rate: 100.0%

# attack type: SquareAttack
# attack kwargs: norm=L2
#                n_restarts=1
#                n_queries=1000
#                eps=2.0
#                p_init=0.8
# data: mnist_test, 10000 samples
# model: MNIST LeNet5 standard training
# accuracy: 98.89%
# attack success rate: 58.98%

# attack type: SquareAttack
# attack kwargs: norm=Linf
#                n_restarts=1
#                n_queries=1000
#                eps=0.3
#                p_init=0.8
# data: mnist_test, 10000 samples
# model: MNIST LeNet 5 PGD training according to Madry et al. 2018
# accuracy: 98.64%
# attack success rate: 10.71%

# attack type: SquareAttack
# attack kwargs: norm=L2
#                n_restarts=1
#                n_queries=1000
#                eps=2.0
#                p_init=0.8
# data: mnist_test, 10000 samples
# model: MNIST LeNet 5 PGD training according to Madry et al. 2018
# accuracy: 98.64%
# attack success rate: 60.05%



from advertorch_examples.utils import get_mnist_test_loader
from advertorch_examples.utils import get_mnist_lenet5_clntrained
from advertorch_examples.utils import get_mnist_lenet5_advtrained
from advertorch_examples.benchmark_utils import get_benchmark_sys_info

from advertorch.attacks import SquareAttack

from advertorch_examples.benchmark_utils import benchmark_attack_success_rate

batch_size = 1000
device = "cuda"

lst_attack = [
    (SquareAttack, dict(
        norm='Linf',
        n_restarts=1,
        n_queries=1000,
        eps=.3,
        p_init=.8
        )),
    (SquareAttack, dict(
        norm='L2',
        n_restarts=1,
        n_queries=1000,
        eps=2.,
        p_init=.8
        )),
]  # each element in the list is the tuple (attack_class, attack_kwargs)

mnist_clntrained_model = get_mnist_lenet5_clntrained().to(device)
mnist_advtrained_model = get_mnist_lenet5_advtrained().to(device)
mnist_test_loader = get_mnist_test_loader(batch_size=batch_size)

lst_setting = [
    (mnist_clntrained_model, mnist_test_loader),
    (mnist_advtrained_model, mnist_test_loader),
]


info = get_benchmark_sys_info()

lst_benchmark = []
for model, loader in lst_setting:
    for attack_class, attack_kwargs in lst_attack:
        lst_benchmark.append(benchmark_attack_success_rate(
            model, loader, attack_class, attack_kwargs
            ))

print(info)
for item in lst_benchmark:
    print(item)
