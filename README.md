# Conservative Distributional Offline Reinforcement Learning

This is the PARK related fork for [Conservative Distributional Offline Reinforcement Learning](https://arxiv.org/abs/2107.06106).
Currently the repository is in active development and there are things to be fixed: 

Tasks: 

- [x] Port CODAC to run with PARK
- [x] Use risk penalty and risk probability in PARK environments 
- [ ] Verify and implement which dataset to be loaded, right now the train_offline script loads the epoch1 run, which should be changed. 

## Installations

The park-codac.yml file contains the conda environment. You can create this environment using the provided yml file. 

## Experiments

Right now the repository is tested on the load balance environment. 

For online training: 

```python train_online.py --env load_balance --algo codac```

Then you can run offline training: 

```python train_offline.py --env load_balance --algo codac```

## Load Balancer Results

Results from online and offline training on the expected rewards metric in the load balancer environment with the risk probability of 1 and risk penality of 0. 

Online Training Results:

<img width="725" alt="Screen Shot 2022-05-25 at 4 41 02 PM" src="https://user-images.githubusercontent.com/42305684/170363220-3c26b4cb-1028-4785-b774-556a4fed52d7.png">

Offline Training Results (Normalized Score is reward objective)

<img width="1086" alt="Screen Shot 2022-05-25 at 4 47 15 PM" src="https://user-images.githubusercontent.com/42305684/170364283-9a81890a-d7fe-42fc-8a99-3ebd44c8191b.png">

## Citations
If you find this repository useful for your research, please cite:
```
@article{ma2021conservative,
      title={Conservative Offline Distributional Reinforcement Learning}, 
      author={Yecheng Jason Ma and Dinesh Jayaraman and Osbert Bastani},
      year={2021},
      url={https://arxiv.org/abs/2107.06106}
}
```

## Contact
If you have any questions regarding the code or paper, feel free to contact me at jasonyma@seas.upenn.edu or open an issue on this repository.
## Acknowledgement
This repository contains code adapted from the 
following repositories: [pytorch-soft-actor-critic](https://github.com/pranz24/pytorch-soft-actor-critic),
 [CQL](https://github.com/aviralkumar2907/CQL), [dsac](https://github.com/xtma/dsac), [focops](https://github.com/ymzhang01/mujoco-circle) and [replication-mbpo](https://github.com/jxu43/replication-mbpo). We thank the
 authors and contributors for open-sourcing their code.  
